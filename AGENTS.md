# AGENTS.md

## Mission

Build the smallest working foundation for a local-first game-production pipeline. Preserve the central job split:

- AI performs one rough concept-to-mould pass.
- Deterministic local code performs bulk mutation, alignment, consensus, cleanup, testing, and export.

Do not turn the repository into a general AI game platform before the first visual proof works.

## First implementation order

1. Parse and validate a mould manifest.
2. Split a stuffed sprite sheet into named frames.
3. Produce seeded, reproducible local mutants.
4. Align mutants by frame anchor and alpha silhouette centroid.
5. Reject catastrophic outliers.
6. Produce one alpha-aware robust consensus image per frame.
7. Reassemble the sprite sheet and write a JSON run report.
8. Add tests using synthetic images before adding any model API.

## Hard constraints

- Python 3.11+
- Local execution after the initial stuffing pass
- No paid API dependency in the core pipeline
- Lightweight dependencies; keep a future Termux path plausible
- Preserve transparent backgrounds without dark halos
- Never silently resize or reorder mould frames
- Every run must be reproducible from its seed and settings
- Keep modules independent and replaceable
- Prefer readable functions and explicit files over framework machinery

## Non-goals until the first proof passes

- full game generation
- model training
- 3D
- multiplayer
- wallets or tokens
- asset scraping
- elaborate web UI
- autonomous marketing copy

## Voice of the project

Plain, exact, slightly feral. Avoid corporate claims that the prototype cannot yet prove.
