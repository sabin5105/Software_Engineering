def test_empty_string():
    assert pascalize('') == ''


def test_single_letter():
    assert pascalize('h') == 'H'


def test_single_word():
    assert pascalize('hey') == 'Hey'


def test_two_words():
    assert pascalize('hey_you') == 'HeyYou'

def test_three_words():
    assert pascalize('hey_you_there') == 'HeyYouThere'


def pascalize(s):
    if not s: 
        return s
    
    return ''.join(cap(s) for s in s.split('_'))

def cap(t):
    return t[0].upper() + t[1:]