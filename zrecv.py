import sys
import zmq

def main(addr):
    """foo"""
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PULL)
    socket.connect(addr)

    while True:
        print socket.recv(),
        
    socket.close()
        
        
if __name__ == '__main__':
    main(sys.argv[1])
    