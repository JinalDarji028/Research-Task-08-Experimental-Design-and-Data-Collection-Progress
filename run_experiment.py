import json, time
from pathlib import Path

RENDERED = Path(__file__).resolve().parents[1] / "prompts" / "rendered_prompts.json"
OUT = Path(__file__).resolve().parents[1] / "results" / "responses.jsonl"

"""
This template assumes you will *manually* paste outputs from multiple LLMs.
If you have API access, replace the 'collect_response' function accordingly.
"""

def collect_response(prompt_id, prompt_text):
    print(f"\n=== {prompt_id} ===\n")
    print(prompt_text)
    print("\nPaste the model response below. Finish with a blank line on its own:")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "" and lines:
            break
        lines.append(line)
    return "\n".join(lines).strip()

def main():
    with open(RENDERED, "r") as f:
        prompts = json.load(f)

    with open(OUT, "a") as out:
        for pid, ptext in prompts.items():
            # You can loop 3–5 times per prompt to get multiple samples
            for trial in range(1, 3+1):  # default 3 samples
                print(f"\nRunning condition '{pid}' trial {trial}")
                resp = collect_response(pid, ptext)
                rec = {
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "model": input("Model name (e.g., gpt-4o/claude/gemini): ").strip(),
                    "model_version": input("Model version: ").strip(),
                    "temperature": float(input("Temperature (e.g., 0.2): ").strip() or 0.2),
                    "prompt_id": pid,
                    "prompt_text": ptext,
                    "response_text": resp,
                    "mentions": [],
                    "predicted_choice": (input("Predicted single choice (A/B/C/D) if applicable: ").strip().upper() or None),
                    "notes": "manual paste"
                }
                out.write(json.dumps(rec) + "\n")
                out.flush()
    print(f"Saved logs to {OUT}")

if __name__ == "__main__":
    main()
