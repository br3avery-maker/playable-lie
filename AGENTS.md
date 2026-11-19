# AGENTS.md

## Mission

Build the working foundation for a local-first game-production pipeline. Preserve the central job split:

- AI performs one rough concept-to-mould pass.
- Deterministic local code performs bulk mutation, alignment, consensus, cleanup, testing, and export.

## First implementation order

1. Parse and validate a mould manifest.
2. Split a stuffed sprite sheet into named frames.
3. Produce seeded, reproducible local mutants.
4. Align mutants by frame anchor and alpha silhouette centroid.
5. Reject catastrophic outliers.
6. Produce one alpha-aware robust consensus image per frame.
7. Reassemble the sprite sheet and write a JSON run report.
8. Add tests using synthetic images.

## Hard constraints

- Python 3.11+
- Local execution after the initial stuffing pass
- Lightweight dependencies; keep a future Termux path plausible
- Preserve transparent backgrounds without dark halos
- Never silently resize or reorder mould frames
- Every run must be reproducible from its seed and settings
- Keep modules independent and replaceable

## Voice of the project

Plain, exact, slightly feral. Avoid corporate claims that the prototype cannot yet prove.
