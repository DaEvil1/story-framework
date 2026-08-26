# Tests

Quality checks for the story, split by how they run.

## `automated/` — enforced by script

- `rules.yaml` — machine-checkable prose and structure rules (banned phrases,
  patterns, duplicate-title detection).
- `prose_rules.md` — the human-readable spec for those rules, plus the list of
  judgment calls that need manual review.

Run after every drafting session:

```
python tools/check_story.py                          # console report
python tools/check_story.py --report tests/STATUS.md # also regenerate status file
python tools/check_story.py --strict                 # warnings fail too
```

Requires Python 3.10+ and PyYAML (`pip install pyyaml`).

**Regression protocol:** when you find a violation during editing or review,
add its pattern to `rules.yaml` so it can never silently reappear. Log
substantive rule changes in `docs/decisions.log`.

## `manual/` — judgment checklists

Reviewed by a read-through, not pattern-matched:

- `character_arcs.md`, `consistency.md`, `motif_usage.md`,
  `plot_completeness.md`, `style.md`, `thematic_coherence.md`
  (+ project-specific checklists as your story demands)

Manual review results are recorded in `VALIDATION_REPORT.md`.

## `analysis/` — story ledgers and generated metrics

Machine-readable descriptions of the story that the checker validates:

- `scene_ledger.yaml` — per-scene goal / new-info / value-change / cost /
  stakes; enforces escalation, costs, civic stakes (`SL-*` rules)
- `tension_ledger.yaml` — perceived tension curve and feeling variety (`TN-*`)
- `ambiguity_ledger.yaml` — evidence for rival readings of open questions (`AM-*`)
- `relationship_ledger.yaml` — lived-presence targets for key characters (`RL-*`)
- `promise_ledger.yaml` — book claims mapped to delivering beats (`PL-*`)
- plus questions, plant/payoff, attachment, surprise, worldterms, reception

Plus scoring infrastructure:

- `pillars.yaml` — criteria grouped into interacting systems (spread-penalized)
- `scores_current.yaml` / `scores_history.yaml` — rubric scores over time
- `reception_scores.yaml` — red-team panel + council session scores

And generated analytics:

- `ANALYSIS.md` — **generated**, do not edit:

```
python tools/analyze_story.py
```

## `reader_state/` — frozen naive-reader snapshots

Sequential first-read cognition after each chapter; see its README.
Diffed by `tools/reader_diff.py` into `PREDICTION_DIFF.md`.

## Generated files

- `STATUS.md` — per-chapter automated results. **Generated — do not edit.**
- `ANALYSIS.md` — statistical analysis. **Generated — do not edit.**
- `VALIDATION_REPORT.md` — living record of manual validation and open gaps.

When the story changes materially, update the ledgers in the same session,
then re-run checker + analyzer before committing.
