from flask import *
from database import *

public=Blueprint("public",__name__)

@public.route('/')
def home():

    return render_template("home.html")

@public.route('/login',methods=['post','get'])
def login():
    if 'submit' in request.form:
        uname=request.form['uname']
        pwd=request.form['pwd']
        a="select * from login where username='%s' and  password='%s'"%(uname,pwd)
        b=select(a)
        if b:
            session['log']=b[0]['login_id']
            if b[0]['usertype'] == 'admin':
                return redirect(url_for('admin.admin_home'))
            if b[0]['usertype'] == 'user':
                return redirect(url_for('user.user_home'))
    
    return render_template("login.html")

@public.route('/user',methods=['post','get'])
def user():
    if 'submit' in request.form:
        uname=request.form['uname']
        pwd=request.form['pwd']
        name=request.form['name']
        plc=request.form['place']
        phn=request.form['phone']
        email=request.form['email']
        a="insert into login values(null,'%s','%s','user')"%(uname,pwd)
        b=insert(a)
        c="insert into user values(null,'%s','%s','%s','%s','%s')"%(b,name,plc,phn,email)
        d=insert(c)
        if d:
            return'''<script>alert("Account Created Successfully");window.location='/login'</script>'''

    return render_template("user.html")

