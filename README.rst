Word guesser
============

This is a simple program that generates known words for a set of letters. It
uses a brute force approach to test all possible combinations for the given
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
      4. brush
      5. burch
      6. burrs
      7. bursa
      8. busch
      9. bushy
     10. carry
     11. chars
     12. chary
     13. crabs
     14. crash
     15. crush
     16. curbs
     17. curry
     18. cushy
     19. cyrus
     20. harry
     21. hurry
     22. saucy
     23. scary
     24. scrub
     25. scuba
     26. shrub
     27. surya
     28. yucca


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
