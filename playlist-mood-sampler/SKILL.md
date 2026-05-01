---
name: playlist-mood-sampler
description: "Randomly generates a playlist from a personal song library that hits an exact mood quota. Given a CSV of songs tagged with mood labels (e.g. heartbreak, villain era, sunday morning) and a quota like {\"heartbreak\": 3, \"hot girl walk\": 2}, the script samples from each mood bucket without replacement and returns a numbered playlist. Use when someone wants a mood-balanced playlist from their own library, or when a DJ or event planner needs a structured setlist with exact song counts per vibe — especially for weddings, parties, or other events where each moment needs a distinct mood."
---

# playlist-mood-sampler

## What this skill does

Generates a randomized playlist from a personal song library that hits an exact mood quota.

Given a CSV of songs tagged with mood labels and a quota like `{"heartbreak": 3, "villain era": 2}`, the script randomly samples from each mood bucket without replacement and returns a playlist that satisfies the quota exactly.

This requires a script because:
- CSV parsing must be handled deterministically
- Random sampling without replacement cannot be done reliably by a language model
- Exact quota enforcement and error handling (e.g. not enough songs in a category) require real code logic

## When to use this skill

### Personal listening
Use when someone wants a mood-balanced playlist from their own library:
- "Make me a playlist — 3 heartbreak songs, 2 villain era, and 2 sunday morning"
- "I want a road trip mix but mostly rage and hot girl walk"
- "Shuffle my library but weight it toward late night vibes"

### Event planning
Use when a DJ, wedding planner, or host needs to build a structured setlist from a curated song library:
- "I'm DJing a wedding — give me 10 cocktail hour songs, 5 ceremony songs, and 20 reception bangers"
- "Build me a party setlist: 8 hype songs, 4 slow songs, and 3 karaoke closers"
- "I need a first-dance shortlist from my romantic songs folder"

This is especially powerful for weddings, where each moment of the event (ceremony, cocktail hour, first dance, reception, last song) needs a distinct vibe and exact song counts matter.

Do NOT use this skill to:
- Look up songs or artists from external sources
- Infer moods from song titles or artist names
- Generate or recommend songs the user did not provide

## Inputs

| Input | Format | Description |
|-------|--------|-------------|
| `library.csv` | CSV file | Song library with columns: `title`, `artist`, `mood` |
| `quota` | JSON object | Mood labels mapped to desired count, e.g. `{"heartbreak": 3, "hot girl walk": 2}` |

### Example CSV (`library.csv`)

```
title,artist,mood
It'll Be Okay,Rachel Grae,heartbreak
Me,Kelly Clarkson,heartbreak
Man I Need,Olivia Dean,in love
WHERE IS MY HUSBAND,RAYE,in love
For Tonight,GIVEON,late night
Top Down,3Quency,late night
NISSAN ALTIMA,Doechii,villain era
Misery Business,Paramore,karaoke
Little Girl Gone,CHINCHILLA,rage
You're Still The One,Teddy Swims,sunday morning
```

### Example quota

```json
{
  "heartbreak": 2,
  "late night": 2,
  "hot girl walk": 1
}
```

## Supported mood labels

The skill accepts any mood labels the user defines in their CSV. Suggested labels:

- `heartbreak` — emotional, post-breakup
- `in love` — romantic, warm, butterflies
- `late night` — moody, atmospheric
- `villain era` — dark, empowering
- `hot girl walk` — confident, upbeat
- `karaoke` — crowd-pleasers, belters
- `rage` — high energy, cathartic
- `sunday morning` — slow, cozy, low energy

## Step-by-step instructions

1. **Prepare your song library** — create a CSV file with three columns: `title`, `artist`, `mood`. Tag each song with one of your mood labels. Save it somewhere accessible (e.g. `references/library.csv`).
2. **Define your quota** — decide how many songs you want from each mood as a JSON object, e.g. `{"heartbreak": 2, "villain era": 2, "sunday morning": 1}`.
3. **Run the script** — call `sample_playlist.py` with `--csv` pointing to your library and `--quota` as a JSON string.
4. **Check the output** — the script prints a numbered playlist to stdout. If any mood bucket doesn't have enough songs to fulfill the quota, it raises a clear error telling you which mood needs more songs.
5. **Optional: use a seed** — pass `--seed <number>` to lock in a specific result and get the same playlist every time you run it.

## Limitations & checks

- The CSV must have exactly these column headers: `title`, `artist`, `mood` (case-sensitive)
- Mood labels in the quota must exactly match the labels in the CSV (e.g. `"hot girl walk"` ≠ `"Hot Girl Walk"`)
- The skill will error clearly if a mood bucket has fewer songs than the quota requests — add more songs to that category to fix it
- Songs are sampled without replacement — no duplicates in a single playlist run

## Output

A plain-text playlist printed to stdout:

```
🎵 Your Playlist:
1. It'll Be Okay — Rachel Grae [heartbreak]
2. Man I Need — Olivia Dean [in love]
3. NISSAN ALTIMA — Doechii [villain era]
4. You're Still The One — Teddy Swims [sunday morning]
```

## Script

See `scripts/sample_playlist.py`

### Usage

```bash
python scripts/sample_playlist.py --csv library.csv --quota '{"heartbreak": 2, "late night": 2, "hot girl walk": 1}'
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--csv` | Yes | Path to the song library CSV |
| `--quota` | Yes | JSON string with mood-to-count mapping |
| `--seed` | No | Integer seed for reproducible results |
