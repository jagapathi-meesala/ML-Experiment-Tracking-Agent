from pathlib import Path
ROOT=Path(__file__).parents[1]
def test_explainability_headings():
    t=(ROOT/"EXPLAINABILITY.md").read_text()
    assert t.count("## Inputs and Data Sources")==1
    assert t.count("## Decision and Reasoning")==1
    assert t.count("## Limits and Constraints")==1
    assert "## Inputs\n" not in t and "## Decision\n" not in t and "## Limits\n" not in t

def test_skill_frontmatter():
    for p in (ROOT/"skills").glob("*/SKILL.md"):
        t=p.read_text(); assert t.startswith("---\n") and "\nname: " in t and "\ndescription: " in t
