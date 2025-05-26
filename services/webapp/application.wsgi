# application.wsgi
import sys
import os

# Activar entorno virtual
venv_path = '/var/www/webapp/venv/bin/activate_this.py'
with open(venv_path) as f:
    exec(f.read(), dict(__file__=venv_path))

# Agrega el directorio del proyecto al PYTHONPATH
sys.path.insert(0, '/var/www/webapp')

# Establece la variable de entorno para Flask
os.environ['FLASK_APP'] = 'run.py'

# Importa la aplicación desde run.py
from run import app as application
