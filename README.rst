♣ unicards
==========

.. image:: https://pypip.in/v/unicards/badge.png
   :target: https://crate.io/packages/unicards
.. image:: https://pypip.in/d/unicards/badge.png
   :target: https://crate.io/packages/unicards

Convert strings into unicode playing cards

🂡 🂢 🂣 🂤 🂥 🂦 🂧 🂨 🂩 🂪 🂫 🂬 🂭 🂮 🂱 🂲 🂳 🂴 🂵 🂶 🂷 🂸 🂹 🂺 🂻 🂼 🂽 🂾 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃌 🃍 🃎 🃑 🃒 🃓 🃔 🃕 🃖 🃗 🃘 🃙 🃚 🃛 🃜 🃝 🃞

♦ Python API
------------

::

   >>> from unicards import unicard
   >>> print(unicard('As'))
   🂡
   >>> print(unicards.unicard('Jd'))
   🃋
   >>> print(unicards.unicard('Tc'))
   🃚
   >>> print(unicards.unicard('2h'))
   🂲

♠ Colorization
---------------

If the `colorama <https://code.google.com/p/colorama/>`_ module is available,
your cards will automatically be colorized. This feature can be disabled by
setting ``unicards.colors`` to ``False``.

♥ License
---------

.. image:: https://www.gnu.org/graphics/gplv3-127x51.png
   :target: https://www.gnu.org/licenses/gpl.txt
