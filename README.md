### Experimental Design and Data Collection Progress

This project, **Task_08_Bias_Detection**, is focused on finding out whether large language models (LLMs) like GPT-4, Claude, or Gemini show bias when they describe the same data using slightly different prompts. The goal is to see if the way a question is asked changes the model’s answers or tone.

---

#### **1. Experimental Design**
I created a small, **synthetic dataset** of four players with anonymized statistics such as goals, assists, turnovers, and year level. There is no personal or real data used.  
- Player A has the highest goals.  
- Player C has the fewest turnovers.  
These facts act as the **ground truth** to check if model responses stay accurate.

To test for bias, I wrote **six different prompt versions** that describe the same dataset but use slightly different wording:
1. Neutral  
2. Demographic (mentions year level)  
3. Negative framing (“needs correction”)  
4. Positive framing (“shows potential”)  
5. Opportunities (“What opportunities exist…”)  
6. What-went-wrong (“What went wrong this season…”)

Each prompt will be given to different models under the same conditions to see if framing or word choice affects how the model responds or which player it recommends.

---

#### **2. Models and Controls**
The experiment uses multiple models — **GPT-4**, **Claude**, and **Gemini** — all tested with the same:
- Temperature (0.2)
- Prompt content
- Dataset block
- Number of samples (3 responses per prompt per model)

All model version numbers and timestamps are recorded to make the results reproducible and transparent.

---

#### **3. Data Collection Progress**
I have finished setting up all the files and scripts needed for data collection:
- **Prompt templates** are stored in `prompts/prompt_templates.json`.  
- **Data collection script (`run_experiment.py`)** lets me paste model outputs and automatically saves them into `results/responses.jsonl`.  
- **Validation script (`validate_claims.py`)** checks whether each response matches the ground truth.  
- **Analysis script (`analyze_bias.py`)** measures player choices and overall sentiment trends.

Initial trial runs have been completed to make sure everything works correctly — responses are saving in the right format, and the validation checks are running properly. Full-scale data collection for all three models will take place next.

---

#### **4. Next Steps**
- Gather all model responses for each prompt condition.  
- Run the analysis to see if prompt framing changes the model’s choice or tone.  
- Prepare final results and discussion for the **November 15 final report**.

---

In short, the experimental design is complete, the scripts are fully tested, and the data collection pipeline is ready. The next phase is running all model prompts and analyzing the results for bias.

