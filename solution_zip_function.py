# creer une liste contacts vide
# ouvrir le fichier email.txt en lecture
# lire la premiere ligne en applicant strip et split
# vous avez ainsi une liste contenant les headers
# lire les lignes suivantes en applicant la fonction zip ( header, line)
# faire un append dans votre liste contacts vide du resultat de la fonction zip
# afficher le resultat au format
# email: <value>  --  lastname ,  firstname
# utiliser l'outil python console pour mettre au point votre structure de donnees

contacts = []
with open('email.txt') as file:
    header = file.readline().strip().split(',')
    for line  in file:
        line = line.strip().split(',')
        contact_map = zip(header, line)
        contacts.append(dict(contact_map))

print(contacts)
for contact in contacts:
    print("email: {email} -- {last}, {first}".format(**contact))


