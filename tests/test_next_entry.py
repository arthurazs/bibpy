from io import StringIO

from case_tests import ACM_STR, IEEE_STR, SCI_DIR_STR, SCOPUS_STR
from bibpy.model2 import next_entry


ACM_FILE = StringIO(ACM_STR)
IEEE_FILE = StringIO(IEEE_STR)
SCI_DIR_FILE = StringIO(SCI_DIR_STR)
SCOPUS_FILE = StringIO(SCOPUS_STR)


def get_expected_entries(case: str) -> tuple[str, str, str]:
    entry1, entry2 = case.rsplit("@", 1)
    entry1, tmp = entry1.rsplit("}", 1)
    entry2 = tmp + "@" + entry2
    entry2, entry3 = entry2.rsplit("}", 1)

    return entry1 + "}", entry2 + "}", entry3


def test_ieee_next_entry() -> None:
    expected_entry1, expected_entry2, expected_entry3 = get_expected_entries(IEEE_STR)

    entry = next_entry(IEEE_FILE)
    assert entry == expected_entry1
    assert IEEE_FILE.tell() == 357

    entry = next_entry(IEEE_FILE)
    assert entry == expected_entry2
    assert IEEE_FILE.tell() == 738

    entry = next_entry(IEEE_FILE)
    assert entry == expected_entry3
    assert IEEE_FILE.tell() == 739

    entry = next_entry(IEEE_FILE)
    assert entry == ""
    assert IEEE_FILE.tell() == 739


def test_acm_next_entry() -> None:
    expected_entry1, expected_entry2, expected_entry3 = get_expected_entries(ACM_STR)

    entry = next_entry(ACM_FILE)
    assert entry == expected_entry1
    assert ACM_FILE.tell() == 621

    entry = next_entry(ACM_FILE)
    assert entry == expected_entry2
    assert ACM_FILE.tell() == 1131

    entry = next_entry(ACM_FILE)
    assert entry == expected_entry3
    assert ACM_FILE.tell() == 1132

    entry = next_entry(ACM_FILE)
    assert entry == ""
    assert ACM_FILE.tell() == 1132


def test_acm_next_entry() -> None:
    expected_entry1, expected_entry2, expected_entry3 = get_expected_entries(ACM_STR)

    entry = next_entry(ACM_FILE)
    assert entry == expected_entry1
    assert ACM_FILE.tell() == 621

    entry = next_entry(ACM_FILE)
    assert entry == expected_entry2
    assert ACM_FILE.tell() == 1131

    entry = next_entry(ACM_FILE)
    assert entry == expected_entry3
    assert ACM_FILE.tell() == 1132

    entry = next_entry(ACM_FILE)
    assert entry == ""
    assert ACM_FILE.tell() == 1132


def test_science_direct_next_entry() -> None:
    expected_entry1, expected_entry2, expected_entry3 = get_expected_entries(SCI_DIR_STR)

    entry = next_entry(SCI_DIR_FILE)
    assert entry == expected_entry1
    assert SCI_DIR_FILE.tell() == 552

    entry = next_entry(SCI_DIR_FILE)
    assert entry == expected_entry2
    assert SCI_DIR_FILE.tell() == 1140

    entry = next_entry(SCI_DIR_FILE)
    assert entry == expected_entry3
    assert SCI_DIR_FILE.tell() == 1141

    entry = next_entry(SCI_DIR_FILE)
    assert entry == ""
    assert SCI_DIR_FILE.tell() == 1141


def test_scopus_next_entry() -> None:
    expected_entry1, expected_entry2, expected_entry3 = get_expected_entries(SCOPUS_STR)

    entry = next_entry(SCOPUS_FILE)
    assert entry == expected_entry1
    assert SCOPUS_FILE.tell() == 1283

    entry = next_entry(SCOPUS_FILE)
    assert entry == expected_entry2
    assert SCOPUS_FILE.tell() == 2962

    entry = next_entry(SCOPUS_FILE)
    assert entry == expected_entry3
    assert SCOPUS_FILE.tell() == 2963

    entry = next_entry(SCOPUS_FILE)
    assert entry == ""
    assert SCOPUS_FILE.tell() == 2963

