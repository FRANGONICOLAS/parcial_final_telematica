# Start from a different base image
FROM ubuntu:latest

# Install Apache, mod_wsgi, and OpenSSL
RUN apt-get update && apt-get install -y apache2 libapache2-mod-wsgi-py3 openssl

# Enable mod_wsgi
RUN a2enmod wsgi

# Enable ssl
RUN a2enmod ssl

# Generate self-signed SSL certificates
RUN mkdir -p /etc/ssl/private && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/apache-selfsigned.key \
    -out /etc/ssl/certs/apache-selfsigned.crt \
    -subj "/C=CO/ST=VAC/L=Cali/O=HigueraGonzalez/CN=localhost" && \
    chmod 600 /etc/ssl/private/apache-selfsigned.key

# Copy the web application files
COPY ./webapp /var/www/webapp

# Set permissions for the webapp directory
RUN chown -R www-data:www-data /var/www/webapp && \
    chmod -R 755 /var/www/webapp

# Copy Apache2 files
COPY ./apache2 /etc/apache2/

# Expose ports
EXPOSE 80 443

CMD ["service", "apache2", "restart"]
# Start Apache
CMD ["apache2ctl", "-D", "FOREGROUND"]
