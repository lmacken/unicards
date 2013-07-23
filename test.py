# Copyright 2013 Luke Macken <lmacken@redhat.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unicards


def test_As():
    card = unicards.unicard('As')
    assert card == u'\U0001f0a1', card


def test_color():
    card = unicards.unicard('As', color=True)
    assert card == u'\x1b[30m\U0001f0a1\x1b[39m', repr(card)


def test_unicards():
    for suit in unicards.SUITS:
        print('')
        out = []
        for face in unicards.FACES:
            out.append(unicards.unicard(face + suit, color=True))
        print(u' '.join(out))
    print('')


def test_case_insensitivity():
    assert unicards.unicard('as') == u'\U0001f0a1'
    assert unicards.unicard('aS') == u'\U0001f0a1'


def test_ten():
    assert unicards.unicard('10c') == u'\U0001f0da'


if __name__ == '__main__':
    test_unicards()
