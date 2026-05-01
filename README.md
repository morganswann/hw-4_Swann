# hw-4: playlist-mood-sampler

## What the skill does

`playlist-mood-sampler` generates a randomized playlist from a personal song library that hits an exact mood quota. You give it a CSV of songs tagged with mood labels and tell it how many songs you want from each mood — it randomly samples from each bucket and returns a numbered playlist with no repeats.

This is especially useful for personal listening (when you want a specific vibe mix) and event planning (like building a wedding setlist where each moment needs a distinct mood and exact song counts matter).

## Why I chose it

I wanted a skill that felt personal and had a real use case beyond a generic example. Playlist curation is something people actually do — especially for events like weddings where a DJ needs 10 cocktail hour songs, 5 ceremony songs, and 20 reception bangers. The script is genuinely load-bearing here because a language model can't reliably do random sampling without replacement or enforce exact quotas — that has to be code.

## How to use it

1. Add your songs to `references/library.csv` with three columns: `title`, `artist`, `mood`
2. Tag each song with a mood label (e.g. `heartbreak`, `villain era`, `hot girl walk`)
3. Ask the agent for a playlist with a specific quota, e.g.:
   > "Make me a hype playlist — 3 hot girl walk songs and 2 villain era songs from my library"
4. The agent runs `scripts/sample_playlist.py` and returns a numbered playlist

You can also pass `--seed` for reproducible results.

## What the script does

`scripts/sample_playlist.py` handles all the deterministic work:
- Parses the CSV file
- Groups songs into mood buckets
- Randomly samples from each bucket without replacement
- Enforces exact quotas and raises a clear error if a mood bucket doesn't have enough songs
- Prints a numbered playlist to stdout

This is the part that prose alone cannot do reliably — the randomness, the quota enforcement, and the error handling all require real code logic.

## What worked well

- Mixing multiple moods into a single combo playlist worked great — for example, generating 3 hot girl walk + 2 villain era songs in one run produced a natural, balanced result
- The error handling was helpful and clear — when asked for 10 heartbreak songs with only 6 in the library, the agent explained exactly what was available rather than failing silently
- The skill correctly declined to search Spotify or look up external songs, staying within its defined scope

## Limitations

- **Manual library updates** — adding new songs requires editing the CSV by hand, which can get tedious as your library grows
- **Shuffle Abilities** — the skill will not shuffle two or more moods without your prompt
- **No mood inference** — the skill cannot guess a song's mood from its title or artist; every song must be manually tagged by the user

## Video Walkthrough

[https://youtu.be/a474cfh_IZg](https://youtu.be/a474cfh_IZg)
