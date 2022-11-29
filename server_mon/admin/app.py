from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

app.config['FLASK_ADMIN_SWATCH'] = 'pavelbeard'

admin = Admin(app, name='iva_dashboard', template_mode='bootstrap3')

admin.add_view(ModelView())

app.run(host='0.0.0.0', port=8003, debug=True)


