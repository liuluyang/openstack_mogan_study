#coding:utf8
import os
import urllib
import urllib2

def save_img(img_url,file_name,file_path='img'):
    try:
        if not os.path.exists(file_path):
            print 'make dirs %s'%(file_path)
            os.makedirs(file_path)
        file_suffix = os.path.splitext(img_url)[1]
        print os.path.splitext(img_url)
        print file_suffix
        filename = '{}{}{}{}'.format(file_path,'\\',file_name,file_suffix)
        print os.sep
        print filename
        urllib.urlretrieve(img_url,filename=filename)
    except Exception as e:
        print e

if __name__ == '__main__':
    #url = 'http://jbcdn2.b0.upaiyun.com/2016/08/74d126ea14f964e13bb07d24843bdab4.jpg'
    #save_img(url, 'test1')
    pass
#url = 'http://img2.imgtn.bdimg.com/it/u=801003741,1615586483&fm=26&gp=0.jpg'
#url_x = 'http://51.alook.pw/media/photos/556385.jpg'
#u = url.split('/')[-1]
#urllib.urlretrieve('http://jbcdn2.b0.upaiyun.com/2016/08/74d126ea14f964e13bb07d24843bdab4.jpg', u)

for i in range(4001):
    print 'loading %s......'%(181+i)
    url = 'http://51.alook.pw/media/photos/'+str(181+i)+'.jpg'
    u = url.split('/')[-1]
    try:
        r = urllib2.urlopen(url, timeout=5)
        urllib.urlretrieve(url, 'img\\'+u)
        print 'finished'
    except:
        print 'this picture is time out!'
        pass




