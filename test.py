import unicards


def test_As():
    card = unicards.unicard('As')
    assert card == u'\U0001f0a1', card


def test_color():
    card = unicards.unicard('As', color=True)
    assert card == u'\x1b[30m\U0001f0a1\x1b[39m', repr(card)

def test_unicards():
    out = []
    for suit in unicards.SUITS[0]:
        for face in unicards.FACES[0]:
            out.append(unicards.unicard(face + suit, color=True))
    print(u' '.join(out))


def test_case_insensitivity():
    assert unicards.unicard('as') == u'\U0001f0a1'
    assert unicards.unicard('aS') == u'\U0001f0a1'


def test_ten():
    assert unicards.unicard('10c') == u'\U0001f0da'


if __name__ == '__main__':
    test_unicards()
