from dataclasses import dataclass


@dataclass
class Entry:
    category: str
    key: str
    author: tuple[str, ...] | None = None
    journal: str | None = None
    title: str | None = None
    year: int | None = None
    volume: int | None = None
    number: int | None = None
    pages: str | None = None
    doi: str | None = None
    issn: str | None = None
    month: str | None = None
