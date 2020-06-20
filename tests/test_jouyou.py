from kanji_lists import Jouyou


def test_number_of_kanji():
    assert len(Jouyou()) == 2136
