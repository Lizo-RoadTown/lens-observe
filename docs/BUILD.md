# lens-observe — build-out plan (self-directed)

This is lens-observe's own plan for working itself out. Work top-down; check items off
and append what you learned. Precedent to consult (not to copy as identity): the
PROVES reference inventory at
`tapestry/docs/decomposition/proves/process-log.md`, and the PROVES spine
`staging_extractions → validation_decisions → core_entities`.

## What lens-observe must become

- [ ] **1. Signal computation.** Compute signals over records / activity —
  active / orphaned / degrading / blind. The **input source is injected**, so the
  same computation serves both a lab (watching its target system) and the
  platform/loom layer (watching our own projects).
- [ ] **2. A store + read for signals.** Persist computed signals and expose them for
  reading.
- [ ] **3. The `observe` CLI.** Runs compute → store → read end-to-end.
- [ ] **4. Tests.** Signal computation (fixture activity), store + read round-trip.
  Mirror the stdlib + pytest style of `tapestry-cli`.

### Migrate-from (precedent, generalize — do not copy as identity)
- Tapestry `services/project-observatory/`:
  - `signals.py`, `compute_signals.py` — the hot_path / orphaned / degrading / blind
    design.
  - migration 006 `observation_signals`.
- Note: project-observatory is itself a scaffold — its compute / read are **unbuilt**.
  lens-observe can be where that logic actually gets built, and the platform layer
  then borrows it. Keep the input source injected so both observatories share one
  module.

## What you own vs. don't
Own: signals compute + read. Do NOT implement the pipeline here — no intake, review,
promotion, or serve. lens-observe is the watcher only.

## Record as you go
Append here: what you built, what you needed, what's missing, what you had to decide.
Also write it to loom-memory scoped to `lens-observe`. This log is capture-before-loss.
