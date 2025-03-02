from flask import *
from database import *

user=Blueprint("user",__name__)

@user.route('/user_home')
def user_home():

    return render_template("user_home.html")

@user.route('/user_product')
def user_product():
    data={}
    a="select * from product"
    b=select(a)
    if b:
        data['view']=b

    return render_template("user_product.html",data=data)