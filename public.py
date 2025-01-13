from flask import *
from database import *
import uuid

public=Blueprint('public',__name__)

@public.route('/')
def home_page():
    return render_template("home.html")


@public.route('/login',methods=['get','post'])
def login():
    if 'submit' in request.form:
        username=request.form['username']
        password=request.form['password']

        qry="select * from login where username='%s' and password='%s'"%(username,password)
        res=select(qry)
        print(res)

        if res:
            session['log']=res[0]['login_id']

            if res[0]['usertype']=='admin':

                return ("<script>alert('login successfull');window.location='/admin_home'</script>")
            
            if res[0]['usertype']=='advisor':
                qry1="select * from advisor where login_id='%s'"%(session['log'])
                res1=select(qry1)
                if res1:
                    session['advisor']=res1[0]['advisor_id']
                return ("<script>alert('login successfull');window.location='/advisor_home'</script>")
            else:
                return ("<script>alert('admin not verified');window.location='/login'</script>")
            
            
        else:
            return ("<script>alert('invalid username or password');window.location='/login'</script>")


    return render_template("login.html")
@public.route('/login',methods=['get','post'])
def login():
    if 'submit' in request.form:
        username=request.form['username']
        password=request.form['password']

        qry="select * from login where username='%s' and password='%s'"%(username,password)
        res=select(qry)
        print(res)

        if res:
            session['log']=res[0]['login_id']

            if res[0]['usertype']=='admin':

                return ("<script>alert('login successfull');window.location='/admin_home'</script>")
            
            if res[0]['usertype']=='advisor':
                qry1="select * from advisor where login_id='%s'"%(session['log'])
                res1=select(qry1)
                if res1:
                    session['advisor']=res1[0]['advisor_id']
                return ("<script>alert('login successfull');window.location='/advisor_home'</script>")
            else:
                return ("<script>alert('admin not verified');window.location='/login'</script>")
            
            
        else:
            return ("<script>alert('invalid username or password');window.location='/login'</script>")


    return render_template("login.html")

@public.route('/advisor_reg',methods=['POST','GET'])
def advisor_reg():
    if 'submit' in request.form:
        name=request.form['name']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        work_exp=request.form['work_exp']
        prof_certi=request.files['prof_certi']
        username=request.form['username']
        password=request.form['password']

        path='static/'+str(uuid.uuid4())+prof_certi.filename
        prof_certi.save(path)

        qry="insert into login values(null,'%s','%s','pending')"%(username,password)
        res=insert(qry)
        qry1="insert into advisor values(null,'%s','%s','%s','%s','%s','%s','%s')"%(res,name,place,phone,email,work_exp,path)
        insert(qry1)
        return ("<script>alert('Registration successfull');window.location='/login'</script>")
    return render_template("advisor_reg.html")



# @public.route('/forgot_password',methods=['POST','GET'])
# def forgot_password():
#     data={}
#     if 'submit' in request.form:
#         email=request.form['email']
#         phone=request.form['phone']
#         qry="select * from clinic where email='%s' and phone='%s'"%(email,phone)
#         res=select(qry)
#         if res:
#             data['view']=res
#         else:
#             qry1="select * from user where email='%s' and phone='%s'"%(email,phone)
#             res1=select(qry1)
#             if res1:
#                 data['view']=res1

#     if 'confirm' in request.form:
#         new_password=request.form['new_password']
#         log_id=request.form['log_id']
#         qry2="update login set password='%s' where login_id='%s'"%(new_password,log_id)
#         update(qry2)
#         return '''<script>alert("password updated successfully");window.location="/login"</script>'''
        

#     return render_template("forgot_password.html",data=data)
