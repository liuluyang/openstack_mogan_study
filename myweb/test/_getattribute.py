#coding:utf8

class C(object):
    a = 'abc'

    def __getattribute__(self, *args, **kwargs):
        try:
            print("__getattribute__() is called")

            attr = object.__getattribute__(self, *args, **kwargs)
            print attr
            print args,kwargs
            if args[0] == 'a':
                return object.__getattribute__(self, *args, **kwargs)
            else:
                print '调用函数foo()'
                obj = object.__getattribute__(self,args[0])
                #if args[0] in obj:
                    #print 1
                return obj
        except:
            return 'attr'
            #return self.__getattr__(args)

    def __getattr__(self, item):
        return 'default'
    def foo(self, name):
        return "hello",name
    def foo2(self):
        return "hello2"
if __name__ == '__main__':
    c = C()
    print c.foo
    print c.foo3