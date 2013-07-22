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

try:
    from colorama import init
    from colorama import Fore
    init(autoreset=True)
    colors = True
except ImportError:
    colors = False

faces = 'A23456789TJCQK'
unicode_faces = '123456789ABCDE'
suits = 'shdc'
unicode_suits = 'ABCD'


def unicard(card):
    if card.startswith('10'):
        card = card.replace('10', 'T')
    code = "u'\\U0001f0{}{}'".format(unicode_suits[suits.index(card[1].lower())],
                                     unicode_faces[faces.index(card[0].upper())])
    c = eval(code)
    if colors:
        c = (card[1] in 'hd' and Fore.RED or Fore.BLACK) + c + Fore.RESET
    return c
