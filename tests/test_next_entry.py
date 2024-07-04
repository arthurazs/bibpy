from io import StringIO
import pytest

from case_tests import ACM_STR, IEEE_STR, SCI_DIR_STR, SCOPUS_STR
from bibpy.parser import next_entry


TEST_DATA = (
    # case, expected_tell1, expected_tell2
    (ACM_STR, 621, 1131),
    (IEEE_STR, 357, 738),
    (SCI_DIR_STR, 542, 1112),
    (SCOPUS_STR, 1273, 2938),
)


def get_expected_entries(case: str) -> tuple[str, str, str]:
    entry1, entry2 = case.rsplit("@", 1)
    entry1, tmp = entry1.rsplit("}", 1)
    entry2 = tmp + "@" + entry2
    entry2, entry3 = entry2.rsplit("}", 1)

    return entry1 + "}", entry2 + "}", entry3


@pytest.mark.parametrize("case, expected_tell1, expected_tell2", TEST_DATA)
def test_next_entry(case: str, expected_tell1: int, expected_tell2: int) -> None:
    file = StringIO(case)
    expected_entry1, expected_entry2, expected_entry3 = get_expected_entries(case)

    entry = next_entry(file)
    assert entry.tell() == 0
    assert entry.read() == expected_entry1
    assert file.tell() == expected_tell1

    entry = next_entry(file)
    assert entry.tell() == 0
    assert entry.read() == expected_entry2
    assert file.tell() == expected_tell2

    entry = next_entry(file)
    assert entry.tell() == 0
    assert entry.read() == expected_entry3
    assert file.tell() == expected_tell2 + 1

    entry = next_entry(file)
    assert entry.tell() == 0
    assert entry.read() == ""
    assert file.tell() == expected_tell2 + 1


def test_last_entry() -> None:
    assert False, "how do I know if I've reached the end of the file?"
