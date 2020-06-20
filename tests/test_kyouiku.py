import pytest

from kanji_lists import Kyouiku


@pytest.mark.parametrize(
    "version,grade,expected",
    [
        (None, "GRADE1", 80),
        (None, "GRADE2", 160),
        (None, "GRADE3", 200),
        (None, "GRADE4", 202),
        (None, "GRADE5", 193),
        (None, "GRADE6", 191),
        (Kyouiku.Version.REIWA2, "GRADE1", 80),
        (Kyouiku.Version.REIWA2, "GRADE2", 160),
        (Kyouiku.Version.REIWA2, "GRADE3", 200),
        (Kyouiku.Version.REIWA2, "GRADE4", 202),
        (Kyouiku.Version.REIWA2, "GRADE5", 193),
        (Kyouiku.Version.REIWA2, "GRADE6", 191),
        (Kyouiku.Version.HEISEI4, "GRADE1", 80),
        (Kyouiku.Version.HEISEI4, "GRADE2", 160),
        (Kyouiku.Version.HEISEI4, "GRADE3", 200),
        (Kyouiku.Version.HEISEI4, "GRADE4", 200),
        (Kyouiku.Version.HEISEI4, "GRADE5", 185),
        (Kyouiku.Version.HEISEI4, "GRADE6", 181),
    ],
)
def test_number_of_kanji(version, grade, expected):
    kyouiku_list = Kyouiku(version) if version else Kyouiku()
    grade_set = getattr(kyouiku_list, grade)
    assert len(grade_set) == expected


@pytest.mark.parametrize("version", Kyouiku.Version.__members__.values())
def test_no_duplicate_characters_in_grades(version):
    kyouiku_list = Kyouiku(version)
    kanji_from_all_grades = []
    for grade in range(1, 7):
        grade_set = getattr(kyouiku_list, f"GRADE{str(grade)}")
        kanji_from_all_grades.extend(grade_set)
    assert set(kanji_from_all_grades) == kyouiku_list
    assert len(kanji_from_all_grades) == len(kyouiku_list)


@pytest.mark.parametrize(
    "old,new,grade,difference",
    [
        (
            Kyouiku.Version.REIWA2,
            Kyouiku.Version.HEISEI4,
            "GRADE4",
            "茨媛岡潟岐熊香佐埼崎滋鹿縄井沖栃奈梨阪阜賀群徳富城囲紀喜救型航告殺士史象賞貯停堂得毒費粉脈歴胃腸",
        ),
        (
            Kyouiku.Version.REIWA2,
            Kyouiku.Version.HEISEI4,
            "GRADE5",
            "囲紀喜救型航告殺士史象賞貯停堂得毒費粉脈歴恩券承舌銭退敵俵預賀群徳富",
        ),
        (Kyouiku.Version.REIWA2, Kyouiku.Version.HEISEI4, "GRADE6", "胃腸恩券承舌銭退敵俵預城"),
    ],
)
def test_symmetric_difference_between_versions(new, old, grade, difference):
    old_list = Kyouiku(old)
    new_list = Kyouiku(new)
    old_grade = getattr(old_list, grade)
    new_grade = getattr(new_list, grade)
    assert old_grade ^ new_grade == set(difference)
