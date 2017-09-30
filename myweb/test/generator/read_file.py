#coding:utf8

def read_lines():
    with open('desc.txt', 'r') as f:
        #f.seek(0,2)
        #for i in range(15):
            #print f.readline()
        while True:
            lines = f.readline()
            if not lines:
                yield 0
                #continue
            yield lines


#print r.next()
#print r.next()
def read_file_by_line():
    r = read_lines()
    while True:
        put = raw_input('>>>')
        if put == 'close':
            print 'closing... ok'
            break
        else:
            content = r.next()
            print type(content)
            if content:
                print content
            else:
                break
                #print 'nothing'
read_file_by_line()

