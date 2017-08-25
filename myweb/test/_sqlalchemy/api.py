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
        print 'info-name:',i.userinfo.name
    print 'articles-list:',i.articles

#创建文章
for i in article_data:
    #db_server.article_create(i)
    pass

#获取文章列表
for i in db_server.article_get_all():
    print i.id,i.title,i.context,i.user_id,i.cate_id,i.author,i
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
for i in db_server.tag_get_all():
    print i.id,i.name,i.articles

#给文章添加标签 false
#db_server.add_tag_for_article(1,1)



