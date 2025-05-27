import sys
import site
import os

# Agrega la ruta de tu proyecto
sys.path.insert(0, '/var/www/webapp')

# Agrega el virtualenv al path de Python
site.addsitedir('/var/www/webapp/venv/lib/python3.12/site-packages')  # Ajusta versión Python si es necesario

# Activa el virtualenv
activate_env = os.path.expanduser("/var/www/webapp/venv/bin/activate_this.py")
with open(activate_env) as f:
    exec(f.read(), dict(__file__=activate_env))

# Configura la variable de entorno de Flask
os.environ['FLASK_APP'] = 'run.py'

# Importa la app Flask
from run import app as application
