#coding:utf8
import gevent
from gevent import monkey,socket

monkey.patch_all()   #有IO才做时需要这一句

s = socket.socket(2,1)  #用的都是gevent模块中的socket,但用法一样
#s.setsockopt(1,2,1)
s.bind(('',8080))
s.listen(1024)
print 'listening ...8080'
def func_accept():
    while 1:
        cs,userinfo = s.accept()
        print('来了一个客户'+str(userinfo))
        g = gevent.spawn(func_recv,cs)  #每当有用户连接,增加一条协程

def func_recv(cs):
    try:
        while 1:
            recv_data = cs.recv(1024)
            print(recv_data)  #程谁堵塞了,便会跳转至其他协程
            if len(recv_data) > 0:
                cs.send(recv_data)
            else:
                cs.close()
                break
    except:
        print cs,'is cut connection'

#g1 = gevent.spawn(func_accept)
#g1.join()
func_accept()
