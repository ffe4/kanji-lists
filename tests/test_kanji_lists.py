from kanji_lists import JOYO, KYOIKU, __version__
import pytest


def test_version():
    assert __version__ == "0.1.0"


def test_kyouiku_is_subset_of_joyo():
    assert KYOIKU.issubset(JOYO)


@pytest.mark.parametrize(
    "kanji_list,current_version",
    [
        (JOYO, JOYO.HEISEI22),
        (KYOIKU, KYOIKU.REIWA2),
        (KYOIKU.GRADE1, KYOIKU.REIWA2.GRADE1),
        (KYOIKU.GRADE2, KYOIKU.REIWA2.GRADE2),
        (KYOIKU.GRADE3, KYOIKU.REIWA2.GRADE3),
        (KYOIKU.GRADE4, KYOIKU.REIWA2.GRADE4),
        (KYOIKU.GRADE5, KYOIKU.REIWA2.GRADE5),
        (KYOIKU.GRADE6, KYOIKU.REIWA2.GRADE6),
    ],
)
def test_current_versions(kanji_list, current_version):
    assert kanji_list == current_version


joyo_kanji_test_data = {
    "HEISEI22": 2136,
    "SHOWA56": 1945,
}


@pytest.mark.parametrize("version", JOYO.version_list())
def test_number_of_joyo_kanji(version):
    joyo_list = getattr(JOYO, version)
    expected = joyo_kanji_test_data[version]
    assert len(joyo_list) == expected, (version, len(joyo_list))


@pytest.mark.parametrize(
    "version,grade,expected",
    [
        ("REIWA2", "GRADE1", 80),
        ("REIWA2", "GRADE2", 160),
        ("REIWA2", "GRADE3", 200),
        ("REIWA2", "GRADE4", 202),
        ("REIWA2", "GRADE5", 193),
        ("REIWA2", "GRADE6", 191),
        ("HEISEI4", "GRADE1", 80),
        ("HEISEI4", "GRADE2", 160),
        ("HEISEI4", "GRADE3", 200),
        ("HEISEI4", "GRADE4", 200),
        ("HEISEI4", "GRADE5", 185),
        ("HEISEI4", "GRADE6", 181),
    ],
)
def test_number_of_kyoiku_kanji(version, grade, expected):
    kyoiku_list = getattr(KYOIKU, version)
    grade_set = getattr(kyoiku_list, grade)
    assert len(grade_set) == expected


@pytest.mark.parametrize("version", KYOIKU.version_list())
def test_contains_each_character_exactly_once(version):
    kyoiku_list = getattr(KYOIKU, version)
    kanji_from_all_grades = [
        kanji for g in range(1, 7) for kanji in kyoiku_list.grade(g)
    ]
    assert set(kanji_from_all_grades) == kyoiku_list
    assert len(kanji_from_all_grades) == len(kyoiku_list)


@pytest.mark.parametrize(
    "old,new,grade,difference",
    [
        (
            "REIWA2",
            "HEISEI4",
            "GRADE4",
            "茨媛岡潟岐熊香佐埼崎滋鹿縄井沖栃奈梨阪阜賀群徳富城囲紀喜救型航告殺士史象賞貯停堂得毒費粉脈歴胃腸",
        ),
        ("REIWA2", "HEISEI4", "GRADE5", "囲紀喜救型航告殺士史象賞貯停堂得毒費粉脈歴恩券承舌銭退敵俵預賀群徳富",),
        ("REIWA2", "HEISEI4", "GRADE6", "胃腸恩券承舌銭退敵俵預城"),
    ],
)
def test_symmetric_difference_between_kyoiku_versions(new, old, grade, difference):
    old_list = getattr(KYOIKU, old)
    new_list = getattr(KYOIKU, new)
    old_grade = getattr(old_list, grade)
    new_grade = getattr(new_list, grade)
    assert old_grade ^ new_grade == set(difference)
