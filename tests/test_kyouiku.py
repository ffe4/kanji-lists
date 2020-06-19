import pytest

from kanji_lists import Kyouiku


@pytest.mark.parametrize('grade,expected', [
    ('GRADE1', 80),
    ('GRADE2', 160),
    ('GRADE3', 200),
    ('GRADE4', 202),
    ('GRADE5', 193),
    ('GRADE6', 191)
])
def test_number_of_kanji(grade, expected):
    grade_set = getattr(Kyouiku(), grade)
    assert len(grade_set) == expected
