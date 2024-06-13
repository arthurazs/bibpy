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
    volume: str | None = None
    year: int | None = None
    number: str | None = None
    author: tuple[str] | None = None
    keywords: tuple[str] | None = None
    editor: tuple[str] | None = None

    @property
    def code(self: "Entry") -> str:
        return self.key + self.issn

    @staticmethod
    def parse_value(key: str, value: str) -> str | int | tuple[str, ...]:
        if key in ("author", "editor"):
            return tuple(map(str.strip, value.split(" and ")))
        if key in ("keywords", ):
            return tuple(map(str.strip, value.split(",")))
        if key in ("year", ):
            return int(value)
        return value

    @staticmethod
    def value2string(key: str, value: str | tuple[str, ...] | int) -> str:
        if key in ("author", "editor"):
            return " and ".join(value)  # type: ignore[arg-type]
        if key in ("keywords", ):
            return ", ".join(value)  # type: ignore[arg-type]
        if key in ("year", ):
            return str(value)
        return value  # type: ignore[return-value]

    def __str__(self: "Entry") -> str:
        entry = "@%s{%s,\n" % (self.category, self.key)  # noqa: UP031
        for attr in (  # I could have used `dir`, but I want to order the output
            "title",
            "year",
            "author",
            "journal",
            "doi",
            "issn",
            "abstract",
            "url",
            "pages",
            "note",
            "series",
            "publisher",
            "volume",
            "number",
            "keywords",
            "editor",
        ):
            value = getattr(self, attr)
            if value is None:
                continue
            entry += attr + " = {%s},\n" % self.value2string(attr, value)  # noqa: UP031
        entry = entry.removesuffix(",\n")
        return entry + "\n}\n"

@dataclass(kw_only=True, slots=True, frozen=True)
class Element:
    key: str
    value: str

