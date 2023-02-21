from seatable_api import Base
from cert_data import get_cert
import datetime
#Récupérer le token de l'API Seatable et son URL, on les stocke dans un fichier txt appelé tokens.txt 
#ayant pour structure: ligne 1: URL, ligne 2: token

tokens = open('tokens.txt', 'r')
lines = tokens.readlines()

#La commande strip() permet de supprimer les espaces et les sauts de ligne
server = lines[0].strip()
token = lines[1].strip()

#On referme le fichier
tokens.close()

#Création d'un contexte pour l'API Seatable
base = Base(token, server)
base.auth()

#Liste qui contiendra les informations des certificats
infos = []

#On récupère les adresses des sites web à analyser et on les ajoute à la liste addr
addresses = open('addresses.txt', 'r')
date_today = datetime.datetime.today()

#On récupère les informations des certificats et on les ajoute à la liste infos
for line in addresses:
    cert_info = get_cert(line.strip())
    #Comparer la date d'expiration du certificat avec la date du jour
    if cert_info['expiration'] != '00-00-0000':
        if cert_info['expiration'] < date_today:
            cert_info['state'] = 'expired'
        else:
            cert_info['state'] = 'valid'
    
    cert_info['expiration'] = str(cert_info['expiration'])
    infos.append(cert_info)
    print(cert_info)
addresses.close()

#On ajoute les informations des certificats à la table Table1
for i in infos:
    base.append_row('Table1', i)
