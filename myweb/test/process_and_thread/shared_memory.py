from multiprocessing import Pool, Value, Array, sharedctypes, Process


def run_task(v, i):
    if i == 2:
        v.value = 1.1
    print v.value

if __name__ == '__main__':
    p = Pool()
    v = Value('d', 0.0)
    #for i in range(5):
        #p.apply_async(run_task, args=(v, i))

    #p.close()
    #p.join()
    for i in range(5):
        Process(target=run_task, args=(v, i)).start()
    #p.start()
    #p.join()
    #print 'end'

