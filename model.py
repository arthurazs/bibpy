
from dataclasses import dataclass
@dataclass(slots=True)
class Entry:
    category: str
    key: str
    issn: str
    title: str | None = None
    journal: str | None = None
    pages: str | None = None
    doi: str | None = None
    url: str | None = None
    note: str | None = None
    series: str | None = None
    publisher: str | None = None
    abstract: str | None = None
    volume: int | str | None = None
    year: int | None = None
    number: int | None = None
    author: list[str] | None = None
    keywords: list[str] | None = None
    editor: list[str] | None = None

    def __str__(self: "Entry") -> str:
        entry = "@%s{%s,\n" % (self.category, self.key)
        entry += "issn = {%s},\n" % (self.issn)
        for attr in dir(self):
            if attr[:2] == "__":
                continue
            if attr in ("category", "key", "issn"):
                continue
            
            value = getattr(self, attr)
            if value is None:
                continue

            if attr in ("author", "editor"):
                entry += attr + " = {" + " and ".join(value) + "},\n"
            elif attr == "keywords":
                value = attr + " = {" + ", ".join(value) + "},\n"
            else:
                entry += attr + " = {%s},\n" % value
        entry = entry.removesuffix(",\n")
        return entry + "\n}\n"

@dataclass(kw_only=True, slots=True, frozen=True)
class Element:
    key: str
    value: str

def parse_element(element: str) -> "Element":
    key, value = map(str.strip, element.split("=", 1))
    return Element(key=key, value=value)
