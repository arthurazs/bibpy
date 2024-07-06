import io
import logging
import os

from bibpy.model import Entry

logger = logging.getLogger(__name__)


def get_category(entry: "io.TextIOWrapper") -> str:
    category = ""
    found_at = False  # looking for @ symbol
    while True:
        char = entry.read(1)
        if char == "":
            break

        if not found_at:
            found_at = char == "@"
            continue

        if char == "{":
            break

        category += char
    return category.lower()


def get_key(entry: "io.TextIOWrapper") -> str:
    key = ""
    while True:
        char = entry.read(1)

        if char in ("", ","):
            break

        key += char
    return key


def get_element_key(entry: "io.TextIOWrapper") -> str:
    key = ""
    while True:
        char = entry.read(1)

        if char in ("", "="):
            break

        key += char
    return key.removeprefix(",").strip().lower()


def get_element_value(entry: "io.TextIOWrapper") -> str:
    value = ""
    started = False
    counter = 0
    while True:
        char = entry.read(1)
        if char == "":
            break

        if not started:
            if char == "{":
                started = True
                counter += 1
            continue

        counter += char == "{"
        counter -= char == "}"
        if started and counter == 0:
            break

        value += char
    return value


def get_next_element(entry: "io.TextIOWrapper") -> tuple[str, str]:
    return get_element_key(entry), get_element_value(entry)


def parse_entry(entry: "io.TextIOWrapper") -> "Entry":
    category = get_category(entry)
    key = get_key(entry)
    # element_key, element_value = get_next_element(entry)
    return Entry(category=category, key=key)


def next_entry(bib: "io.TextIOWrapper") -> "io.StringIO":
    entry = io.StringIO()
    counter = 0
    started = False
    end = False

    while not end:
        char = bib.read(1)
        entry.write(char)

        is_empty = char == ""
        is_open = char == "{"
        if not started:
            started = is_open

        counter += is_open
        counter -= char == "}"

        end = is_empty or (started and counter == 0)

    entry.seek(0, os.SEEK_SET)  # rewind to the start of the stream
    return entry


def is_empty(buffer: "io.TextIOWrapper") -> bool:
    cookie = buffer.tell()
    buffer.seek(0, os.SEEK_END)
    empty = cookie == buffer.tell()
    buffer.seek(cookie, os.SEEK_SET)
    return empty

