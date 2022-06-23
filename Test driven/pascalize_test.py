from pascalize import pascalize

def test_empty_string():
    assert pascalize('') == ''


def test_single_letter():
    assert pascalize('h') == 'H'


def test_single_word():
    assert pascalize('hey') == 'Hey'

def test_multiple_words():
    assert pascalize('hey_there') == 'HeyThere'