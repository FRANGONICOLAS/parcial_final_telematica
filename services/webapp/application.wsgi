import sys
import site
import os

# Agrega la ruta de tu proyecto
sys.path.insert(0, '/var/www/webapp')

# Agrega el virtualenv al path de Python
site.addsitedir('/var/www/webapp/venv/lib/python3.12/site-packages')  # Ajusta versión Python si es necesario

# Configura la variable de entorno de Flask
os.environ['FLASK_APP'] = 'run.py'

# Importa la app Flask
from run import app as application
