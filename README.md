# Mathematics Distillation Challenge: Equational Theories

This repository is dedicated to the [Mathematics Distillation Challenge: Equational Theories (Stage 1)](https://competition.sair.foundation/competitions/mathematics-distillation-challenge-equational-theories-stage1/).

The challenge focuses on exploring the space of equational theories of magmas, ordered by implication. It involves proving or disproving implications between thousands of equational laws.

## Data

The relevant data files for this challenge are sourced from the [SAIR Foundation on Hugging Face](https://huggingface.co/datasets/SAIRfoundation/equational-theories-selected-problems).

- `data/normal.jsonl`: Normal difficulty problems (1000 items).
- `data/hard.jsonl`: Hard difficulty problems (200 items).
- `data/train.jsonl`: Merged training set (80% split).
- `data/val.jsonl`: Merged validation set (10% split).
- `data/test.jsonl`: Merged test set (10% split).

## Evaluation

The repository includes `eval_prompt_template.txt`, which is the Jinja2 template used for evaluating model performance on these problems.

## Challenge Links

- [Official Challenge Site](https://competition.sair.foundation/competitions/mathematics-distillation-challenge-equational-theories-stage1/)
- [Equational Theories Project (GitHub)](https://github.com/teorth/equational_theories)
- [Equational Theories Project (Website)](https://teorth.github.io/equational_theories/)
