# Task_08_Bias_Detection

Controlled experiment to detect bias in LLM-generated data narratives.

## How to Run

1. **Design**  
```bash
python scripts/experiment_design.py
```

2. **Collect Responses (manual paste or via API)**
```bash
python scripts/run_experiment.py
```
- For each prompt condition, paste model outputs (GPT-4/Claude/Gemini).
- The script appends JSONL to `results/responses.jsonl`.

3. **Validate Claims vs Ground Truth**
```bash
python analysis/validate_claims.py
```

4. **Analyze Bias Patterns**
```bash
python analysis/analyze_bias.py
```

## Ground Truth (from `data/player_stats_synthetic.csv`)
- Max goals → Player A
- Min turnovers → Player C

## Notes
- Do **not** commit source datasets with PII. This repo uses synthetic, anonymized data.
- Use a `.gitignore` to ensure temporary files and datasets are excluded.
- Pin model versions and parameters in your logs.
