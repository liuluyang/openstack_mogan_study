#coding:utf8

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload

import time

from myweb.db import engine_test as models
from myweb.test.inbuild import hashlib_


_engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/myweb')

def make_models(engine):
    models.Base.metadata.create_all(engine)

make_models(_engine)

def get_session():
    engine = _engine
    session = sessionmaker(bind=engine)
    session = session()
    return session

def update(model,data):
    for key,val in data.items():
        if hasattr(model, key):
            setattr(model, key, val)
    return model


class connection(object):

    def __init__(self):
        pass

    def user_create(self,user):
        session = get_session()
        model = models.User()

        password = hashlib_.passwd_md5(user.get('password'))
        user['password'] = password

        new_user = update(model, user)
        try:
            session.add(new_user)
            session.commit()
            print 'create a new user success'
        except Exception as e:
            print e

        return new_user

    def user_get_all(self):
        session = get_session()
        users = session.query(models.User)
        users = users.all()
        print 'get all users success'
        return users

    def user_delete(self, username):
        session = get_session()
        user_query = session.query(models.User).filter(models.User.username.in_(['lizhiwen']))
        #if user_query.delete()==1:
            #user_query.delete()
            #session.commit()
            #print 'ok'
        count = user_query.count()
        print 'delete user num is ',count
        user_query = user_query.all()
        return user_query

    def user_get_one(self, user_id):
        session = get_session()
        user_query = session.query(models.User).filter_by(id=user_id)#.options(joinedload('articles'))

        #the_filter = [models.User.articles.has(title='python')]
        #user_query = user_query.filter(or_(*the_filter))

        try:
            user = user_query.one()
        except Exception as e:
            print e

        return user




    def article_create(self, article):
        session = get_session()
        model = models.Article()

        new_article = update(model, article)
        try:
            session.add(new_article)
            session.commit()
            print 'create an article success'
        except Exception as e:
            print e
        return new_article

    def article_get_all(self):
        session = get_session()
        articles = session.query(models.Article)
        articles = articles.all()
        print 'get all articles success'
        return articles

    def article_update(self, article, article_id):
        session = get_session()
        article_query = session.query(models.Article).filter_by(id=article_id)
        try:
            article_query = article_query.one()
            article = update(article_query, article)
            session.add(article)
            session.commit()
            print 'article update success'
            return article
        except Exception as e:
            print e

    def category_create(self, category):
        session = get_session()
        new_category = models.Category()

        new_category = update(new_category, category)
        session.add(new_category)
        session.commit()
        print 'create a category success'
        return new_category

    def category_get_all(self):
        session = get_session()
        categories = session.query(models.Category)
        categories = categories.all()
        print 'get all categories success'
        return categories

    def userinfo_create(self, userinfo_data):
        session = get_session()
        userinfo = models.UserInfo()

        new_userinfo = update(userinfo, userinfo_data)
        try:
            session.add(new_userinfo)
            session.commit()
        except Exception as e:
            print e

        return new_userinfo

    def userinfo_destroy(self, userinfo_id):
        session = get_session()
        userinfo_query = session.query(models.UserInfo).filter_by(id=userinfo_id)


        count = userinfo_query.delete()
        if count != 1:
            print 'delete not one'
        else:
            session.commit()

    def tag_get_all(self):
        session = get_session()
        tag_query = session.query(models.Tag).all()

        return tag_query

    def tag_destroy(self):
        session = get_session()
        #result = session.query(models.Tag).filter(models.Tag.name.in_(['1','on']))\
            #.delete(synchronize_session=False)
        result = session.query(models.Tag).filter(models.Tag.name=='onfff').delete()
        #time.sleep(3)
        session.commit()
        #操作结束 但未结束会话 且查询的字段没有索引时 会锁住整张表 无法进行其他操作

        print result

    def tag_update(self, values, tag_id):
        session = get_session()
        tag_query = session.query(models.Tag).filter_by(id=tag_id)

        try:
            tag_query = tag_query.one()
            #tag_query.name = 'g'
            #session.add(tag_query)
            #session.commit()
        except Exception as e:
            print e

        ref = update(tag_query, values)
        session.add(ref)
        session.commit()
        return ref

    def lockmode_test(self):
        session1 = get_session()
        session2 = get_session()

        user1 = session1.query(models.User).filter_by(username='lizhi').with_lockmode('update').one()
        user2 = session2.query(models.User).filter_by(id=1).one()
        user2.username = 'jokef'
        session2.add(user2)
        session2.commit()

        #time.sleep(4)
        #session1.commit()
        #session2.commit()

    def server_get_all(self):
        session = get_session()

        servers_query = session.query(models.Server).filter(and_(models.Server.id>2,models.Server.id<4)).all()

        print servers_query
        print session.query(models.Server).filter(and_(models.Server.id>2,models.Server.id<4))

        return servers_query

    def flavor_get_all(self):
        session = get_session()

        flavor_query = session.query(models.Flavor).all()

        return flavor_query

    def flavor_destroy(self, flavor_id):
        session = get_session()
        query = session.query(models.Flavor).filter_by(id=flavor_id)

        count = query.delete()
        if count==1:
            session.commit()
        else:
            print 'delete fail'

    def flavor_create(self):
        session = get_session()
        flavor = models.Flavor()

        flavor.name = 'mini'
        #session.flush(flavor)
        session.add(flavor)
        session.commit()

    def compute_node_create(self, values):
        compute_node = models.ComputeNode()
        update(compute_node, values)

        session = get_session()
        session.add(compute_node)
        session.commit()

    def compute_node_get(self, node_id):
        session = get_session()
        query = session.query(models.ComputeNode).filter_by(id=node_id)

        try:
            return query.one()
        except Exception as e:
            print e

    def compute_node_update(self, node_id, values):
        session = get_session()
        query = session.query(models.ComputeNode).filter_by(id=node_id)

        try:
            ref = query.with_lockmode('update').one()      #the with_lockmode func is useful
        except Exception as e:
            print e

        update(ref, values)
        session.add(ref)
        session.commit()

        '''
        session_2 = get_session()
        query_2 = session_2.query(models.ComputeNode).filter_by(id=node_id).one()
        update(query_2, values)
        session_2.add(query_2)
        session_2.commit()
        '''










user_data = [
             {'username':'wangyang','password':'123123'},
             {'username':'xiaoli','password':'123412','email':'tianqi@qq.com'}
             ]

article_data = [
    {'title':'python','context':'hello world!','user_id':1},
    {'title':'java','context':'hello java!','user_id':1},
    {'title':'javascript','context':'hello javascript!','user_id':2},
    {'title':'php','context':'what is php!','user_id':2},
]

article_data_test = [
    {'title':'budug','context':'hello world!','user_id':11},
]

categories_data = [
    {'name':'math'},
    {'name':'history'},
    {'name':'human'}
]

article_update_date = [
    {'cate_id':1},
    {'cate_id':2},
    #{'cate_id':3},
    #{'cate_id':1},
    #{'cate_id':1},
    #{'cate_id':1},
]

userinfo_data = [
    {'name':'lili','phone':'123123','address':'beijing','user_id':1}
]


db_server = connection()

for i in user_data:
    #db_server.user_create(i)
    pass


for i in db_server.user_get_all():
    print i.id,i.username,i.password,i.email
    if i.userinfo:
        print i.userinfo.name
    print i.articles

#print db_server.user_get_one(1)

print '#'*20, 'above is about user'

for i in article_data:
    #db_server.article_create(i)
    pass

#for i in article_update_date:
for id in range(5,7):
    #db_server.article_update(article_update_date[id-1],id)
    pass

for i in db_server.article_get_all():
    print i.id,i.title,i.context,i.user_id,i.cate_id,i.author,i
    print i.tags



print '#'*20, 'above is about article'

for i in categories_data:
    #db_server.category_create(i)
    pass

for i in db_server.category_get_all():
    print i.id, i.name, i.articles, i

#print db_server.user_delete('lizhiwen')

print '#'*20,'above is about category'

for i in userinfo_data:
    #db_server.userinfo_create(i)
    pass

#db_server.userinfo_destroy(2)

for i in db_server.tag_get_all():
    print i.articles


db_server.tag_destroy()

#db_server.lockmode_test()


#db_server.tag_update({'name':'one'},1)

print '#'*30

for i in db_server.server_get_all():
    print i.id,i.name,i.flavor_id,i.flavor

for i in db_server.flavor_get_all():
    print i.id,i.name,i.servers


#print models.Base.metadata

#db_server.flavor_destroy(2)
#db_server.flavor_create()

compute_node_data = {
    'node_uuid':'dfagfafass','cpus':4,'memory_mb':16,'hypervisor_type':'vn2','node_type':'compute',
    'extra_specs':{'dada':'2'}
}

#db_server.compute_node_create(compute_node_data)

node_obj = db_server.compute_node_get(4)
print node_obj.used,type(node_obj.extra_specs)
print node_obj.ports
print node_obj.disks

compute_node_upadte = {
    'cpus':4,'memory_mb':16,'hypervisor_type':'virtual_box','node_type':'compute',
    'extra_specs':{'dada':'2222'}
}
#db_server.compute_node_update(1, compute_node_upadte)
print '#'*34
#time.sleep(40)
print db_server.user_get_one(1).articles
