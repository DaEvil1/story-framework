# Frozen Reader-State Ledger

Simulated naive-reader cognition, snapshotted after each chapter of a
sequential first read. Purpose: measure **prediction error** and
**communication fidelity** — not what the author put in the text, but what
actually built up in a reader.

## Procedure

1. Fresh context. Read ONLY chapters 1..N, in order. No outline, no intent
   docs, no ledgers, no later chapters.
2. Immediately fill `after_chNN.yaml` using the schema below, in the
   reader's own uncertain voice. Guesses included; certainty marked.
3. Freeze. Never edit an old snapshot after reading further.
4. When chapter N+1 exists, run `python tools/reader_diff.py` — it places
   the frozen predictions beside what chapter N+1 actually delivers.
   Hit / miss / surprised calls are judgment, recorded in
   `tests/PREDICTION_DIFF.md`, and feed the surprise ledger (#47).

## Known limitation

One model simulating its own reader carries correlated blind spots. The
value is longitudinal: systematic misses (reader never notices X, reader
always certain when design wanted doubt) are structural facts about the
text even under correlation.

## Schema

```yaml
chapter_read: N
believes_happened: []        # events as understood, including wrong guesses
trust: []                    # who the reader trusts/distrusts, and why
protagonist_wants: ""        # what the reader believes the protagonist wants
character_beliefs: {}        # per-character status theories, e.g. {mentor: "alive but hiding"}
central_mystery_belief: ""   # current theory of the story's central unknown
questions_holding: []        # live questions the reader is actively holding
predictions_next: []         # explicit "I expect..." statements
confused_by: []
emotionally_strongest: ""
seems_like_foreshadowing: []
fuzzy_or_forgotten: []       # details already slipping
```

Adapt `character_beliefs` keys to YOUR cast; keep them stable across all
snapshots so longitudinal drift is visible.
