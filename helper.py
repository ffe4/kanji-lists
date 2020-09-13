import argparse
import json
import subprocess

from jinja2 import Template
import toml
import black


# Template and target file locations of files that need to be generated
CODEGEN_FILES = [
    ("codegen/kanji_lists.jinja2", "kanji_lists/kanji_lists.py"),
    ("codegen/__init__.jinja2", "kanji_lists/__init__.py"),
    ("codegen/README.jinja2", "README.rst"),
]


def load_render_data() -> dict:
    with open("codegen/kanji_lists.json") as f:
        data = json.load(f)
    with open("pyproject.toml") as f:
        doc = toml.load(f)
    project_version = doc["tool"]["poetry"]["version"]
    return dict(
        set=set,
        data=data,
        version=project_version,
    )


def run(check_only):
    print("Running Code Generation")
    render_parameters = load_render_data()
    needs_formatting = False
    for file in CODEGEN_FILES:
        template, target = file
        with open(template, "r") as src:
            template = Template(src.read())
        output = template.render(**render_parameters)
        if check_only:
            with open(target, "r") as src:
                current_version = src.read()
            if current_version != output:
                needs_formatting = 1
                print(f"✗ {target}")
            else:
                print(f"✓ {target}")
        else:
            with open(target, "w+") as out:
                print(f"✓ {target}")
                out.write(output)
    if needs_formatting:
        print(
            "Some files are not correctly generated. "
            "Please run without --check-only to re-generate source files"
        )

    print("\nRunning Black Formatter")
    cmd = ["black", "."]
    if check_only:
        cmd.append("--check")
    black_exit_code = subprocess.call(cmd)

    if black_exit_code != 0 or needs_formatting:
        exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Helper script for code generation and linting"
    )
    parser.add_argument(
        "--check-only",
        default=False,
        action="store_true",
        help="do not write changes to disk",
    )
    args = parser.parse_args()
    run(args.check_only)
