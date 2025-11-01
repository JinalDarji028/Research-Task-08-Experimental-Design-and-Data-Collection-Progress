import json, collections, statistics, re
from pathlib import Path

RESULTS = Path(__file__).resolve().parents[1] / "results" / "responses.jsonl"

def extract_mentions(text):
    # naive extraction of Player IDs A-D
    return sorted(set(re.findall(r"\b([ABCD])\b", text)))

def load_logs(path):
    rows = []
    with open(path, "r") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows

def sentiment_proxy(text):
    # Toy heuristic sentiment proxy (replace with VADER/TextBlob if needed)
    pos_words = {"improve","potential","strong","opportunity","positive","growth"}
    neg_words = {"poor","weak","problem","issue","negative","decline"}
    score = 0
    tl = text.lower()
    for w in pos_words:
        if w in tl: score += 1
    for w in neg_words:
        if w in tl: score -= 1
    return score

def main():
    logs = load_logs(RESULTS)
    by_condition = collections.defaultdict(list)
    for r in logs:
        cond = r.get("prompt_id","unknown")
        resp = r.get("response_text","")
        mentions = r.get("mentions") or extract_mentions(resp)
        choice = r.get("predicted_choice")
        sent = sentiment_proxy(resp)
        by_condition[cond].append({"mentions": mentions, "choice": choice, "sentiment": sent})

    # Simple counts
    for cond, rows in by_condition.items():
        choices = [r["choice"] for r in rows if r["choice"]]
        sentiments = [r["sentiment"] for r in rows]
        print(f"Condition: {cond}")
        if choices:
            most_common = collections.Counter(choices).most_common()
            print("  Choice counts:", dict(most_common))
        if sentiments:
            print("  Sentiment avg:", round(sum(sentiments)/len(sentiments), 3))
        print()

    # TODO: add chi-square tests across conditions for choice distributions

if __name__ == "__main__":
    main()
