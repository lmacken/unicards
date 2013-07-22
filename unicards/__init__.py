# unicards is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# unicards is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with unicards.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2013 Luke Macken <lmacken@redhat.com>
"""
Converts strings into unicode playing cards
"""

FACES = 'A23456789TJCQK', '123456789ABCDE'
SUITS = 'SHDC', 'ABCD'
RED, BLACK, RESET = '\x1b[31m', '\x1b[30m', '\x1b[39m'


def unicard(card, color=False):
    if card[:2] == '10':
        card = 'T' + card[2]
    face, suit = card.upper()
    c = eval("u'\\U0001f0{}{}'".format(
        SUITS[1][SUITS[0].index(suit)],
        FACES[1][FACES[0].index(face)]
    ))
    if color:
        c = (suit in 'HD' and RED or BLACK) + c + RESET
    return c
