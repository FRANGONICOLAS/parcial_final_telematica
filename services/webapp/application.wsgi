import sys
import os

# Agrega la ruta de tu proyecto
sys.path.insert(0, '/var/www/webapp')

# Configura la variable de entorno de Flask
os.environ['FLASK_APP'] = 'run.py'

# Importa la app Flask
from run import app as application
