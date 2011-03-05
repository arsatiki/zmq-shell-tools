===============
0MQ Shell Tools
===============

My idea is to separate Unix pipes in time and space. On machine #1::

    grep foo -r . | zee tcp://*:6000 --no-stdout

And on machines #2,  #3, #4 upto #_n_::

    zat tcp://machine1:6000 | <further data processing>

Another fascinating possibility is the creation of simple servers, such as the
worlds smallest echo server::

    zserver tcp://*:1234 cat


TODO
----

- Tests
- `getopt`


Current Status
==============

Obviously a work in progress. Nay! A work in gestation.

I'm first prototyping this on Python to find the proper interface. If time
and energy permit, I will convert them to C.

`zee`
=====

`zee <ZMQ endpoint>` reads input from standard input. Individual lines are
sent as messages to the specified ZMQ endpoint.

The `zee` tool is named analogously to `tee`. Instead of making a T-shaped
junction in the pipeline, `zee` creates sort of a Z-shaped junction. The lower
bar of the Z can be seen to represent another parallel pipeline.

Also, it is a pun on ZMQ and `tee`. Obviously.

The default socket type is PUSH. Use the `--pub` option to create a PUB type
socket.

TODO for `zee`
--------------

- Add `--no-stdout` or `-q` or `-s` option
- Add `--pub` option
- Multiple end points? (Not really worth it since it is easy to write just
  `zee ipc://sock1 | zee ipc://sock2`)


`zat`
=====

`zat [[--sub] <ZMQ endpoint> ...]` reads specified ZMQ sockets and outputs the
messages to the standard output.

The `zat` is named after the `cat` tool. Unfortunately the `zcat` is already
reserved. (Other alternative names: `zoot`, `ztdin`, `czat` and `catz`.)

The default socket is type is PULL. Use the `--sub` option to specify a SUB
type socket.

TODO for `zat`
--------------
- `zat` to support sub sockets as well
- `zat` should also pass stdin through
- Three options for stdin:
  - always include in output
  - include if a flag is (not) present
  - imitate `cat`, i.e. absent or -

