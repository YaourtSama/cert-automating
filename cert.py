import OpenSSL
import os
import requests
import ssl
import datetime
url = "www.manche.fr"
# Fonction pour charger le certificat à partir de l'URL donnée
def load_certificate_from_url(url):
    # Récupération du contenu du certificat à partir de l'URL donnée 
    response = ssl.get_server_certificate((url, 443))
    with open('certs/cert.pem', 'wb') as file: 
        file.write(response.content)
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, response.content)

    return cert 


# Fonction pour sauvegarder le certificat au format PEM dans un fichier donné
def save_certificate_to_file(file_name, certificate):
    with open(file_name, 'wb') as file: 
        file.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, certificate))

# Fonction principale 
def main():
    # URL à partir de laquelle le certificat sera téléchargé
    url = "https://www.manche.fr"
    
    # La méthode charge le certificat situé à l'URL donnée à partir d'une variable
    cert = load_certificate_from_url(url)
    
    # Enregistrer le certificat chargé au format PEM dans un fichier 
    #Le chemin sera certs/#Le nom commun du certificat
    save_certificate_to_file('certs/{0}.pem'.format(cert.get_subject().CN), cert)
    
    # Appel de la méthode qui vérifie la date de validité du certificat  
    isValid = check_certificate_validity(cert);

    if(isValid):
        print("Le certificat fourni est valide")
    else:
        print("Le certificat fourni n'est pas valide")

if __name__ == '__main__':
    main()