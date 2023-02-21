import ssl
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import datetime

def get_cert(addr):

    #On crée un dictionnaire qui contiendra les informations des certificats
    infos_cert = {}

    infos_cert['host'] = addr

    try:
        #Récupération du certificat au format PEM
        pem_data = ssl.get_server_certificate((addr, 443))

        #Convertir le certificat du format PEM en object Certificate
        cert = x509.load_pem_x509_certificate(str.encode(pem_data), default_backend())

        #Affichage des informations du certificat https://cryptography.io/en/latest/x509/reference/
        infos_cert['cn'] = cert.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value
        infos_cert['expiration'] = cert.not_valid_after
        infos_cert['serial'] = str(cert.serial_number)
        infos_cert['issuer'] = cert.issuer.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value

    except TimeoutError:
        infos_cert['cn'] = 'TimeoutError'
        infos_cert['expiration'] = '00-00-0000'
        infos_cert['serial'] = 'TimeoutError'
        infos_cert['issuer'] = 'TimeoutError'
        infos_cert['state'] = 'TimeoutError'

    
    
    return infos_cert

#print(get_cert('www.manche.fr'))