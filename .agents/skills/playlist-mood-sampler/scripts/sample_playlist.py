import argparse
import csv
import json
import random
import sys
from collections import defaultdict


def main():
    parser = argparse.ArgumentParser(description="Sample songs from a CSV by mood quota.")
    parser.add_argument("--csv", required=True, help="Path to CSV file with columns: title, artist, mood")
    parser.add_argument("--quota", required=True, help='JSON string mapping mood labels to counts, e.g. \'{"heartbreak": 2}\'')
    parser.add_argument("--seed", type=int, help="Random seed for reproducible results")
    args = parser.parse_args()

    try:
        quota = json.loads(args.quota)
    except json.JSONDecodeError as e:
        sys.exit(f"Error: --quota is not valid JSON: {e}")

    try:
        with open(args.csv, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except FileNotFoundError:
        sys.exit(f"Error: CSV file not found: {args.csv}")
    except Exception as e:
        sys.exit(f"Error reading CSV: {e}")

    buckets = defaultdict(list)
    for row in rows:
        mood = row.get("mood", "").strip()
        if mood:
            buckets[mood].append(row)

    if args.seed is not None:
        random.seed(args.seed)

    playlist = []
    for mood, count in quota.items():
        available = buckets.get(mood, [])
        if len(available) < count:
            sys.exit(
                f"Error: mood '{mood}' needs {count} song(s) but only {len(available)} available."
            )
        playlist.extend(random.sample(available, count))

    for i, song in enumerate(playlist, 1):
        print(f"{i}. {song['title']} — {song['artist']} [{song['mood']}]")


if __name__ == "__main__":
    main()
