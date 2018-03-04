♣ unicards
==========

.. image:: https://api.travis-ci.org/lmacken/unicards.png?branch=master
   :target: http://travis-ci.org/lmacken/unicards
.. image:: https://coveralls.io/repos/lmacken/unicards/badge.png?branch=master
   :target: https://coveralls.io/r/lmacken/unicards
.. image:: https://img.shields.io/pypi/v/unicards.svg
   :target: https://crate.io/packages/unicards
.. image:: https://img.shields.io/pypi/dm/unicards.svg
   :target: https://crate.io/packages/unicards

A Python module for converting strings into `unicode playing cards <https://en.wikipedia.org/wiki/Unicode_Playing_Card_Block>`_.

.. image:: http://lewk.org/img/unicards-4color.png

♠ Installation
--------------

::

   pip install unicards

♦ API
-----

::

   >>> from unicards import unicard
   >>> print(unicard('As'))
   🂡
   >>> print(unicard('Jd'))
   🃋
   >>> print(unicard('Tc'))
   🃚
   >>> print(unicard('2h'))
   🂲
   >>> unicard('8d', color=True)
   u'\x1b[31m\U0001f0c8\x1b[39m'
   >>> unicard('b')
   🂠


♥ License
---------

`Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_
