import ssl
from cryptography import x509
from cryptography.hazmat.backends import default_backend

addr = 'www.manche.fr'
pem_data = ssl.get_server_certificate((addr, 443))

#Convertir le certificat du format PEM en object Certificate
cert = x509.load_pem_x509_certificate(str.encode(pem_data), default_backend())

#Affichage des informations du pays du certificat https://cryptography.io/en/latest/x509/reference/
print(cert.subject.get_attributes_for_oid(x509.NameOID.COUNTRY_NAME)[0].value) 

#print(cert.not_valid_before)
print(cert.subject)