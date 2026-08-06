from pathlib import Path

from model import Artifact


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "book" / "docs" / "generated"

def destination(artifact: Artifact) -> Path:

    if artifact.type == "constitution":
        return OUTPUT / "constitution" / f"{artifact.id}.md"

    if artifact.type == "glossary":
        return OUTPUT / "glossary" / f"{artifact.id}.md"

    return (
        OUTPUT
        / "specifications"
        / artifact.type
        / f"{artifact.id}.md"
    )

def render_markdown(artifact: Artifact) -> str:

    title = artifact.id

    if artifact.title:
        title += f" — {artifact.title}"

    return (
        "---\n"
        f"title: {title}\n"
        "---\n\n"
        + artifact.content
    )

def write_artifact(artifact: Artifact):

    output = destination(artifact)

    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output.write_text(
        render_markdown(artifact),
        encoding="utf-8",
    )

def write_all(model):

    if OUTPUT.exists():
        import shutil
        shutil.rmtree(OUTPUT)

    OUTPUT.mkdir(
        parents=True,
        exist_ok=True,
    )

    for artifact in model.repository.all():
        write_artifact(artifact)


