#!/bin/bash

# Install system
sudo apt-get install docker.io nginx git -y

# Install certbot
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo snap set certbot trust-plugin-with-root=ok

# Install certificat
sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d xtraorbitals.xyz -d *.xtraorbitals.xyz --manual --preferred-challenges dns-01 certonly

# For renew
#certbot renew


# Get Jupyter examples
sudo mkdir /opt/share/quantum_lab

# Get Nginx conf
## sites-available && sites-enabled
## Reload conf
sudo systemctl reload nginx
