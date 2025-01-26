from flask import *
from public import *
from admin import *
from advisor import *



app=Flask(__name__)

app.secret_key='secret_key'

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(advisor)


app.run(debug=True,host='0.0.0.0',port=5009)