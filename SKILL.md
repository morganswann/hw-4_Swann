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
Liability,Lorde,heartbreak
Die For You,The Weeknd,late night
MONTERO,Lil Nas X,villain era
Good as Hell,Lizzo,hot girl walk
Stronger,Kanye West,rage
Coffee for Your Head,beabadoobee,sunday morning
Bohemian Rhapsody,Queen,karaoke
So High School,Taylor Swift,heartbreak
Blinding Lights,The Weeknd,late night
Espresso,Sabrina Carpenter,hot girl walk
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

## Output

A plain-text playlist printed to stdout:

```
🎵 Your Playlist:
1. Liability — Lorde [heartbreak]
2. So High School — Taylor Swift [heartbreak]
3. Blinding Lights — The Weeknd [late night]
4. Coffee for Your Head — beabadoobee [late night]
5. Espresso — Sabrina Carpenter [hot girl walk]
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
