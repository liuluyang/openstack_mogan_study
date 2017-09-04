#coding:utf8

from multiprocessing import Pool
import os, time, random

from myweb.test.process_and_thread.func_timelimit import timelimit
from myweb.test.loadpicture.save_picture import make_url, load_image
from myweb.test.run_time import run_time

@run_time
def main():
    print 'parent process %s'%(os.getpid())
    p = Pool(4)
    for i in range(50):
        url = make_url(start_num=38780, index=i)
        p.apply_async(timelimit, args=(11, load_image), kwds={'args':(url,)})
    print 'waiting for all subprocess done '
    p.close()
    p.join()
    print 'all done!'

if __name__ == '__main__':
    main()



