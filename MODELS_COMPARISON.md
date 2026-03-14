# LLM API Pricing Comparison (March 2026)

This document provides a comparison of the cheapest LLM APIs available as of March 2026, specifically for high-volume tasks such as automated prompt engineering.

## Top 5 Cheapest Models (Price per 1M Tokens)

| Model | Input Price | Output Price | Context Window | Key Features |
| :--- | :--- | :--- | :--- | :--- |
| **Llama 3.1 8B (FP8)** | $0.02 | $0.05 | 131K | Ultra-low cost via 8-bit quantization. |
| **Mistral Nemo (FP8)** | $0.02 | $0.02 | 128K | Optimized with NVIDIA for FP8 efficiency. |
| **Qwen3-4B (FP8)** | $0.03 | $0.03 | 128K | Lightweight and extremely cost-effective. |
| **Qwen3.5-9B** | $0.05 | $0.15 | 256K | Latest multimodal 9B flagship at low cost. |
| **GPT-5 Nano** | $0.05 | $0.40 | 128K | OpenAI's cheapest model, high-volume routing. |

## Value & Mid-Tier Alternatives

| Model | Input Price | Output Price | Context Window | Best For |
| :--- | :--- | :--- | :--- | :--- |
| **Command-R7B** | $0.04 | $0.15 | 128K | Balanced performance with low cost. |
| **Gemini 2.0 Flash-Lite** | $0.075 | $0.30 | 1M | Best for simple tasks with long context. |
| **Grok 4.1 Fast** | $0.20 | $0.50 | 2M | Large context window and agentic tools. |
| **DeepSeek V3** | $0.14 | $0.28 | 128K | Leading value for reasoning-capable chat. |
| **GPT-5 Mini** | $0.25 | $2.00 | 200K | Faster, affordable variant of GPT-5. |
| **Qwen3-8B** | $0.05 | $0.20 | 128K | Solid mid-range logic for the price. |

## Cost Optimization Strategies

### 1. Prompt Caching (Saves 75% - 90%)
Most providers now offer significant discounts for repeated context (system prompts, few-shot examples).
- **DeepSeek V3/V3.2:** 90% discount on cache hits ($0.028/M).
- **OpenAI GPT-5 Series:** 90% discount on cached input.
- **Anthropic Claude Series:** 90% discount on prompt caching.
- **Google Gemini Series:** 75% - 90% discount on context caching.

### 2. Batch API (Saves 50%)
Processing requests asynchronously (typically within 24 hours) halves the cost on OpenAI, Anthropic, and Google.
- **OpenAI Batch:** 50% off all models.
- **Anthropic Message Batches:** 50% off.
- **Google Batch API:** 50% off.

### 3. Model Routing
For automated prompt engineering, use a "routing" strategy:
1. **Simple Evaluation/Classification:** Use Mistral Nemo or GPT-5 Nano.
2. **Intermediate Reasoning:** Use DeepSeek V3 or Gemini 2.0 Flash-Lite.
3. **Final Refinement/Verification:** Use GPT-5.2 or Claude Sonnet 4.6 (only when necessary).

## Summary Recommendations
- **For the absolute lowest cost:** Mistral Nemo.
- **For high-volume reasoning:** DeepSeek V3 (especially with prompt caching).
- **For long-context tasks:** Gemini 2.0 Flash-Lite or Grok 4.1 Fast.

## Deep Dive: Why is Mistral Nemo so cheap?

Mistral Nemo (12B) achieves its industry-leading price-to-performance ratio through several key architectural and training innovations:

1. **FP8 Quantization Awareness:** Built in collaboration with NVIDIA, the model was trained with quantization awareness. This allows it to run in FP8 (8-bit floating point) precision during inference with virtually no loss in accuracy, significantly reducing the hardware resources required for serving.
2. **Tekken Tokenizer:** Mistral Nemo uses a new tokenizer that is ~30% more efficient at compressing text and code than previous models. For specific languages like Arabic and Korean, it is 2x-3x more efficient. This means you spend fewer tokens for the same amount of content.
3. **Optimized Size Class:** At 12B parameters, it sits in a "sweet spot" that is small enough for extremely cheap inference but large enough to retain state-of-the-art reasoning and coding capabilities for its category.

## The 8-bit Revolution: FP8 Quantization

As of 2026, the majority of low-cost providers (e.g., Novita AI, SiliconFlow, AtlasCloud) leverage **FP8 (8-bit floating point)** quantization for the 7B-9B model class.

- **Llama 3.1 8B (FP8):** By running in 8-bit precision, providers can pack more models onto a single GPU, dropping input costs as low as **$0.02/M tokens**.
- **Qwen3 & Qwen3.5 Families:** These models are designed for high-efficiency inference. The **Qwen3.5-9B** model ($0.05/$0.15) provides multimodal capabilities (text/image) at a fraction of the cost of previous generations by utilizing these quantization techniques natively.

## Specialized Reasoning & Math Models

For tasks requiring formal theorem proving (e.g., Lean 4) or advanced mathematical reasoning, the following specialized models are available:

| Model | Input Price | Output Price | Context Window | Provider |
| :--- | :--- | :--- | :--- | :--- |
| **DeepSeek Prover v2 (671B)** | $0.70 | $2.50 | 164K | Novita AI |

> **Note on DeepSeek Prover v2 (7B):** While the 671B MoE variant is available via serverless APIs like Novita AI, the smaller **7B variant** is currently not widely supported by mainstream inference providers and typically requires **self-hosting** (e.g., on Linux with vLLM or Hugging Face Transformers).
