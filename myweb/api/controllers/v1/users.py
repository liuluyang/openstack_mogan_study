#coding:utf8
import pecan
from pecan import rest
from pecan import request
from wsme import types as wtypes

from myweb.api.controllers.v1 import types
from myweb.api import expose
import uuid
import wsme
from myweb.api.controllers import base
from myweb.api import validation
from myweb.api.controllers.v1.schemas import user as schems_user

from myweb.objects import user as user_obj

example_users_list = [
    {
        'id':1,
        'user_id':'1',
        'name':'bob',
        'email':'ww@dd.com'
    },
    {
        'id':2,
        'user_id':'11',
        'name':'alince',
        'email':'ww@hhd.com'
    }
]

class User(base.APIBase):


    id = int
    user_id = wtypes.text
    name = wsme.wsattr(wtypes.text,mandatory=True)
    email = wtypes.text
    like = [wtypes.text]
    extra = {wtypes.text:types.jsontype}

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.fields = []
        for field in {'id','user_id','name','email','like','extra'}:
            if hasattr(self, field):
                self.fields.append(field)

        print kwargs

class Users(wtypes.Base):
    users = [User]

class UserController(rest.RestController):



    def __init__(self, name):
        super(UserController, self).__init__()
        self.name = name
        #print self.name,pecan.request.context   #在此处接收不到context
        #print request.db_conn

    _custom_actions = {
        'detail': ['GET']
    }

    @expose.expose(wtypes.text)
    def detail(self):
        return 'sssssss'

    @expose.expose(None)
    def get(self):
        print self.name
        #print type(id),'d'
        #print user_id,'i am id'
        #print 'I am get user',id
        #print request.db_conn                #
        #print pecan.request.db_conn,'db'
        #print request.context                 #
        #print pecan.request.context.user_name           #
        user_info = {
            #'name':self.name,
            #'name':'Bob',
        }
        #print pecan.request.public_url
        #return User(**user_info)
        #return 'get'

    @expose.expose(User, body=User)
    def put(self, user):
        user_info = {
            'id': self.user_id,
            'name': user.name,
        }
        return User(**user_info)

    @expose.expose(None, wtypes.text, status_code=200)
    def delete(self, id):
        print 'Delete user_id: %s' % self.name,id

class UsersController(rest.RestController):


    #@pecan.expose()
    #def _lookup(self, user_id, *remainder):
        #print remainder,user_id
        #return UserController(user_id), remainder

    @expose.expose(None, wtypes.text)
    def get_one(self, id):
        print 'get one user'
        print id
        print pecan.request.path.split('/')[:-1][-1]
        #db_conn = request.db_conn
        #users = db_conn.list_users()
        #db_conn = request.db_conn
        #db_conn.create_user('xiaoming')
        #print db_conn.list_users(),'hi i am user list'
        #for i in db_conn.list_users():
            #print i,i.name,i.id,i.user_id
        '''
        users = example_users_list
        users_list = []
        for user in db_conn.list_users():
            u = User()
            u.id = user.id
            u.user_id = user.user_id
            u.name = user.name
            u.email = user.email
            users_list.append(u)
        '''
        #return Users(users=users_list)

    @expose.expose(None, wtypes.text, wtypes.text,wtypes.text, status_code=201 )
    def put(self, id, user,desc):
        print 'update a user'
        print id
        print user
        print desc
        #return User(**{'name':'dd','user':1,'user_id':'2'})

    @expose.expose(User,types.boolean, body=User, status_code=201 )
    def post(self, change, user):
        print 'create a user'
        print change
        validation.check_schema({'policy':'disk','metadata':{'1':'w'}}, schems_user.user_add)
        print user.as_dict()
        user_db = user_obj.User(**user.as_dict())
        #user_db.id = 1
        print user_db
        values = user_db.obj_get_changes()
        print "get_changes",values
        print "obj_attr_set of name",user_db.obj_attr_is_set('name')
        print "changed_fields",user_db._changed_fields
        user_db.obj_reset_changes()
        print "obj_attr_set of name",user_db.obj_attr_is_set('name')
        print "clear changed_fields",user_db._changed_fields
        #setattr(user_db, 'name', 'yy')
        del user_db.extra['v']
        del user_db.extra['type']
        user_db.extra = user_db.extra
        user_db.like = user.like+[1]
        print "changed_fields",user_db._changed_fields
        print user_db.obj_what_changed()
        values = user_db.obj_get_changes()
        print "get_changes",values
        print user_db['extra']

        print "obj_attr_set of extra",user_db.obj_attr_is_set('extra')
        print user_db._obj_name
        print 'extra' in user_db
        print user_db.__dict__
        print user_db.id
        print user.created_at
        print user.fields
        #user.name = 'change_name'
        print user.name,'name'
        print user.extra
        print user.like,'like'
        if 'foot' in user.like:
            print 'foot in list'
        if user.name == '':
            print 1
        dic = {'user':'l','name':'RE','id':''}
        if dic.get('id'):
            print dic

        #return User(**{'name':'dd','user':1,'user_id':'2'})
        setattr(user, 'other', "hook")
        print user.other
        #user.name = 1
        del user.name
        #return user

        user = User()
        #user.name = 'hel'
        new_user = user_obj.User()
        new_user.id = None
        new_user.name = 'd '
        del new_user.name
        print new_user
        new_user.extra = {"d":1}
        #new_user.id = 1
        print 'extra' in new_user
        print 'id' in new_user
        print new_user.extra
        print new_user.obj_attr_is_set('extra')


        return user


        #pecan.request.context = {1:2}
        #print pecan.request.db_conn
        #print pecan.request.db_conn==request.db_conn
        #print userw
        #print type(userw.name)
        #print status,'status'
        #db_conn = request.db_conn
        #db_conn.create_user(userw.name)
        #print db_conn.list_users(),'hi i am user list'
        #for i in db_conn.list_users():
            #print i,i.name,i.id,i.user_id
        #print pecan.response.status

    @expose.expose(wtypes.text, wtypes.text)
    def delete(self, id):
        print id,'delete id'
        return {'name':'dd','user':1,'user_id':'2'}

    @expose.expose(None)
    def get_all(self):
        print 'get all'

