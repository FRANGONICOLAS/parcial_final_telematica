#application.wsgi
import sys
import os

# Agrega el directorio del proyecto al PYTHONPATH
sys.path.insert(0, '/var/www/webapp')

# Establece la variable de entorno para Flask
os.environ['FLASK_APP'] = 'run.py'

# Importa la aplicación desde run.py
from run import app as application
