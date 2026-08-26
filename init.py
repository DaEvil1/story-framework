"""Story Framework — initialize a new fiction project.

Usage:
    python init.py <project-name> [--genre <genre>] [--title "<title>"]

Creates a new directory with the full scaffolding: src/, tests/, tools/,
docs/, templates for all ledger and config files, and the verification
stack. Ready to write chapter 1 immediately.
"""

import argparse
import shutil
import sys
from pathlib import Path

FRAMEWORK_ROOT = Path(__file__).resolve().parent
TEMPLATES = FRAMEWORK_ROOT / "templates"
TOOLS = FRAMEWORK_ROOT / "tools"

DIRS = [
    "src/01-world",
    "src/02-characters",
    "src/03-outlines",
    "src/04-chapters",
    "src/05-canon",
    "tests/automated",
    "tests/manual",
    "tests/redteam",
    "tests/council",
    "tests/character_board",
    "tests/analysis",
    "docs",
    "output",
    "drafts",
    "drafts/discovery_buffer",
]

CHAPTER_TEMPLATE = """Chapter 1 — [Title]

[Write your opening here. The hook should create a question or imbalance
within the first scene. Curiosity or unease should precede understanding.]
"""

LEDGER_SCHEMES = {
    "scene_ledger.yaml": """# Scene Ledger
# One entry per scene. Validated by tools/check_story.py (rules SL-*).
# Fields:
#   goal            - what the POV character wants in this scene
#   new_info        - information the READER gains here for the first time
#   value_change    - yes-but | no-and | flat
#   cost_paid       - what the scene extracts (none if free)
#   irreversible    - true if a cost/door here can never be undone
#   opponent_pressure - none | archive | limit | character-name
#   stakes_scope    - personal | civic

scenes: []
thresholds:
  min_costs_total: 3
  min_irreversible_costs: 1
  max_info_overlap: 0.5
  require_civic_stakes: true
""",
    "ambiguity_ledger.yaml": """# Ambiguity Ledger
# For each deliberately unresolved question, evidence for rival readings.

questions: []
""",
    "tension_ledger.yaml": """# Tension & Feeling Ledger
# Per-scene perceived tension (0-10) and dominant reader feeling.

scenes: []
thresholds:
  min_stdev: 1.2
  min_peak: 8
  min_valley: 3
  min_peak_count: 2
  min_valley_count: 2
  max_consecutive_equal: 2
  min_distinct_feelings: 6
""",
    "questions_ledger.yaml": """# Open-Loops (Reader Questions) Ledger

loops: []
thresholds:
  max_simultaneously_open: 6
  max_open_chapters_without_reminder: 5
""",
    "plantpayoff_ledger.yaml": """# Plant/Payoff Ledger
# Everything planted must pay off; everything paid off must be planted.

items: []
""",
    "attachment_ledger.yaml": """# Attachment Ledger
# Reasons the reader cares about each character BEFORE the story spends them.

characters: []
""",
    "relationship_ledger.yaml": """# Relationship Ledger
# Lived presence test: characters act, speak, or react within rendered scenes.

characters: []
""",
    "worldterms_ledger.yaml": """# World-Term Onboarding Ledger

terms: []
thresholds:
  max_definition_lag: 3
""",
    "surprise_ledger.yaml": """# Surprise Ledger (Expectation Management)

turns: []
thresholds:
  min_shift_ratio: 0.5
  max_confirmed_ratio: 0.3
""",
    "reception_ledger.yaml": """# Reception Ledger
# Cold-reader bookkeeping: stakes legibility, immersion breakers,
# judgment pressure, title payoffs.

act_stakes_legibility: []
immersion_breakers: []
reader_judgment_pressure: []
title_payoffs: []
""",
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python init.py <project-name> [--genre <genre>] [--title <title>]")
        sys.exit(1)

    name = sys.argv[1]
    genre = "literary-sf"
    title = "Untitled"
    for i, arg in enumerate(sys.argv):
        if arg == "--genre" and i + 1 < len(sys.argv):
            genre = sys.argv[i + 1]
        if arg == "--title" and i + 1 < len(sys.argv):
            title = sys.argv[i + 1]

    root = Path(name)
    if root.exists():
        print(f"'{name}' already exists.", file=sys.stderr)
        sys.exit(1)

    root.mkdir(parents=True)

    # Directory tree
    for d in DIRS:
        (root / d).mkdir(parents=True, exist_ok=True)

    # Copy tools
    tools_dst = root / "tools"
    tools_dst.mkdir(exist_ok=True)
    for f in TOOLS.glob("*.py"):
        shutil.copy2(f, tools_dst / f.name)

    # Copy rules template
    rules_src = TEMPLATES / "rules.yaml"
    if rules_src.exists():
        shutil.copy2(rules_src, root / "tests" / "automated" / "rules.yaml")

    # Write ledger schemas
    analysis = root / "tests" / "analysis"
    for fname, content in LEDGER_SCHEMES.items():
        (analysis / fname).write_text(content, encoding="utf-8")

    # Story config
    story_yaml = f'title: "{title}"\nstatus: drafting\n'
    story_yaml += f'genre: "{genre}"\n'
    story_yaml += "target_word_count: 10000\nmax_word_count: 50000\nchapters: []\n"
    (root / "story.yaml").write_text(story_yaml, encoding="utf-8")

    book_yaml = f'title: "{title}"\nstatus: drafting\ngenre: {genre}\n'
    book_yaml += "target_word_count: 10000\nmax_word_count: 50000\nchapters: []\n"
    (root / "book.yaml").write_text(book_yaml, encoding="utf-8")

    # First chapter
    (root / "src" / "04-chapters" / "chapter_01.md").write_text(
        CHAPTER_TEMPLATE, encoding="utf-8")

    # Discovery buffer
    buffer = root / "drafts" / "discovery_buffer.md"
    buffer.write_text(
        "# Discovery Buffer\n\n"
        "Things that appeared while writing and feel alive. Un-scored,\n"
        "no justification required.\n", encoding="utf-8")

    # Empty docs
    (root / "docs" / "pipeline.md").write_text(
        "# Pipeline\n\nSee the story-framework repo for the canonical pipeline\n"
        "documentation. This file will be customized per project.\n",
        encoding="utf-8")
    (root / "README.md").write_text(f"# {title}\n\nA {genre} story.\n", encoding="utf-8")

    # .gitignore
    (root / ".gitignore").write_text(
        "__pycache__/\n.experiments/\n*.pyc\noutput/\n", encoding="utf-8")

    # Init git
    import subprocess
    subprocess.run(["git", "init"], cwd=root, capture_output=True)
    subprocess.run(["git", "add", "-A"], cwd=root, capture_output=True)
    subprocess.run(["git", "commit", "-m", "init: scaffold from story-framework"],
                   cwd=root, capture_output=True)

    print(f"\nInitialized '{name}' ({genre})")
    print(f"  {len(DIRS)} directories created")
    print(f"  Tools copied from framework")
    print(f"  Git initialized with initial commit")
    print(f"\nNext steps:")
    print(f"  1. Fill in book.yaml / story.yaml with your premise")
    print(f"  2. Write src/04-chapters/chapter_01.md")
    print(f"  3. python tools/check_story.py")
    print(f"  4. Define your red-team personas in tests/redteam/")
    print(f"  5. Define your council members in tests/council/")


if __name__ == "__main__":
    main()
