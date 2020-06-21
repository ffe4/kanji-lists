from kanji_lists import JOYO, KYOIKU, JINMEIYO, __version__
import pytest


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.parametrize(
    "kanji_list,current_version",
    [
        (JOYO, JOYO.HEISEI22),
        (JINMEIYO, JINMEIYO.HEISEI29),
        (KYOIKU, KYOIKU.REIWA2),
        (KYOIKU.GRADE1, KYOIKU.REIWA2.GRADE1),
        (KYOIKU.GRADE2, KYOIKU.REIWA2.GRADE2),
        (KYOIKU.GRADE3, KYOIKU.REIWA2.GRADE3),
        (KYOIKU.GRADE4, KYOIKU.REIWA2.GRADE4),
        (KYOIKU.GRADE5, KYOIKU.REIWA2.GRADE5),
        (KYOIKU.GRADE6, KYOIKU.REIWA2.GRADE6),
    ],
)
def test_current_version_is_correct(kanji_list, current_version):
    assert kanji_list == current_version


@pytest.mark.parametrize(
    "kanji_list,expected",
    [
        (JOYO, 2136),
        (KYOIKU, 1026),
        (JINMEIYO, 863),
        (JOYO.HEISEI22, 2136),
        (JOYO.SHOWA56, 1945),
        (JINMEIYO.HEISEI29, 863),
        (JINMEIYO.HEISEI27, 862),
        (JINMEIYO.HEISEI25, 861),
        (KYOIKU.REIWA2, 1026),
        (KYOIKU.HEISEI4, 1006),
        (KYOIKU.REIWA2.GRADE1, 80),
        (KYOIKU.REIWA2.GRADE2, 160),
        (KYOIKU.REIWA2.GRADE3, 200),
        (KYOIKU.REIWA2.GRADE4, 202),
        (KYOIKU.REIWA2.GRADE5, 193),
        (KYOIKU.REIWA2.GRADE6, 191),
        (KYOIKU.HEISEI4.GRADE1, 80),
        (KYOIKU.HEISEI4.GRADE2, 160),
        (KYOIKU.HEISEI4.GRADE3, 200),
        (KYOIKU.HEISEI4.GRADE4, 200),
        (KYOIKU.HEISEI4.GRADE5, 185),
        (KYOIKU.HEISEI4.GRADE6, 181),
    ],
)
def test_number_of_kanji(kanji_list, expected):
    assert len(kanji_list) == expected


@pytest.mark.parametrize(
    "old,new,added,removed",
    [
        (KYOIKU.HEISEI4.GRADE1, KYOIKU.REIWA2.GRADE1, set(), set()),
        (KYOIKU.HEISEI4.GRADE2, KYOIKU.REIWA2.GRADE2, set(), set()),
        (KYOIKU.HEISEI4.GRADE3, KYOIKU.REIWA2.GRADE3, set(), set()),
        (
            KYOIKU.HEISEI4.GRADE4,
            KYOIKU.REIWA2.GRADE4,
            set("城賀群徳富茨媛岡潟岐熊香佐埼崎滋鹿縄井沖栃奈梨阪阜"),
            set("囲紀喜救型航告殺士史象賞貯停堂得毒費粉脈歴胃腸"),
        ),
        (
            KYOIKU.HEISEI4.GRADE5,
            KYOIKU.REIWA2.GRADE5,
            set("囲紀喜救型航告殺士史象賞貯停堂得毒費粉脈歴"),
            set("賀群徳富恩券承舌銭退敵俵預"),
        ),
        (KYOIKU.HEISEI4.GRADE6, KYOIKU.REIWA2.GRADE6, set("胃腸恩券承舌銭退敵俵預"), set("城")),
        (
            JOYO.SHOWA56,
            JOYO.HEISEI22,
            set(
                "旦曖柵湧踪戴脊妖憬詣亀苛弄栃柿貌叱謎葛餌熊錦璧傲凄璃溺鍋瓦睦闇賭臼彙捉芯桁諧捻籠瘍蔽鎌瞳采蔑尻呂藍餅嗅頃丼窟韓麓恣那塞袖嵐萎咽挫頬爽畏鹿箋虹汎巾伎捗憧腺楷貪拭塡顎綻旺貼痩乞稽摯瞭奈媛艶拳昧醒鬱賂僅肘嘲梨訃遜舷瑠蜜岡腫膝拉腎埼慄淫詮挨羞眉駒唄戚俺麺蹴裾椅惧冶毀梗罵蓋枕呪勃剝汰錮鍵阜狙哺蜂唾弥緻串股氾嫉妬玩辣虎沙箸爪膳脇拶斬隙喩沃崖喉堆藤酎遡曽匂潰椎痕羨刹宛誰畿阪臆鶴骸釜茨須牙怨勾冥頓斑諦侶煎"
            ),
            set("勺銑脹錘匁"),
        ),
        (JINMEIYO.HEISEI25, JINMEIYO.HEISEI27, set("巫"), set()),
        (JINMEIYO.HEISEI27, JINMEIYO.HEISEI29, set("渾"), set()),
    ],
)
def test_changes_between_consecutive_versions(old, new, added, removed):
    assert old - new == removed
    assert new - old == added


@pytest.mark.parametrize(
    "kanji_list,expected",
    [
        (JOYO, {"HEISEI22", "SHOWA56"}),
        (JINMEIYO, {"HEISEI29", "HEISEI27", "HEISEI25"}),
        (KYOIKU, {"REIWA2", "HEISEI4"}),
    ],
)
def test_version_lists(kanji_list, expected):
    result = kanji_list.version_list()
    assert set(result) == expected


def test_kyoiku_is_subset_of_joyo():
    assert KYOIKU.issubset(JOYO)
