# Autonomous Run Protocol

This document defines the complete state machine for autonomously writing,
revising, and finishing a novella using the story-framework. Follow these
phases in order. Do not skip gates. Do not add machinery.

## Ground rules

1. You are the writer AND the reviewer. Use different modes for different
   tasks, but never let the reviewer mode contaminate the writer mode.
2. Infrastructure is frozen. Do not add new tools, rules, or protocols.
   If you find a problem the tools don't catch, note it and move on.
3. Coherence is delayed. Early chapters may be unexplained, contradictory,
   or excessive. Consolidation comes AFTER generation, not during.
4. When bored, branch. When stale, rewrite. When curious, dive.
   You do not need permission or evidence to explore.

---

## PHASE 0: PREMISE & CHARACTERS

**Goal:** Know who the people are and what world they inhabit.

1. Imagine 2–4 major characters. For each, write in `src/02-characters/`:
   - Name, role, one-line description
   - What they want (conscious goal)
   - What they fear (unconscious need)
   - One contradiction (how they betray themselves)
   - Voice note (how they speak differently from others)

2. Write a premise paragraph (NOT an outline) in `src/01-world/concept.md`:
   - What is the central tension?
   - What is the world's relationship to the story's themes?
   - What is at stake?

3. Write one sentence about the setting in `src/01-world/setting.md`.

**Exit when:** character sketches exist, premise paragraph exists.
**Tools:** none required yet.
**Do NOT:** outline chapters, design magic systems, draw maps, name factions.

---

## PHASE 1: BOOKENDS

**Goal:** Write the first and last chapters. Know where you start and end.

1. Write `chapter_01.md`: Who is this person BEFORE anything changes?
   Show their ordinary life, their contradiction in action, their voice.
2. Write `chapter_last.md`: Who is this person AFTER everything has changed?
   Show the cost. Show what remains. Do not explain the middle.

**Run:** `python tools/check_story.py`
**Run:** `python tools/analyze_story.py`

**Exit when:** checker passes, both chapters feel like the same hand wrote
them despite depicting different states.

**Do NOT:** connect them yet. Do not outline what happens between them.
The gap between ch1 and ch-last IS the story. You'll discover it, not plan it.

---

## PHASE 2: EXPERIMENTAL MIDDLE

**Goal:** Write the middle by following threads, not outlines.

### Session loop (repeat until story connects):

1. **Creative pulse:** What does the story want right now? Trust your
   instinct. If bored, skip ahead. If excited about a tangent, follow it.
2. **Write one scene** into the next chapter file. Start mid-situation
   if possible. End on a pull, not a resolution.
3. **Update ledgers** for the new scene:
   - Scene ledger (goal, new_info, value_change, cost)
   - Tension ledger (score, feeling)
   - Open questions (if new questions raised)
   - Plant/payoff (if objects/details introduced)
4. **Run checker** — fix errors only.
5. **Every 3–4 scenes:** run analyzer, review open questions ledger.
   Are you still heading toward the ending you wrote in Phase 1?
   If yes: continue. If no: **that's fine. Update the last chapter
   or write a new one.** The bookends serve the story, not vice versa.

### Sub-phase rules

- Write scenes out of order if that's how they come to you.
- Skip transitional scenes; fill gaps later or discover they weren't needed.
- When a character makes a decision you didn't expect: **follow it.**
  Update your understanding of who they are. Let it change subsequent scenes.
- When you discover something that contradicts earlier material:
  **do not fix it yet.** Note it. Keep writing. Reconcile in Phase 3.

### Exit when:

- Story connects beginning to end (even if roughly)
- OR word count approaches target_word_count × 0.9
- OR you've gone 3 sessions without adding a scene that feels necessary
- OR you have 8+ chapters

**Minimum viable:** 6 chapters. **Typical:** 8–12. **Maximum before Phase 3:** 15.

**Run:** full tool stack (checker, analyzer, build).
**Convene:** editorial board to discuss findings.

---

## PHASE 3: FIRST FULL PASS

**Goal:** Make the rough middle into a coherent book.

1. **Cold read** the assembled manuscript. No tools. No notes. Just read.
   Then write one paragraph: what was the experience like? What do you
   remember? What felt flat?

2. **Structural revision** based on cold-read + editorial board findings:
   - Cut scenes that don't earn their place
   - Reorder if chronology serves theme better than chronology serves chronology
   - Merge duplicate beats
   - Fill genuine gaps (not perceived ones — actual holes in logic or emotion)

3. **Ledger sync:** bring all ledgers current with the revised text.

4. **Run:** full tool stack.

**Exit when:** checker clean, manuscript reads as coherent whole,
editorial board has discussed findings.

---

## PHASE 4: EXPERIMENT ITERATION LOOPS

**Goal:** Search for improvements that polishing can't reach.

Each loop = 3 experiments (different operators) + consolidation + verification.

### Per-loop procedure

1. **Choose 3 experiments** with different operators (dive, fork, rewrite,
   veto, mutation, zero-base, wild). At least one must challenge a
   load-bearing assumption.
2. **Execute each** through the lifecycle: PROBE → INCUBATE → CANDIDATE.
3. **Judge blind**: OLD vs NEW, anonymized, randomized, 3 fresh contexts.
4. **Close**: ACCEPT / REJECT / HARVEST / DEFER.
5. **Consolidate**: merge accepted changes, sync ledgers, rebuild.
6. **Verify**: full tool stack.

### Loop-level tracking (record per experiment)

- Operator + trigger + proposer + scope
- Distance traveled (low / medium / high / very-high)
- Furthest stage reached
- Outcome (accept / reject / harvest / defer)
- Judge margin (how close was the vote?)
- Later rollback or regression?

### STOP CONDITIONS (check after each loop)

| Condition | Test |
|---|---|
| Plateau | All 3 experiments in current loop produced negligible improvement |
| Double-dismissal | All experiments rejected/dismissed 2 consecutive loops |
| Max loops | 12 loops completed (≈36 experiments) |
| Species change | Story has become a fundamentally different book |

If any stop condition triggers: move to Phase 5.

**Typical:** 6–10 loops. **Maximum:** 12.

---

## PHASE 5: FINAL PASSES (exactly 3, then stop)

**Pass 1 — Voice harmonization:** ensure all chapters sound like one author.
Check register consistency, dialogue music, body-metonymy density.

**Pass 2 — Consistency audit:** run all ledgers against final text.
Timeline, object chains, who-knows-what, sensory palette continuity.

**Pass 3 — Line polish:** rhythm, crutch removal, opener variety,
em-dash density, fragment-run frequency. Final checker + analyzer run.

After Pass 3: declare content-complete. Log in decisions.log.
Set `status: content-complete` in book.yaml.

**DO NOT continue after Pass 3.** The book is done. Further changes are
over-working, not improving.

---

## Metrics reference

| Metric | Healthy range | Source |
|---|---|---|
| Sentence mean length | 8–24 words | Analyzer |
| Sentence stdev | ≥7 (canon varies 12–17) | Analyzer |
| Em-dash density | 30–80 per 10k | Analyzer |
| Opener dominance ("The") | <20% | Analyzer |
| Abstract-of frames | <8 per 10k | Analyzer |
| Body-part metonymy | <12 per 10k | P12 scan |
| Dialogue share | 7–42% | Analyzer |
| Motif FUSED pairs | 0 pairs above 60% | Analyzer co-occurrence |
| FQ warnings | ≤3 per chapter | Checker |
| NC warnings | ≤2 per chapter | Checker |

---

## What NOT to do

- Do not add new tools, rules, or protocols during a run
- Do not convene committees during PROBE stage
- Do not explain themes through narrator commentary
- Do not resolve ambiguities because unresolved things feel dangerous
- Do not force connections between unrelated discoveries
- Do not keep writing past Phase 5 because "one more pass might help"
