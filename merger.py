from pathlib import Path
from parser import parse_entry

INPUT_PATH = Path("input")
INPUT_PATH.mkdir(exist_ok=True)

OUTPUT_PATH = Path("output")
OUTPUT_PATH.mkdir(exist_ok=True)

SCIENCE_DIRECT = "scienceDirect"



entries = {}
for file in (INPUT_PATH / SCIENCE_DIRECT).iterdir():
    with file.open() as bib:
        entry = ""
        counter = 0
        for row in bib:
            counter += row.count("{")
            counter -= row.count("}")
            entry += row
            if counter == 0:
                parsed_entry = parse_entry(entry)
                if parsed_entry.key + parsed_entry.issn not in entries:
                    entries[parsed_entry.key + parsed_entry.issn] = parsed_entry
                entry = ""
                counter = 0

with (OUTPUT_PATH / SCIENCE_DIRECT).with_suffix(".bib").open("w") as file:
    for entry in entries.values():
        file.write(str(entry))

