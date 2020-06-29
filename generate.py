import json

from jinja2 import Template

with open("codegen/kanji_lists.json") as f:
    data = json.load(f)['lists']

with open("codegen/kanji_lists.jinja2") as f:
    template = Template(f.read())

with open("kanji_lists/kanji_lists.py", "w") as f:
    f.write(template.render(data=data, set=set))
