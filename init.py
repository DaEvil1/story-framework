"""Story Framework — initialize a new fiction project.

Usage:
    python init.py <project-name> [--genre <genre>] [--title "<title>"]

Creates a new directory with the full scaffolding: src/, tests/, tools/,
docs/, templates for all ledger and config files, the verification stack,
the reference calibration corpus, and the canonical run documentation.
Ready to write chapter 1 immediately.
"""

import shutil
import sys
from pathlib import Path

FRAMEWORK_ROOT = Path(__file__).resolve().parent
TEMPLATES = FRAMEWORK_ROOT / "templates"
TOOLS = FRAMEWORK_ROOT / "tools"
DOCS = FRAMEWORK_ROOT / "docs"

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
    "tests/reader_state",
    "references",
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
# status: texture marks PROTECTED LOCALS — deliberately unconnected details,
# exempt from orphan warnings, reviewed at zero-based audits.

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

# Template files copied verbatim into the project (template-relative -> project-relative)
FILE_COPIES = [
    # Quantitative gate config + spec
    ("rules.yaml", "tests/automated/rules.yaml"),
    ("prose_rules.md", "tests/automated/prose_rules.md"),
    # Board protocols
    ("redteam/personas.md", "tests/redteam/personas.md"),
    ("redteam/persona_templates.md", "tests/redteam/persona_templates.md"),
    ("redteam/EDITORIAL_BOARD.md", "tests/redteam/EDITORIAL_BOARD.md"),
    ("editorial_session_template.md", "tests/redteam/editorial_session_template.md"),
    ("council/README.md", "tests/council/README.md"),
    ("council/member_templates.md", "tests/council/member_templates.md"),
    ("character_board/README.md", "tests/character_board/README.md"),
    ("character_board/role_templates.md", "tests/character_board/role_templates.md"),
    ("character_board/session_template.md", "tests/character_board/session_template.md"),
    ("integrator_triage_template.md", "docs/integrator_triage_template.md"),
    ("zero_base_audit_template.md", "docs/zero_base_audit_template.md"),
    # Tool-consumed ledgers + scoring infrastructure
    ("ledgers/promise_ledger.yaml", "tests/analysis/promise_ledger.yaml"),
    ("ledgers/pillars.yaml", "tests/analysis/pillars.yaml"),
    ("ledgers/scores_current.yaml", "tests/analysis/scores_current.yaml"),
    ("ledgers/scores_history.yaml", "tests/analysis/scores_history.yaml"),
    ("ledgers/intentional_violations.yaml", "tests/intentional_violations.yaml"),
    ("ledgers/reception_scores.yaml", "tests/reception_scores.yaml"),
    # Reader-state protocol
    ("reader_state_README.md", "tests/reader_state/README.md"),
    # Tests index
    ("tests_README.md", "tests/README.md"),
    # Manual test checklists
    ("manual/character_arcs.md", "tests/manual/character_arcs.md"),
    ("manual/consistency.md", "tests/manual/consistency.md"),
    ("manual/motif_usage.md", "tests/manual/motif_usage.md"),
    ("manual/plot_completeness.md", "tests/manual/plot_completeness.md"),
    ("manual/style.md", "tests/manual/style.md"),
    ("manual/thematic_coherence.md", "tests/manual/thematic_coherence.md"),
    ("manual/absent_character.md", "tests/manual/absent_character.md"),
    ("manual/the_limit_ambiguity.md", "tests/manual/the_limit_ambiguity.md"),
    # src skeletons
    ("src/canon.md", "src/01-world/canon.md"),
    ("src/character_template.md", "src/02-characters/template.md"),
    # Project-local doc skeletons
    ("docs/authorial_intent.md", "docs/authorial_intent.md"),
    ("docs/craft_narrative.md", "docs/craft_narrative.md"),
    ("docs/experiment_lessons.md", "docs/experiment_lessons.md"),
    ("docs/decisions.log", "docs/decisions.log"),
]

# Canonical framework docs copied into projects (single source: framework docs/)
DOC_COPIES = [
    "AUTONOMOUS_RUN.md",
    "getting_started.md",
    "pipeline.md",
    "metric_interactions.md",
    "story_craft_criteria.md",
    "style_guide.md",
]


def copy_file(src: Path, dst: Path) -> None:
    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


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

    # Tools
    tools_dst = root / "tools"
    tools_dst.mkdir(parents=True, exist_ok=True)
    for f in TOOLS.glob("*.py"):
        shutil.copy2(f, tools_dst / f.name)

    # Template files
    missing = []
    for tmpl_rel, proj_rel in FILE_COPIES:
        src = TEMPLATES / tmpl_rel
        if src.exists():
            copy_file(src, root / proj_rel)
        else:
            missing.append(tmpl_rel)

    # Reference calibration corpus
    refs_src = TEMPLATES / "references"
    if refs_src.exists():
        for f in refs_src.glob("*"):
            shutil.copy2(f, root / "references" / f.name)

    # Canonical run docs
    for fname in DOC_COPIES:
        copy_file(DOCS / fname, root / "docs" / fname)

    # Ledger schemas
    analysis = root / "tests" / "analysis"
    for fname, content in LEDGER_SCHEMES.items():
        (analysis / fname).write_text(content, encoding="utf-8")

    # Story config — single source of truth (tools read book.yaml)
    book_yaml = f'title: "{title}"\nstatus: drafting\n'
    book_yaml += f'genre: {genre}\n'
    book_yaml += "target_word_count: 10000\nmax_word_count: 50000\n"
    book_yaml += "style: []\ntheme: []\nmotifs: []\nchapters: []\n"
    (root / "book.yaml").write_text(book_yaml, encoding="utf-8")

    # First chapter
    (root / "src" / "04-chapters" / "chapter_01.md").write_text(
        CHAPTER_TEMPLATE, encoding="utf-8")

    # Discovery buffer
    (root / "drafts" / "discovery_buffer.md").write_text(
        "# Discovery Buffer\n\n"
        "Things that appeared while writing and feel alive. Un-scored,\n"
        "no justification required.\n", encoding="utf-8")

    (root / "README.md").write_text(f"# {title}\n\nA {genre} story.\n", encoding="utf-8")

    # .gitignore
    (root / ".gitignore").write_text(
        "__pycache__/\n*.pyc\n.experiments/\noutput/\n", encoding="utf-8")

    # Init git
    import subprocess
    subprocess.run(["git", "init"], cwd=root, capture_output=True)
    subprocess.run(["git", "add", "-A"], cwd=root, capture_output=True)
    subprocess.run(["git", "commit", "-m", "init: scaffold from story-framework"],
                   cwd=root, capture_output=True)

    print(f"\nInitialized '{name}' ({genre})")
    print(f"  {len(DIRS)} directories, {len(FILE_COPIES)} template files")
    print(f"  Tool stack, boards, ledgers, rubric, reference corpus ready")
    if missing:
        print(f"  WARNING: missing framework templates: {', '.join(missing)}")
    print(f"\nNext steps:")
    print(f"  1. Fill in book.yaml (genre/theme/motifs) + docs/authorial_intent.md")
    print(f"  2. Write src/04-chapters/chapter_01.md; follow docs/AUTONOMOUS_RUN.md")
    print(f"  3. python tools/check_story.py")
    print(f"  4. Adapt personas in tests/redteam/personas.md (use persona_templates.md)")
    print(f"  5. Define council members in tests/council/ BEFORE first verdicts")


if __name__ == "__main__":
    main()
