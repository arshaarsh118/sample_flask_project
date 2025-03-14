from flask import *
from public import public
from admin import admin
from user import user

app=Flask(__name__)
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(user)
app.secret_key="gh"


app.run(debug=True)