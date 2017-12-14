#coding:utf8

from myweb.test._sqlalchemy import db_api

db_server = db_api.Connection()


user_data = [
             {'username':'wan','password':'123123'},
             {'username':'xiai','password':'123412','email':'tianqi@qq.com'}
             ]

article_data = [
    {'title':'python','context':'hello world!','user_id':1},
    {'title':'java','context':'hello java!','user_id':1},
    {'title':'javascript','context':'hello javascript!','user_id':2},
    {'title':'php','context':'what is php!','user_id':2},
]

#新建用户
for data in user_data:
    #db_server.user_create(data)
    pass

#获取用户列表
for i in db_server.user_get_all():
    print (i.id,i.username,i.password,i.email)
    if i.userinfo:
        print 'info-name:',i.userinfo
    print 'articles-list:',i.articles

print '获取指定用户'
u = db_server.user_get_one(user_id=1)
print u.userinfo        #这里不需要options(orm.joinedload())方法就可以获取其他数据
                        #但是mogan上需要这个方法进行惰性加载
                        #问题解决：如果加上session.close()使会话结束 就需要进行惰性加载
print u.articles

print '获取指定用户详细信息'
print db_server.user_info_get_one(user_id=1).user.username

#创建文章
for i in article_data:
    #db_server.article_create(i)
    pass

#获取文章列表
print '获取文章列表'
for i in db_server.article_get_all():
    print i.id,i.title,i.context,i.user_id,i.cate_id,i.author.username
    print 'category:',i.category.name
    print 'tags-list:',i.tags

#更新文章数据
#db_server.article_update({'cate_id':3}, 4)

categories_data = [
    {'name':'math'},
    {'name':'history'},
    {'name':'human'}
]
#新建文章类型
for i in categories_data:
    #db_server.category_create(i)
    pass

tags_data = [
    {'name':'one thousand'},
    {'name':'two thousand'},
    {'name':'three thousand'}
]
#新建文章标签
for i in tags_data:
    #db_server.tag_create(i)
    pass

#文章标签列表
print '\'文章标签列表\''
for i in db_server.tag_get_all():
    print i.id,i.name,i.articles

#给文章添加标签 false
#db_server.add_tag_for_article(1,1)






