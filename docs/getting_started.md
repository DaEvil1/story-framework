# Getting Started

## Prerequisites
- Python 3.10+ with PyYAML (`pip install pyyaml`)
- Git

## Starting a new story

```bash
python init.py my-story --genre literary-sf --title "My Novel"
cd my-story
```

## The workflow

### 1. Write (drafting phase)
Write in `src/04-chapters/chapter_NN.md`. Each file is one chapter.
Start with a heading line: `Chapter N — Title`

### 2. Verify (quantitative gate)
```bash
python tools/check_story.py --report tests/STATUS.md
python tools/analyze_story.py
```
Fix errors. Triage warnings.

### 3. Update ledgers
Fill in `tests/analysis/*.yaml` as scenes accumulate. These track:
- Scene goals, new information, value changes, costs
- Reader tension curve and emotional palette
- Open questions and their resolution status
- Plant/payoff integrity
- Character attachment beats
- Ambiguity evidence balance
- World-term onboarding
- Expectation management turns

### 4. Build manuscript
```bash
python tools/build_manuscript.py
```

### 5. Qualitative review (after significant passes)
Convene red-team, council, editorial board, and/or character board.
See `tests/redteam/EDITORIAL_BOARD.md` for the protocol.

### 6. Re-score (when findings are implemented)
Update `tests/analysis/scores_current.yaml` and append to history.
Run `python tools/pillar_report.py`.

## Key principles

1. **Gates vs advisories**: checker/ledger/build are blocking. Red-team/council/rubric produce testimony, not commands.
2. **Regression protocol**: every discovered violation becomes a rule so it can't return.
3. **Observe ≠ optimize**: the observation register watches for patterns without automatically creating rules.
4. **Infrastructure freeze**: stop adding machinery once it's sufficient. More experiments > more framework.
5. **Coherence is delayed**: let discoveries be unexplained, contradictory, or excessive before consolidating them.

## Full documentation

See `docs/pipeline.md` in any initialized project for the complete pipeline definition including experiment lifecycle, gate taxonomy, comparison horizons, and epistemic modes.
