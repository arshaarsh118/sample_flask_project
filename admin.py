from flask import *
from database import *

admin=Blueprint("admin",__name__)

@admin.route('/admin_home')
def admin_home():

    return render_template("admin_home.html")

@admin.route('/admin_product',methods=['post','get'])
def admin_product():
    if 'submit' in request.form:
        name=request.form['name']
        price=request.form['price']
        stk=request.form['stk']
        
       
        c="insert into product values(null,'%s','%s','%s')"%(name,price,stk)
        d=insert(c)
        if d:
            return'''<script>alert("Menu Item Added Successfully");window.location='/admin_product'</script>'''
        
    data={}
    a="select * from product"
    b=select(a)
    if b:
        data['view']=b

    return render_template("admin_product.html",data=data)