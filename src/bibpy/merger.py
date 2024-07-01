import logging
from pathlib import Path
from bibpy.parser import parse_entry


logger = logging.getLogger(__name__)

def merge(input_path: "Path", output_path: "Path") -> None:
    for folder in input_path.iterdir():
        logger.info("Entering %s...", folder)
        entries = {}
        issn_counter = 0
        for file in folder.iterdir():
            logger.info("Parsing %s...", file)
            with file.open() as bib:
                entry = ""
                counter = 0
                tmp = ""
                for row in bib:
                    if row == "\n":
                        continue
                    if tmp:
                        row = tmp + row
                    if "}@" in row:  # tmp for IEEE
                        row, tmp = row.split("}@")
                        row = row[:-1] + "\n}"
                        tmp = "@" + tmp
                    else:
                        tmp = ""
                    counter += row.count("{")
                    counter -= row.count("}")
                    entry += row
                    if counter == 0:
                        try:
                            parsed_entry = parse_entry(entry)
                        except AttributeError as e:
                            missing_attribute = e.args[0].split("'")[-2]
                            msg = 'Attribute "%s" not found in "%s"' % (missing_attribute, file)
                            logger.error(entry)
                            logger.error(msg)
                            exit(1)
                        except KeyError as e:
                            missing_key = e.args[0]
                            if missing_key == "issn":
                                issn_counter += 1
                                head, tail = entry.split("\n", 1)
                                entry = head + ("\nissn = {not-found-%s},\n" % issn_counter) + tail
                                parsed_entry = parse_entry(entry)
                            else:
                                msg = 'Key "%s" not found in "%s"' % (missing_key, file)
                                logger.critical(entry)
                                logger.error(msg)
                                exit(2)
                        if parsed_entry.key + parsed_entry.issn not in entries:
                            entries[parsed_entry.key + parsed_entry.issn] = parsed_entry
                        else:
                            current = parsed_entry
                            previous = entries[parsed_entry.key + parsed_entry.issn]
                            logger.debug("Duplicated entry\n\nCurrent\n%s\n\nPrevious\n%s", current, previous)
                        entry = ""
                        counter = 0

        logger.info("Merging %d entries to %s...", len(entries), folder.name)
        with (output_path / folder.name).with_suffix(".bib").open("w") as file:
            for entry in entries.values():
                file.write(str(entry))
