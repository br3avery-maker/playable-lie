# Architecture

## 1. The Hoard

A license-clean collection of 2D game assets with machine-readable metadata:

- SHA-256 identity
- perceptual similarity hash
- creator and source
- license and attribution requirements
- dimensions, frame count, palette, alpha, category, and tags
- style-family and compatibility relationships

The Hoard is not required for the first visual proof, but the manifests must be designed so it can plug in later.

## 2. The Mould

A mould defines the structural grammar the generated concept must inhabit:

- sprite-sheet dimensions
- named frame rectangles
- animation order and timing
- anchor or foot point per frame
- optional silhouette masks
- optional palette constraints
- transparent-background requirements

The mould solves structure before generation begins.

## 3. Rough stuffing

An image model or crude mapping step produces one imperfect sheet. This is the only step that may require expensive generative compute.

The stuffed sheet is a seed, not final art.

## 4. The Mutant Mill

The local pipeline generates reproducible nearby variants using cheap operations such as:

- integer and subpixel shifts
- controlled local warps
- morphology
- outline expansion and contraction
- palette nudges
- alpha cleanup variations
- seeded noise
- small region-preserving scale changes

Mutation must remain constrained enough that variants still fit the mould.

## 5. Alignment and rejection

Each frame is separated and normalized. Variants are aligned using the frame anchor, transparent bounds, and silhouette centroid. Catastrophic outliers are rejected using configurable thresholds.

## 6. Flat Pageant Princess / The Press

The Press finds the stable character hiding inside the mutant swarm. Initial strategies:

- alpha-aware channel median
- trimmed mean
- silhouette majority vote
- palette-constrained nearest-color selection
- isolated-pixel cleanup
- edge and outline repair

The Press must not be a naïve blur average.

## 7. The Toybox

Later, tested game systems replace one-shot code generation:

- movement and collision
- animation state machines
- dialogue and quests
- inventory and equipment
- combat and health
- crafting and progression
- save/load
- trading and ownership adapters

Agents select and connect these modules rather than rewriting them from scratch.

## 8. The Builder

An agentic team coordinates asset selection, mould choice, module assembly, execution, playtesting, repair, and export. It should expose failures and artifacts rather than hiding them behind a polished demo.
