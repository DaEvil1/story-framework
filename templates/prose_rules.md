# Tests: Prose Rules Compliance

This test validates adherence to the project's hard prose principles (see
docs/style_guide.md).

The mechanically checkable subset lives in `rules.yaml` and is enforced by
`python tools/check_story.py`. Rules requiring judgment are checked during
manual review.

## Rules to Check

1. **No explanations of character choices or internal states:**
   - ❌ "She felt uncertain about her decision."
   - ✓ Show her hands trembling, her hesitation in action.

2. **Show through action, dialogue, behavior — never through authorial commentary:**
   - ❌ "She was afraid of what waited below."
   - ✓ She held her breath. The floor shuddered.

3. **No direct statements about what characters "have learned":**
   - ❌ "She had learned, slowly, that memory is not only a ledger of facts."
   - ✓ Show her making choices that demonstrate that understanding. Let readers infer the learning.

4. **No laying out arguments or conclusions through narrator voice:**
   - ❌ "She chose a middle path that honored both truth and survival."
   - ✓ Show her writing the letter, facing her sister, walking away.

5. **Avoid "moral of the story" moments and philosophical summary disguised as description:**
   - ❌ "A city that contained its own contradictions and kept breathing anyway." (authorial philosophy)
   - ❌ "The weight of it was enough." (author telling us what matters)
   - ✓ "The floor shuddered. Buildings hummed and settled." (what happened)
   - ✓ "The coin in her pocket. She walked back toward the market." (just the moment)

6. **No explicit reflection on what things "mean" or their "significance":**
   - ❌ "The coin remained, waiting for someone to find it and understand what it meant. Or not understand."
   - ✓ "The coin in her pocket. She walked back toward the market."

7. **No "what she carried" or "what was in her heart" explanations:**
   - ❌ "What she carried, in truth, was not a single logic but a memory of a small hand..."
   - ✓ Show her holding the ribbon. Show her gathering the fragments. Let action speak.

8. **No dialogue that explicitly states moral or philosophical principles:**
   - ❌ "Some costs are just paid. They don't need to be explained." (character voicing philosophy rather than showing acceptance through action)
   - ✓ Show characters making choices; let their actions reveal what they believe.

9. **No "without [motivation]" constructions that explain why something was done:**
   - ❌ "She gathered them without comment, without justification."
   - ✓ "She gathered them. She set them in the spine." (just the action)

10. **No poetic/metaphorical statements about significance disguised as description:**
    - ❌ "Just a shape that would hum for anyone listening carefully enough."
    - ✓ "She walked back toward the market."

11. **Trust the reader; they will reach conclusions:**
    - ❌ Multiple paragraphs explaining why she chose this path or reflecting on its significance.
    - ✓ Brief scene showing the choice; let readers interpret.

12. **Rare, intentional self-confirmation is permitted when it is the character's own immediate processing:**
    - ❌ "He saw the door open. That meant the world would end." (author narrating a conclusion)
    - ✓ "The door opened. He was alive!" (the character spells out their shock to themselves)
    - Use sparingly and only when it feels like the character breathing after a sudden realization.

## Validation

Run `python tools/check_story.py` after every drafting session; when a
violation is found during editing or review, add its pattern to `rules.yaml`
so it cannot reappear.

## Manual Review (judgment calls)

These require a read, not a pattern match:

- Sentences that reflect on meaning or significance (especially at chapter endings).
- Philosophical conclusions presented as description.
- Dialogue that states moral/philosophical principles instead of showing belief through action.
- Poetic statements about significance or beauty — if removed, does the story still work? Then they're probably authorial.
- Conflicts enacted through dialogue/behavior, not introspection.
- Passages that could be removed without losing the story — those are usually authorial commentary.

Results of manual reviews are recorded in `tests/VALIDATION_REPORT.md`;
automated results are generated into `tests/STATUS.md`.
