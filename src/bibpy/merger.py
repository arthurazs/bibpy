import logging
from typing import TYPE_CHECKING

from bibpy.parser import parse_entry

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)


def merge(input_path: "Path", output_file: "Path") -> None:
    # TODO @arthurazs: use load_entries
    entries = {}
    duplicate = 0
    logger.info("Iterating over %s...", input_path)
    for input_file in input_path.iterdir():
        logger.info("Parsing %s...", input_file.name)
        with input_file.open() as bib:
            entry_text = ""
            counter = 0
            for row in bib:
                counter += row.count("{")
                counter -= row.count("}")
                entry_text += row
                if counter == 0:
                    entry = parse_entry(entry_text)
                    if entry.code not in entries:
                        entries[entry.code] = entry
                    else:
                        duplicate += 1
                        logger.debug("Duplicate entry found: %s", entry.code)
                        previous = entries[entry.code]
                        current = entry
                        if previous != current:
                            logger.error("Duplicate entry differs\nPrevious\n%s\n\nCurrent\n%s", previous, current)
                    entry_text = ""
                    counter = 0
    logger.info("Found %d duplicate entries", duplicate)
    logger.info("Found %d unique entries", len(entries))

    logger.info("Saving entries to %s", output_file)
    with output_file.open("w") as file:
        for entry in entries.values():
            file.write(str(entry))

