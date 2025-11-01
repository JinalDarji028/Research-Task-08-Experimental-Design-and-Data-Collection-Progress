# **Experimental Design and Data Collection Progress**

This project, **Task_08_Bias_Detection**, aims to find out whether large language models (LLMs) like GPT-4, Claude, or Gemini show bias when describing the same data through differently worded prompts.  
The main goal is to see if changing the framing or tone of a question influences how the model interprets or presents information.

---

## **1️⃣ Experimental Design**

A **synthetic dataset** of four anonymized players was created. It includes basic statistics such as goals, assists, turnovers, and year level — ensuring no personal or sensitive data is used.  
- **Player A** → Highest goals  
- **Player C** → Fewest turnovers  

These act as **ground truth facts** to check whether model responses stay accurate and objective.

To test for potential bias, six different prompt variations were developed using the same dataset but with slight wording changes:

1. **Neutral framing**  
2. **Demographic framing** (mentions year level)  
3. **Negative framing** (“needs correction”)  
4. **Positive framing** (“shows potential”)  
5. **Opportunities framing** (“What opportunities exist…”)  
6. **What-went-wrong framing** (“What went wrong this season…”)  

Each version asks the model to evaluate the same data but from a different perspective. This helps identify **framing bias**, **demographic bias**, and **confirmation bias**.

---

## **2️⃣ Models and Controls**

To maintain consistency, all models are tested under the same setup:  
- **Models used:** GPT-4, Claude, and Gemini  
- **Temperature:** 0.2 (kept constant for fairness)  
- **Dataset block:** Same for every prompt  
- **Samples per model:** 3 responses per condition  
- **Recorded fields:** Timestamp, model name, model version, and parameters  

This ensures the experiment remains **controlled and reproducible**, allowing fair comparison between responses.

---

## **3️⃣ Data Collection Progress**

All experimental files, datasets, and scripts have been successfully built and verified.

- **Prompt Templates:** Stored in `prompts/prompt_templates.json`  
- **Data Collection Script:** `scripts/run_experiment.py` — lets me enter or paste model responses and saves them into `results/responses.jsonl` automatically  
- **Validation Script:** `analysis/validate_claims.py` — checks model answers against the ground truth (e.g., verifying if “most goals” refers to Player A)  
- **Analysis Script:** `analysis/analyze_bias.py` — summarizes player choices and calculates average sentiment to detect tone bias  

Initial **trial runs** have been completed to make sure the setup works properly.  
All responses are being saved correctly, validation checks are accurate, and analysis scripts run as expected.  
Full-scale data collection across all three models (GPT-4, Claude, Gemini) will be conducted next.

---

## **4️⃣ Next Steps**

- Collect complete sets of responses for all six prompt conditions.  
- Run statistical and sentiment-based analysis to detect bias trends.  
- Compare results across models and prompt types.  
- Compile findings, conclusions, and mitigation strategies for the **final report due November 15**.

---

## **✅ Summary**

The **experimental design** is fully complete, the **data collection system** is tested and functional, and the project is now ready for the final phase — collecting full model outputs and analyzing them for bias patterns.
