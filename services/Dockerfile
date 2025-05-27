FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    apache2 \
    libapache2-mod-wsgi-py3 \
    python3 \
    python3-pip \
    python3-venv \
    openssl

# Crear entorno virtual
RUN python3 -m venv /var/www/webapp/venv

# Instalar Flask y Flask_SQLAlchemy dentro del entorno virtual
RUN /var/www/webapp/venv/bin/pip install --upgrade pip
RUN /var/www/webapp/venv/bin/pip install flask flask_sqlalchemy
RUN /var/www/webapp/venv/bin/pip install pymysql


# Habilitar módulos de Apache
RUN a2enmod wsgi ssl proxy proxy_http headers

# Generar certificado SSL autofirmado
RUN mkdir -p /etc/ssl/private && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/apache-selfsigned.key \
    -out /etc/ssl/certs/apache-selfsigned.crt \
    -subj "/C=CO/ST=VAC/L=Cali/O=HigueraGonzalez/CN=localhost" && \
    chmod 600 /etc/ssl/private/apache-selfsigned.key

# Copiar la aplicación y configuración de Apache
COPY ./webapp /var/www/webapp
COPY ./apache2 /etc/apache2/

# Cambiar propietario y permisos
RUN chown -R www-data:www-data /var/www/webapp && chmod -R 755 /var/www/webapp

# Exponer puertos HTTP y HTTPS
EXPOSE 80 443

CMD ["apache2ctl", "-D", "FOREGROUND"]
