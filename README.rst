===========
Kanji Lists
===========
A collection of Japanese character lists, including jōyō kanji, JLPT, and more.

Installation
============

.. code-block:: console

    pip install kanji-lists


Usage
=====

Using a list is simple enough:

.. code-block:: pycon

    >>> from kanji_lists import JOYO
    >>> "桃" in JOYO
    True
    >>> "苺" in JOYO
    False
    >>> len(JOYO)
    2136

Some lists also have subordinate lists:

.. code-block:: pycon

    >>> from kanji_lists import KYOIKU
    >>> "火" in KYOIKU.GRADE1
    True
    >>> "火" in KYOIKU.GRADE2
    False

All lists inherit from `set`:

.. code-block:: pycon

    >>> isinstance(KYOIKU, set)
    True
    >>> KYOIKU.GRADE1.issuperset({'一', '二', '三'})
    True

Lists can also have different versions:

.. code-block:: pycon

    >>> from kanji_lists import KYOIKU
    >>> KYOIKU.HEISEI4.GRADE6 - KYOIKU.REIWA2.GRADE6
    {'城'}
    >>> "城" in KYOIKU.REIWA2.GRADE4
    True

If you do not specify a version, the default will be chosen. In the case of lists
maintained by the Japanese government, this will generally be the most recent list.
Since the default can change, specify a version if you want to make sure that you
get the same version of the list across updates.

Available Lists and Versions
============================


- JINMEIYO
    
  - HEISEI25
  - HEISEI27
  - HEISEI29
- JLPT
    
  - TANOS
            
    - N1
    - N2
    - N3
    - N4
    - N5
- JOYO
    
  - HEISEI22
  - SHOWA56
- KYOIKU
    
  - HEISEI4
            
    - GRADE1
    - GRADE2
    - GRADE3
    - GRADE4
    - GRADE5
    - GRADE6
  - REIWA2
            
    - GRADE1
    - GRADE2
    - GRADE3
    - GRADE4
    - GRADE5
    - GRADE6
  - SHOWA36
            
    - GRADE1
    - GRADE2
    - GRADE3
    - GRADE4
    - GRADE5
    - GRADE6
  - SHOWA55
            
    - GRADE1
    - GRADE2
    - GRADE3
    - GRADE4
    - GRADE5
    - GRADE6