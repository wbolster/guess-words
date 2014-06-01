Word guesser
============

This is a simple program that generates known words for a set of letters. It
uses a brute force approach to tests all possible combinations for the given
letters against the words in a known word list.

This program can be used for games such as Scrabble or Draw Something.

Usage
=====

Download the program and run it with ``--help`` to see instructions::

    $ ./guess.py --help
    usage: guess.py [-h] [--dict DICT] n_letters letters

    positional arguments:
      n_letters    number of letter in word to guess
      letters      all possible letters

    optional arguments:
      -h, --help   show this help message and exit
      --dict DICT  path to word list file


Example
=======

The example below generates 5 letter words for the given letters::

    $ ./guess.py 5 uhrcsyabcr
    Possible answers:
      1. barry
      2. brash
      3. brays
      4. burch
      5. burrs
      6. bursa
      7. busch
      8. bushy
      9. carry
     10. chary
     11. crabs
     12. crash
     13. crush
     14. curry
     15. cushy
     16. cyrus
     17. harry
     18. hurry
     19. saucy
     20. scary
     21. scrub
     22. scuba
     23. shrub
     24. surya
     25. yucca


License
=======

Copyright © 2014, Wouter Bolsterlee

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

* Neither the name of the author nor the names of its contributors may be used
  to endorse or promote products derived from this software without specific
  prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

*(This is the OSI approved 3-clause "New BSD License".)*
