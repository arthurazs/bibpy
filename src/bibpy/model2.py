from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from io import StringIO

@dataclass
class Entry:
    author: tuple[str, ...]
    journal: str
    title: str
    year: int
    volume: int
    number: int
    pages: str
    doi: str
    issn: str
    month: str


def next_entry(bib: "StringIO") -> str:
    entry = char = ""
    counter = 0
    started = False
    end = False

    while not end:
        char = bib.read(1)
        entry += char

        is_empty = char == ""
        is_open = char == "{"
        if not started:
            started = is_open

        counter += is_open
        counter -= char == "}"
        
        end = is_empty or (started and counter == 0)

    return entry
