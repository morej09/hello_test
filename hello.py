# Demander le nom de l'utilisateur
nom = input("Quel est votre nom ? ")

# Demander l'âge de l'utilisateur
age = int(input("Quel est votre âge ? "))

# Calculer l'année de naissance
annee_naissance = 2023 - age

# Afficher un message personnalisé
print(f"Bonjour {nom} ! Vous êtes né en {annee_naissance}.")

# Vérifier si l'utilisateur est majeur
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")

# Afficher le carré de l'âge
carre_age = age ** 2
print(f"Le carré de votre âge est {carre_age}.")
