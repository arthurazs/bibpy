import logging
from pathlib import Path
from bibpy.parser import parse_entry
logger = logging.getLogger(__name__)
def pub_date(input_path: "Path") -> None:
    entries = {}
    for file in input_path.iterdir():
        if file.name == "scienceDirect.bib":
            continue
        logger.info("Reading %s...", file)
        with file.open() as bib:
            entry = ""
            counter = 0
            for row in bib:
                counter += row.count("{")
                counter -= row.count("}")
                entry += row
                if counter == 0:
                    parsed_entry = parse_entry(entry)
                    try:
                        entries[parsed_entry.year] += 1
                    except KeyError:
                        entries[parsed_entry.year] = 1
                    entry = ""


    output_path = Path("data") / "pub_date.csv"
    logger.info("Saving to %s...", output_path)
    with output_path.open("w") as csv:
        csv.write("year,count\n")
        for year, count in sorted(entries.items()):
            csv.write(f"{year},{count}\n")
