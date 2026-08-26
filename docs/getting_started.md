# Getting Started

## Prerequisites
- Python 3.10+ with PyYAML (`pip install pyyaml`)
- Git

## Starting a new story

```bash
python init.py stories/my-story --genre literary-sf --title "My Novel"
cd stories/my-story
```

Each story is a self-contained git repo (the experiment lifecycle needs real
worktrees). The framework repo ignores `stories/`, so completed stories stay
local — give a story its own remote if you want it backed up. Starting the
next story is just another `init.py` run with a new name; nothing is shared
between runs except the framework itself.

The scaffold includes everything: tool stack, board protocols and persona
templates, all ledgers, the 50-criterion rubric (`docs/story_craft_criteria.md`),
the frozen reader-state protocol, the reference calibration corpus
(`references/`), and the full run documentation (`docs/AUTONOMOUS_RUN.md`,
`docs/pipeline.md`). `book.yaml` is the single config file the tools read.

## The workflow

### 0. Configure (once)
Fill in `book.yaml` (genre, themes, motifs), `docs/authorial_intent.md`,
and `docs/style_guide.md`. Adapt red-team personas
(`tests/redteam/personas.md`) and define council members BEFORE their first
verdicts. Then follow `docs/AUTONOMOUS_RUN.md` Phase 0.

### 1. Write (drafting phase)
Write in `src/04-chapters/chapter_NN.md`. Each file is one chapter.
Start with a heading line: `Chapter N — Title`

### 2. Verify (quantitative gate)
```bash
python tools/check_story.py --report tests/STATUS.md
python tools/analyze_story.py
```
Fix errors. Triage warnings. Deliberate violations of warning-level rules
get registered in `tests/intentional_violations.yaml` with a positive case.

### 3. Update ledgers
Fill in `tests/analysis/*.yaml` in the SAME session that changes the story.
These track scene goals/costs, tension curve, open questions, plant/payoff
(including protected texture locals), attachment, ambiguity evidence,
world-term onboarding, expectation turns — plus the promise ledger mapping
book.yaml claims to delivering beats.

After each new chapter: freeze a naive-reader snapshot in
`tests/reader_state/`, then run `python tools/reader_diff.py`.

### 4. Build manuscript
```bash
python tools/build_manuscript.py
```

### 5. Calibrate (after early chapters)
Run the analyzer over the reference corpus and compare:
```bash
python tools/analyze_story.py --chapters-dir references --report tests/REFERENCE_ANALYSIS.md
```
Record threshold decisions in a dated `docs/reference_calibration_*.md`.
Canon bands beat guessed thresholds.

### 6. Qualitative review (after significant passes)
Convene red-team (panel score → `tests/reception_scores.yaml`), Council,
editorial board, and/or character board. Record findings as session reports;
triage via `docs/integrator_triage_template.md`.

### 7. Re-score (when findings are implemented)
Update `tests/analysis/scores_current.yaml`, append a snapshot to history,
run `python tools/pillar_report.py`, and describe qualitative gains in
`docs/craft_narrative.md`. Lessons from experiment cycles go into
`docs/experiment_lessons.md` as provisional hypotheses.

## Key principles

1. **Gates vs advisories**: checker/ledger/build are blocking. Red-team/council/rubric produce testimony, not commands.
2. **Regression protocol**: every discovered violation becomes a rule so it can't return; positive cases become intentional-violations entries, not style laws.
3. **Observe ≠ optimize**: the observation register watches for patterns without automatically creating rules.
4. **Infrastructure freeze**: stop adding machinery once it's sufficient. More experiments > more framework.
5. **Coherence is delayed**: let discoveries be unexplained, contradictory, or excessive before consolidating them.

## Full documentation

`docs/pipeline.md` (canonical process definition), `docs/AUTONOMOUS_RUN.md`
(the phase state machine), `docs/story_craft_criteria.md` (the rubric),
`docs/metric_interactions.md` (metric couplings).
