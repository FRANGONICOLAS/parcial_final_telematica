FROM ubuntu:latest

# Evita interacción al instalar paquetes
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias
RUN apt-get update && apt-get install -y \
    apache2 \
    libapache2-mod-wsgi-py3 \
    python3 \
    python3-pip \
    openssl

# Habilitar módulos
RUN a2enmod wsgi && a2enmod ssl

# Crear entorno virtual
RUN python3 -m venv /var/www/webapp/venv

# Activar entorno virtual e instalar Flask
RUN /var/www/webapp/venv/bin/pip install flask

# Generar certificado SSL autofirmado
RUN mkdir -p /etc/ssl/private && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/apache-selfsigned.key \
    -out /etc/ssl/certs/apache-selfsigned.crt \
    -subj "/C=CO/ST=VAC/L=Cali/O=HigueraGonzalez/CN=localhost" && \
    chmod 600 /etc/ssl/private/apache-selfsigned.key

# Copiar archivos de la aplicación y configuración Apache
COPY ./webapp /var/www/webapp
COPY ./apache2 /etc/apache2/

# Asignar permisos
RUN chown -R www-data:www-data /var/www/webapp && chmod -R 755 /var/www/webapp

# Exponer puertos
EXPOSE 80 443

# Iniciar Apache en primer plano
CMD ["apache2ctl", "-D", "FOREGROUND"]
