0MQ Shell Tools
===============

My idea is to separate Unix pipes in time and space. On machine #1::

    grep foo -r . | zsend tcp://*:6000

And on machines #2,  #3, #4 upto #_n_::

    zrecv tcp://machine1:6000 | <further data processing>

Another fascinating possibility is the creation of simple servers, such as the
worlds smallest echo server::

    zserver tcp://*:1234 cat


Current Status
--------------

Obviously a work in progress. Nay! A work in gestation.

I'm first prototyping this on Python to find the proper interface. If time
and energy permit, I will convert them to C.


TODO
----

- `setup.py` and commands as egg entrypoints
- Tests
- `getopt`
- zrecv should read many sockets (and stdin) and combine their outputs

