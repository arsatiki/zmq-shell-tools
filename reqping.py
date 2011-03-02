import sys
import zmq

def main(addr, sender):
    """foo"""

    ctx = zmq.Context()
    socket = ctx.socket(zmq.REQ)
    socket.connect(addr)

    k = 0
    while True:
        socket.send("Message %d from %s" % (k, sender))
        print socket.recv()
        k += 1

    socket.close()
        
        
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
