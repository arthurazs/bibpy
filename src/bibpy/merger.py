from typing import TYPE_CHECKING

from bibpy.parser import parse_entry

if TYPE_CHECKING:
    from pathlib import Path

def merge(input_path: "Path", output_file: "Path") -> None:
    entries = {}
    for input_file in input_path.iterdir():
        with input_file.open() as bib:
            entry_text = ""
            counter = 0
            for row in bib:
                counter += row.count("{")
                counter -= row.count("}")
                entry_text += row
                if counter == 0:
                    parsed_entry = parse_entry(entry_text)
                    if parsed_entry.key + parsed_entry.issn not in entries:
                        entries[parsed_entry.key + parsed_entry.issn] = parsed_entry
                    entry_text = ""
                    counter = 0

    with output_file.open("w") as file:
        for entry in entries.values():
            file.write(str(entry))

