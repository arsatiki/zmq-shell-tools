import sys
import zmq

def main(addr):
    """foo"""
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUSH)
    socket.bind(addr)
    
    for line in sys.stdin:
        socket.send(line)
        print "->", line,
    
    socket.close()
        
        
if __name__ == '__main__':
    main(sys.argv[1])