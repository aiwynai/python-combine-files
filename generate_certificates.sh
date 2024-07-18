#!/bin/bash

openssl genrsa -out private_key.pem 2048
openssl req -new -key private_key.pem -out certificate.csr
openssl x509 -req -days 365 -in certificate.csr -signkey private_key.pem -out certificate.crt
openssl pkcs12 -export -out certificate.pfx -inkey private_key.pem -in certificate.crt
