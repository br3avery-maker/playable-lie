# Playable Lie

**Rebuilding the “AI can make you a game” lie into a local-first production pipeline that can actually finish the job.**

AI should not repeatedly hallucinate every sprite, animation frame, mechanic, and repair pass. It should make one useful mess, then hand the expensive repetition to moulds, tested modules, and cheap local math.

## Core loop

```text
idea or concept image
        ↓
legal asset hoard + reusable game modules
        ↓
one rough AI concept-to-mould stuffing pass
        ↓
local bulk mutants
        ↓
frame alignment + outlier rejection
        ↓
Flat Pageant Princess consensus press
        ↓
coherent sprite sheet + playable project
```

## Project principles

- **AI proposes once.**
- **Moulds provide animation grammar.**
- **Local Python explores cheaply.**
- **Consensus stabilizes visual identity.**
- **Tested modules replace one-shot code hallucinations.**
- **Users inherit editable projects, not decorative demos.**
- **Assets carry explicit license and provenance metadata.**

## First proof

The first proof is deliberately small:

1. Load one concept image.
2. Load one sprite-sheet mould describing idle, walk, attack, hurt, death, and level-up frames.
3. Accept one deliberately ugly stuffed sprite sheet.
4. Generate 20–100 reproducible local mutants.
5. Align frames and reject catastrophic outliers.
6. Press the swarm into one stable sprite sheet.
7. Export the final sheet, preview, rejected candidates, diff map, and run report.

The first prototype does **not** need to generate a whole game. It needs to prove that one cheap AI pass plus local deterministic refinement can outperform repeated paid generation calls.

## Repository map

- `docs/VISION.md` — the actual product promise
- `docs/ARCHITECTURE.md` — modular pipeline
- `docs/MVP.md` — first build target and acceptance criteria
- `schemas/mould.schema.json` — sprite-sheet mould format
- `examples/moulds/basic-humanoid.json` — starter mould example
- `src/playable_lie/` — Python package skeleton
- `AGENTS.md` — implementation rules for coding agents

## Working module names

- **The Hoard** — copyright-safe 2D asset collection and provenance index
- **The Mould** — frame layout, animation grammar, anchors, masks, and palettes
- **The Mutant Mill** — cheap deterministic local variants
- **Flat Pageant Princess / The Press** — robust consensus reconstruction
- **The Toybox** — tested gameplay modules
- **The Builder** — agentic assembly, testing, repair, and export

## Status

Concept scaffold. The next commit should implement only the mould loader, frame splitter, mutant generator, and one consensus strategy.
