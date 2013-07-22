import unicards


def test_As():
    unicards.colors = False
    card = unicards.unicard('As')
    assert card == u'\U0001f0a1', card


def test_unicards():
    unicards.colors = True
    out = []
    for suit in unicards.suits:
        for face in unicards.faces:
            out.append(unicards.unicard(face + suit))
    print(u' '.join(out))


def test_case_insensitivity():
    unicards.colors = False
    assert unicards.unicard('as') == u'\U0001f0a1'
    assert unicards.unicard('aS') == u'\U0001f0a1'


def test_ten():
    unicards.colors = False
    assert unicards.unicard('10c') == u'\U0001f0da'


if __name__ == '__main__':
    test_unicards()
