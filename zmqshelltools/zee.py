import sys
import zmq

def mainloop(addr):
    """foo"""
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUSH)
    socket.bind(addr)
    
    for line in sys.stdin:
        socket.send(line)
        print "->", line,
    
    socket.close()
        
def main():
    mainloop(sys.argv[1])

if __name__ == '__main__':
    main()