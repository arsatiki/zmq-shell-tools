from subprocess import Popen, PIPE
import sys

import zmq

def main(addr, cmd):
    """foo"""

    ctx = zmq.Context()
    socket = ctx.socket(zmq.REP)
    socket.bind(addr)

    while True:
        # Not line by line ATM.
        # It'd be nice but probably not sane.
        proc = Popen(cmd, bufsize=1, stdin=PIPE, stdout=PIPE)
        input = socket.recv() # XXX Multiparts?
        output, _ = proc.communicate(input)
        socket.send(output)

    socket.close()
        
        
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
