def saluer(nom: str) -> str:
    return f"Bienvenue dans l'atelier GL, {nom} !"

if __name__ == "__main__":
    nom = input("Votre nom : ")
    print(saluer(nom))