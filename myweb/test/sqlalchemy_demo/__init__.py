#coding:utf8

'''
在SQLAlchemy中一个Session（可以看作）是一个transaction，每个操作（基本上）对应一条或多条SQL语句，这些SQL语句需要发送到数据库服务器才能被真正执行，而整个transaction需要commit才能真正生效，如果没提交，一旦你的程序挂了，所有未提交的事务都会被回滚到事务开始之前的状态。
flush就是把客户端尚未发送到数据库服务器的SQL语句发送过去，commit就是告诉数据库服务器提交事务。
简单说，flush之后你才能在这个Session中看到效果，而commit之后你才能从其它Session中看到效果
'''