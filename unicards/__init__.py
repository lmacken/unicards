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

import sys

if sys.version_info.major == 3:
    unichr = chr

# Input values and their corresponding unicode hex values
FACES = 'A23456789TJCQK', '123456789ABCDE'
SUITS = 'SHDC', 'ABCD'

# ANSI color escape codes
COLORS = ['\x1b[%dm' % c for c in (30, 31, 34, 32, 39)]


def unicard(card, color=False):
    if card[:2] == '10':
        card = 'T' + card[2]
    face, suit = card.upper()
    c = unichr(int("0001f0{}{}".format(
        SUITS[1][SUITS[0].index(suit)],
        FACES[1][FACES[0].index(face)]
    ), base=16))
    if color:
        c = COLORS[SUITS[0].index(suit)] + c + COLORS[-1]
    return c
