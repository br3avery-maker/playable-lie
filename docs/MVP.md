# MVP: Flat Pageant Princess

## Inputs

- one rough stuffed sprite sheet
- one validated mould manifest
- variant count
- mutation strength
- random seed

## Outputs

- final sprite sheet
- contact sheet or animated preview
- rejected-outlier sheet
- seed-to-final difference map
- JSON run report containing settings, hashes, frame metrics, and rejection reasons

## Acceptance criteria

- Exact mould dimensions and frame order are preserved.
- Alpha remains clean and transparent regions do not acquire dark halos.
- The same character remains recognizable across animation frames.
- Stable details survive while one-off mutations are suppressed.
- Runs are deterministic for the same input, manifest, settings, and seed.
- Mutation, alignment, pressing, and export run locally without a model API.
- The first implementation works on modest Linux hardware.

## Initial tests

1. A synthetic geometric character with known frame anchors.
2. Transparent PNGs containing deliberate alpha-edge defects.
3. Mutants with controlled shifts and isolated-pixel corruption.
4. One deliberately ugly real stuffed sheet.

## First milestone

Prove that the pressed output is measurably and visibly more stable than the rough seed across at least one small animation mould.
