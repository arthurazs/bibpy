
from model import Entry, Element

def next_element(text: str) -> "tuple[Element, str]":
    key, remainder = map(str.strip, text.split("=", 1))
    key = key.removeprefix(",\n")
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
    if remainder == "\n}":
        remainder = ""
    return Element(key=key, value=value), remainder

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
        msg = "Expected empty remainder, got %s" % remainder
        raise ValueError(msg)

    entry = Entry(category=category, key=key, issn=elements.pop("issn"))

    for key, value in elements.items():
        if key in ("year",):
            try:
                value = int(value)
            except ValueError:
                pass
        elif key in ("author", "editor"):
            value = tuple(map(str.strip, value.split("and")))
        elif key == "keywords":
            value = tuple(map(str.strip, value.split(",")))
        setattr(entry, key, value)
    return entry
