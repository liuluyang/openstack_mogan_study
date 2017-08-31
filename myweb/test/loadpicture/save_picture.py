#coding:utf8
import os
import urllib
import urllib2

from myweb.test._oslo_log.olso_log_test import LOG

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
def f():
    for i in range(4001):
        print 'loading %s......'%(973+i)
        url = 'http://51.alook.pw/media/photos/'+str(973+i)+'.jpg'
        u = url.split('/')[-1]
        try:
            #r = urllib2.urlopen(url, timeout=5)
            urllib.urlretrieve(url, 'img\\'+u)
            print 'finished'
        except:
            print 'this picture is time out!'
            pass

def make_url(start_num=0, index=None):
    if not isinstance(start_num, int):
        LOG.error('start_num %s is not int'%start_num)
        return None
    if index is not None and isinstance(index, int):
        base = 'http://51.alook.pw/media/photos/'
        return base+str(start_num+index)+'.jpg'
    else:
        LOG.error('index %s is error'%index)
        return None


def load_image(image_url, file_path='image\\'):
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        image_name = image_url.split('/')[-1]
        print 'loading %s'%image_name
        urllib.urlretrieve(image_url, file_path+image_name)
        LOG.info('load image success!')
        return True
    except:
        LOG.error('load image failed!')

#if __name__ == '__main__':
    #load_image('http://jbcdn2.b0.upaiyun.com/2016/08/74d126ea14f964e13bb07d24843bdab4.jpg')
    #load_image(make_url(index=3333))

#print make_url(1, 0)
