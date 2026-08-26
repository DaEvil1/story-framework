# Story Framework

A generalizable creative search system for AI-driven fiction writing.
Genre-agnostic: literary fiction, fantasy, SF, thriller, romance,
modern drama, or any combination.

## What this provides

| Layer | What it does |
|---|---|
| **Quantitative gate** | Prose rules, frequency caps, structure validation, ledger consistency |
| **Story ledgers** | 10+ YAML schemas tracking scenes, tension, questions, plants/payoffs, attachment, ambiguity, relationships, promises, world-terms, surprises, reception |
| **Analyzer + reference calibration** | Word frequency, sentence rhythm, opener dominance, abstract-agent density, dialogue music, voice fingerprints, emotion lexicons, motif co-occurrence, staleness report, atmosphere panel — thresholds calibrated against a bundled public-domain corpus |
| **50-criterion rubric** | `story_craft_criteria.md`: craft traits + reading-experience tests, pillar-grouped with spread penalties |
| **Frozen reader-state ledger** | Sequential naive-reader snapshots with prediction diffing against what the next chapter delivers |
| **Intentional-violation registry** | Regression constraints distinguished from style laws; violations allowed with a positive case on file |
| **Experiment lifecycle** | Git worktree alternate universes with PROBE→INCUBATE→CANDIDATE stages and ACCEPT/REJECT/HARVEST/DEFER outcomes |
| **Red-team protocol** | Adversarial cold-read personas with panel scoring |
| **Editorial board** | Deliberative body that debates findings and produces unified recommendations |
| **Character board** | Autonomy check: characters assess whether their portrayal matches their self-concept |
| **Council of Readers** | Target-audience members score experience and communication fidelity |
| **Pairwise judging** | Blind OLD/NEW comparison with horizon-aware questions |
| **Zero-based audit** | Periodic architectural review assuming load-bearing decisions are wrong |

`python init.py <name>` scaffolds all of this into a ready-to-write project:
tools, ledgers, board protocols, rubric, reference corpus, and the
`docs/AUTONOMOUS_RUN.md` phase state machine (premise → bookends →
experimental middle → consolidation → experiment loops → 3 final passes →
content-complete).

## The key principle

> Internal institutions may discover questions. They should rarely dictate answers.

The framework constrains weaknesses (context loss, prose tics, self-congratulation) while protecting the irrationality that produces genuine discovery. Infrastructure freezes after initial setup; further gains come from running experiments, not adding machinery.

## First case study

*Something Was Left Behind* (DaEvil1/test-story-ox): literary SF novella,
~11k words, taken from first draft to content-complete over 12 revision
cycles. Raw rubric: 5.2 → 7.46. Council score: 8.0 → 8.3. Red-team panel:
7.0 → 7.7.
