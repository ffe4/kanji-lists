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
        (KYOIKU.REIWA2.GRADE1, 80),
        (KYOIKU.REIWA2.GRADE2, 160),
        (KYOIKU.REIWA2.GRADE3, 200),
        (KYOIKU.REIWA2.GRADE4, 202),
        (KYOIKU.REIWA2.GRADE5, 193),
        (KYOIKU.REIWA2.GRADE6, 191),
        (KYOIKU.HEISEI4, 1006),
        (KYOIKU.HEISEI4.GRADE1, 80),
        (KYOIKU.HEISEI4.GRADE2, 160),
        (KYOIKU.HEISEI4.GRADE3, 200),
        (KYOIKU.HEISEI4.GRADE4, 200),
        (KYOIKU.HEISEI4.GRADE5, 185),
        (KYOIKU.HEISEI4.GRADE6, 181),
        (KYOIKU.SHOWA55, 996),
        (KYOIKU.SHOWA55.GRADE1, 76),
        (KYOIKU.SHOWA55.GRADE2, 145),
        (KYOIKU.SHOWA55.GRADE3, 195),
        (KYOIKU.SHOWA55.GRADE4, 195),
        (KYOIKU.SHOWA55.GRADE5, 195),
        (KYOIKU.SHOWA55.GRADE6, 190),
        (KYOIKU.SHOWA36, 881),
        (KYOIKU.SHOWA36.GRADE1, 46),
        (KYOIKU.SHOWA36.GRADE2, 105),
        (KYOIKU.SHOWA36.GRADE3, 187),
        (KYOIKU.SHOWA36.GRADE4, 205),
        (KYOIKU.SHOWA36.GRADE5, 194),
        (KYOIKU.SHOWA36.GRADE6, 144),
    ],
)
def test_number_of_kanji(kanji_list, expected):
    assert len(kanji_list) == expected


@pytest.mark.parametrize(
    "old,new,added,removed",
    [
        (
            KYOIKU.SHOWA36.GRADE1,
            KYOIKU.SHOWA55.GRADE1,
            set("年入糸夕村早力円校王虫町天千文男字犬空車気名見出立音百休林学"),
            set(),
        ),
        (
            KYOIKU.SHOWA36.GRADE2,
            KYOIKU.SHOWA55.GRADE2,
            set(
                "昼弟鳴交頭回止首毎近店野売買曜原算番科自午答茶歌妹理室広後親帰新絵魚場里通聞黄寺台電社当弱強食計太記同顔図点貝楽船引刀才体市形教画星遠晴語数"
            ),
            set("年入糸夕村早円力校王虫町天千文男字犬空車気名見立出音百休林学"),
        ),
        (
            KYOIKU.SHOWA36.GRADE3,
            KYOIKU.SHOWA55.GRADE3,
            set(
                "氷油植等緑鼻問路整式服商酒院列飲題帳泳予詩歯短育洋具薬館員他部港言福登祭童秒宮悲代調湖放写有章味習命軽対曲医農打守業庭反定血直幸州族横息係陽丁階拾転湯内線消"
            ),
            set(
                "昼弟鳴交頭回止首毎近店野売買曜原算番科自午答茶歌妹理室広後親帰新絵魚場里通聞黄寺台電社当弱強食計太記同顔図点貝楽船引刀才体市形教画星遠晴語数"
            ),
        ),
        (
            KYOIKU.SHOWA36.GRADE4,
            KYOIKU.SHOWA55.GRADE4,
            set(
                "功典管単毒宿賞折紀各説希念倉牧殺欠伝周救側求栄量億低辺敗養給腸兵筆候帯貯副漢氏例票標博浅象辞課議想型軍胃飯参健省浴央験灯令康区約倍要満完漁"
            ),
            set(
                "氷油植等緑鼻問路整式服商酒院列飲題帳泳予詩歯短育洋具薬館員他部港言福登祭童秒宮悲代調湖放写有章味習命軽対曲医燈農打守業庭反定血直幸州族横息係陽丁階拾転湯内線消"
            ),
        ),
        (
            KYOIKU.SHOWA36.GRADE5,
            KYOIKU.SHOWA55.GRADE5,
            set(
                "刊富預採資複罪態絹招徳善境除判述退略基故授損職潔妻舌逆営幹制程旧得未効衆犯評称墓財険減耕状券益検眼提豊災断構児条属版税禁率証歓額訓混再暴絶"
            ),
            set("功典管単毒宿賞折紀各説希念倉牧殺欠伝周救側求栄量億低辺敗養給腸兵筆候帯貯副漢氏例票標博浅象辞課議想型軍胃飯参健省浴央験令康区約倍要満完漁"),
        ),
        (
            KYOIKU.SHOWA36.GRADE6,
            KYOIKU.SHOWA55.GRADE6,
            set(
                "城源蒸批探傷閉幕操吸背層干射脳肺危簡片頂忘乳秘羊丸捨宅姿紅砂縮模署垂郷裁好針磁域寸翌笑巻劇仲段庁兆灰染樹腹座覧呼揮街困看泉沿障警割尺熟冊班枚俳郵糖晩胸宝幼潮亡値泣担矢窓径裏訪宙優穴卵机閣鋼痛洗誌棒降宇臓若将乱筋羽縦弓密映奏刻骨暖朗"
            ),
            set(
                "刊富預採資複罪絹招態徳善境除判述退略基故授損職潔妻舌逆営幹制程旧得未効衆犯評称墓財険減耕状券益検眼提豊災断構児条属版税禁率証歓額訓混再暴絶"
            ),
        ),
        (KYOIKU.SHOWA55.GRADE1, KYOIKU.HEISEI4.GRADE1, set("貝竹草玉"), set()),
        (
            KYOIKU.SHOWA55.GRADE2,
            KYOIKU.HEISEI4.GRADE2,
            set("週細直言弓万園線岩活矢羽姉肉公兄丸角内"),
            set("貝竹草玉"),
        ),
        (
            KYOIKU.SHOWA55.GRADE3,
            KYOIKU.HEISEI4.GRADE3,
            set("笛談漢速皿委央練想羊真区相倍宿昔豆筆箱"),
            set("公週兄線角細直万肉園岩内言活"),
        ),
        (
            KYOIKU.SHOWA55.GRADE4,
            KYOIKU.HEISEI4.GRADE4,
            set("街束特笑訓得果札径児好梅巣仲祝松無泣兆未"),
            set("委勢区央相練倍想談姉漢真速筆宿"),
        ),
        (
            KYOIKU.SHOWA55.GRADE5,
            KYOIKU.HEISEI4.GRADE5,
            set("飼勢可桜夢枝"),
            set("祝無絹収善特児歓衆称蚕未訓除得果"),
        ),
        (
            KYOIKU.SHOWA55.GRADE6,
            KYOIKU.HEISEI4.GRADE6,
            set("絹収善並衆蚕誕除激装盛暮"),
            set("街弐笑壱釈可兼径好弓是羊俗仲矢泣羽需勧兆丸"),
        ),
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
        (KYOIKU, {"REIWA2", "HEISEI4", "SHOWA55", "SHOWA36"}),
    ],
)
def test_version_lists(kanji_list, expected):
    result = kanji_list.version_list()
    assert set(result) == expected


def test_kyoiku_is_subset_of_joyo():
    assert KYOIKU.issubset(JOYO)
