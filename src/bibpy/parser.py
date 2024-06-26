import logging
from bibpy.model import Entry, Element

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from io import TextIOBase

logger = logging.getLogger(__name__)


def next_element(text: str) -> "tuple[Element, str]":
    key, remainder = map(str.strip, text.split("=", 1))
    key = key.removeprefix(",").strip()
    if remainder[0] != "{":
        msg = "Element value does not start with {"
        raise ValueError(msg)
    counter = 0
    value = ""
    for index, char in enumerate(remainder):
        counter += char == "{"
        counter -= char == "}"
        value += char
        if counter == 0:
            remainder = remainder[index + 1:]
            break
    value = value.removeprefix("{").removesuffix("}")
    if remainder in ("\n}", ",}", "  }"):
        remainder = ""
    elif len(remainder.strip().rsplit("}", 1)[0]) < 1:  # scopus
        remainder = ""
    return Element(key=key.lower(), value=value), remainder

def parse_entry(text: str) -> "Entry":
    category, remainder = text.split("{", 1)
    category = category.strip().removeprefix("@")
    key, remainder = remainder.split("\n", 1)
    key = key.strip().removesuffix(",")

    elements = {}
    while remainder:
        element, remainder = next_element(remainder)
        elements[element.key] = element.value

    if remainder != "":
        msg = f"Expected empty remainder, got {remainder}"
        raise ValueError(msg)

    entry = Entry(category=category, key=key, issn=elements.pop("issn"))

    for key, value in elements.items():
        if key in ("year",):
            try:
                value = int(value)
            except ValueError:
                pass
        if key == "pmid":
            value = int(value)
        elif key in ("author", "editor"):
            value = tuple(map(str.strip, value.split("and")))
        elif key in ("author_keywords", "keywords"):
            comma = value.count(","), ","
            semicollon = value.count(";"), ";"
            value = tuple(map(str.strip, value.split(max(comma, semicollon)[1])))
        elif key in ("affiliations", "correspondence_address"):
            value = tuple(map(str.strip, value.split(";")))
        elif key == "type":
            key = "type2"
        setattr(entry, key, value)
    return entry

def load_entries(file: "TextIOBase") -> tuple[dict[str, "Entry"], int]:
    entries = {}
    entry_text = ""
    counter = 0
    duplicate = 0
    for row in file:
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
    return entries, duplicate
