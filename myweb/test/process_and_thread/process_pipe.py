from multiprocessing import Process, Pipe

def proc1(pipe):
   for i in xrange(100):
       pipe.send(i)

def proc11(pipe):
   for i in xrange(100,200):
       pipe.send(i)

def proc2(pipe):
    while True:
        print "proc2 rev:", pipe.recv()
def main():
    pipe = Pipe()
    Process(target=proc1, args=(pipe[0],)).start()
    Process(target=proc11, args=(pipe[0],)).start()
    Process(target=proc2, args=(pipe[1],)).start()

if __name__ == '__main__':
    main()