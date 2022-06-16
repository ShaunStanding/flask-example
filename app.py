""" 
create virtual environment: py -m venv <-->
activate virtual environment: <-->/Scripts/activate
deactivate virtual environment: deactivate
delete virtual environment: del <file/path>
"""

""" 
install module: pip install <module>
user log in install: pip install flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator
show modules: pip freeze > requirements.txt
"""
"""  
use:   py app.py   to run/view web app in browser
"""
"""  
/////////////////////////////////////////////////
"""
# import Class from module
# import our views from the views.py file
from views import views
from flask import Flask




#initiate flask app
app = Flask(__name__)


app.register_blueprint(views)


# check flask app is made from a global code space
if __name__ == "__main__":
    app.run(debug=True, port=8000)