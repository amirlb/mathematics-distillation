import json
import os
import requests
import time
from concurrent.futures import ThreadPoolExecutor
from jinja2 import Template
from tqdm import tqdm
import argparse

MODEL_ID = os.getenv("MODEL_ID", "qwen/qwen3.5-9b")
API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_llm(prompt):
    if not API_KEY:
        raise ValueError("OPENROUTER_API_KEY environment variable is not set")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": MODEL_ID,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
    }
    for attempt in range(3):
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=60
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
            else:
                print(f"Error calling LLM after 3 attempts: {e}")
    return None

def evaluate_sample(sample, template):
    prompt = template.render(equation1=sample["equation1"], equation2=sample["equation2"])
    response = call_llm(prompt)
    if response is None:
        return None

    verdict = None
    for line in response.splitlines():
        line = line.strip().upper()
        if "VERDICT:" in line:
            if "TRUE" in line:
                verdict = True
            elif "FALSE" in line:
                verdict = False
            break
    return verdict

def process_file(filepath, template, max_workers=10, limit=None):
    samples = []
    if not os.path.exists(filepath):
        print(f"File {filepath} not found.")
        return 0, 0, 0, 0
    with open(filepath, "r") as f:
        for line in f:
            samples.append(json.loads(line))

    if limit:
        samples = samples[:limit]

    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(evaluate_sample, sample, template) for sample in samples]
        for i, future in enumerate(tqdm(futures, desc=f"Evaluating {filepath}")):
            verdict = future.result()
            results.append({
                "id": samples[i]["id"],
                "expected": samples[i]["answer"],
                "predicted": verdict
            })

    correct = sum(1 for r in results if r["predicted"] is not None and r["expected"] == r["predicted"])
    total = len(results)
    valid = sum(1 for r in results if r["predicted"] is not None)
    accuracy = correct / total if total > 0 else 0
    return accuracy, correct, total, valid

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--subset", type=int, help="Limit number of samples per set for testing")
    parser.add_argument("--workers", type=int, default=10, help="Number of parallel workers")
    args = parser.parse_args()

    with open("eval_prompt_template.txt", "r") as f:
        template_str = f.read()
    template = Template(template_str)

    sets = ["data/val.jsonl", "data/train.jsonl"]
    report = "Performance Report:\n"
    report += f"Model: {MODEL_ID}\n\n"

    for s in sets:
        print(f"Processing {s}...")
        acc, corr, tot, val = process_file(s, template, max_workers=args.workers, limit=args.subset)
        report += f"{s}:\n"
        report += f"  Accuracy: {acc:.2%} ({corr}/{tot})\n"
        report += f"  Valid responses: {val}/{tot}\n\n"

    print(report)
    with open("performance_report.txt", "w") as f:
        f.write(report)

if __name__ == "__main__":
    main()
