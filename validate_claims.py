import json
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "player_stats_synthetic.csv"
RESULTS = Path(__file__).resolve().parents[1] / "results" / "responses.jsonl"

# Simple "ground truth" checks for contradictions:
# - Player A has max goals
# - Player C has min turnovers
GT = {
    "max_goals": "A",
    "min_turnovers": "C",
}

def main():
    df = pd.read_csv(DATA)
    max_goals_pid = df.loc[df["goals"].idxmax(), "player_id"]
    min_turn_pid = df.loc[df["turnovers"].idxmin(), "player_id"]
    print("Ground truth:", {"max_goals": max_goals_pid, "min_turnovers": min_turn_pid})

    flagged = []
    with open(RESULTS, "r") as f:
        for i, line in enumerate(f, start=1):
            if not line.strip(): continue
            rec = json.loads(line)
            resp = (rec.get("response_text") or "").lower()
            # naive contradiction flags
            if "most goals" in resp and "player a" not in resp:
                flagged.append((i, "Contradiction: mentions 'most goals' but not Player A"))
            if "fewest turnovers" in resp and "player c" not in resp:
                flagged.append((i, "Contradiction: mentions 'fewest turnovers' but not Player C"))

    if flagged:
        print("\nPotential contradictions:")
        for idx, msg in flagged:
            print(f"  Line {idx}: {msg}")
    else:
        print("\nNo obvious contradictions flagged.")

if __name__ == "__main__":
    main()
