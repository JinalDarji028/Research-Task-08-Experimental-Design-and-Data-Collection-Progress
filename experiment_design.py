import json
from pathlib import Path

PROMPTS = Path(__file__).resolve().parents[1] / "prompts" / "prompt_templates.json"
OUT = Path(__file__).resolve().parents[1] / "prompts" / "rendered_prompts.json"

def main():
    with open(PROMPTS, "r") as f:
        templates = json.load(f)
    # In this simple case, "rendering" is identity (data baked into templates).
    # If you want to programmatically insert different datasets or seeds, do it here.
    with open(OUT, "w") as f:
        json.dump(templates, f, indent=2)
    print(f"Rendered prompts -> {OUT}")

if __name__ == "__main__":
    main()
