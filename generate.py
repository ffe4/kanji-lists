import json

from jinja2 import Template
from tomlkit import parse

with open("codegen/kanji_lists.json") as f:
    data = json.load(f)

with open("codegen/kanji_lists.jinja2") as f:
    template = Template(f.read())

with open("kanji_lists/kanji_lists.py", "w") as f:
    f.write(template.render(data=data, set=set))

with open("pyproject.toml") as f:
    doc = parse(f.read())
project_version = doc["tool"]["poetry"]["version"]

with open("codegen/__init__.jinja2") as f:
    template = Template(f.read())

with open("kanji_lists/__init__.py", "w") as f:
    f.write(template.render(data=data, version=project_version))
