from pathlib import Path
import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

root = Path(__file__).parent.parent
pipelines_root = root / "ir-pipelines"

SKIP_DIRS = {"tests", "test", "__pycache__"}
PIPELINE_LABELS = {
    "ir-pell-accepts": "Pell Accepts",
    "ir-team-exercise": "Team Exercise",
    "ir-enrollment-projection": "Enrollment Projection"
 }

for pipeline in sorted(pipelines_root.iterdir()):
    if not pipeline.is_dir():
        continue
    
    pipeline_label = PIPELINE_LABELS.get(pipeline.name, pipeline.name)
    src = pipeline / "src"
    if not src.exists():
        continue

    # Find the top package folder under src (e.g., ir_pell_accepts)
    # pkgs = [p for p in src.iterdir() if p.is_dir() and (p / "__init__.py").exists()]
    # if not pkgs:
    #     continue
    # pkg = pkgs[0]  # if you have multiple, we can expand this later

    for path in sorted(src.rglob("*.py")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue

        module_path = path.relative_to(src).with_suffix("")          # ir_pell_accepts/foo
        doc_path = path.relative_to(src).with_suffix(".md")          # ir_pell_accepts/foo.md

        # Put everything under docs/pipelines/<pipeline>/reference/...
        full_doc_path = Path("ir-pipelines", pipeline.name, "reference", doc_path)

        parts = tuple(module_path.parts)

        # skip __main__.py modules
        if parts[-1] == "__main__":
            continue

        is_pkg_index = (parts[-1] == "__init__")

        # Treat package __init__.py as an index page
        if is_pkg_index:
            parts = parts[:-1]
            full_doc_path = full_doc_path.with_name("index.md")

        # NAV: drop the top-level package folder (e.g., "ir_pell_accepts")
        parts_for_nav = parts[1:] if len(parts) > 1 else parts

        # If this is the package index page, don't include it in nav
        # (prevents "ir_pell_accepts" showing as a bullet under Pell Accepts)
        if not is_pkg_index:
            nav[(pipeline_label,) + parts_for_nav] = full_doc_path.as_posix()

        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            ident = ".".join(parts)  # keep full identifier for mkdocstrings
            fd.write(f"::: {ident}\n")

        mkdocs_gen_files.set_edit_path(full_doc_path, path.relative_to(root))

# Root SUMMARY.md for the portal
with mkdocs_gen_files.open("SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
