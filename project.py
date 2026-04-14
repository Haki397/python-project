class personne :
    def __init__(self, id_personne, nom, prenom, telephone, email, type_personne):
        self.id = id_personne
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email
        self.type_personne = type_personne
    def __str__(self):
        return f"[{self.id}] {self.prenom} {self.nom} - {self.type_personne}"
class GestionImmoblier :
    def __init__(self, acheteure, vendeur, locataire):
        self.acheteur=[]
        self.vendeur = [] 
        self.locataire = [] 
    ###la partie de lajout des personnes
    def ajouter_vendeur(self, nom, prenom, telephone, email):
        id_personne = len(self.vendeur) + 1
        vendeur = personne(id_personne, nom, prenom, telephone, email, "vendeur")
        self.vendeur.append(vendeur)
        print(f"Vendeur a etait ajoute avec succes : {vendeur}")
    def ajouter_acheteur(self, nom, prenom, telephone, email):
        id_personne = len(self.acheteur) + 1
        acheteur = personne(id_personne, nom, prenom, telephone, email, "acheteur")
        self.acheteur.append(acheteur)
        print(f"Acheteur a etait ajoute avec succes : {acheteur}")

    def ajouter_locataire(self, nom, prenom, telephone, email):
        id_personne = len(self.locataire) + 1
        locataire = personne(id_personne, nom, prenom, telephone, email, "locataire")
        self.locataire.append(locataire)
        print(f"Locataire a etait ajoute avec succes : {locataire}")
    def afficher_tous(self):
        print("Liste des vendeurs :")
        for vendeur in self.vendeur:
            print(vendeur)
        print("\nListe des acheteurs :")
        for acheteur in self.acheteur:
            print(acheteur)
        print("\nListe des locataires :")
        for locataire in self.locataire:
            print(locataire)
    ######## la partie de la modification des personnes 
    def modifier(self, index, type_recherche, nom=None, prenom=None, tel=None):
        if 0 <= index < len(personne) and personne[index].type_personne == type_recherche:
            t, n, p, te = personne[index], personne[index].nom, personne[index].prenom, personne[index].telephone
            personne[index] = personne(t, nom or n, prenom or p, tel or te, personne[index].email, personne[index].type_personne)
            print(f"{type_recherche} modifié")
    ######## la partie de la suppression des personnes
    def suppr(self, c, i=None):  
        if i is None: 
            exec(f"{c}.clear()") if c != 'tous' else [x.clear() for x in [v,l,a]]
        else: 
            exec(f"{c}.pop({i})")
        print(f" {'tous' if i is None else c} supprimé(s)")
        #### la partie de la class de lappartement, magasin et terrain
class Appartement:
    def __init__(self, id_appartement , adresse, superficie, prix):
        self.id = id_appartement
        self.adresse = adresse
        self.superficie = superficie
        self.prix = prix
        self.photos_vendeur = []  # Liste des photos pour le vendeur avec coordonnées
        self.photos_locataire = []  # Liste des photos pour le locataire avec coordonnées
    def ajouter_photo_vendeur(self, photo, coordonnees , prix, superficie,):
        """Ajoute une photo pour le vendeur avec ses coordonnées."""
        self.photos_vendeur.append({'photo': photo, 'coordonnees': coordonnees, 'prix': prix, 'superficie': superficie})
    
    def ajouter_photo_locataire(self, photo, coordonnees, prix, superficie):
        """Ajoute une photo pour le locataire avec ses coordonnées."""
        self.photos_locataire.append({'photo': photo, 'coordonnees': coordonnees, 'prix': prix, 'superficie': superficie})
class Magasin:
    def __init__(self, id_magasin):
        self.id = id_magasin
        self.photos_vendeur = []  
        self.photos_locataire = []  
    def ajouter_photo_vendeur(self, photo, coordonnees, prix, superficie):
        """Ajoute une photo pour le vendeur avec ses coordonnées."""
        self.photos_vendeur.append({'photo': photo, 'coordonnees': coordonnees, 'prix': prix, 'superficie': superficie})
    def ajouter_photo_locataire(self, photo, coordonnees, prix, superficie):
        """Ajoute une photo pour le locataire avec ses coordonnées."""
        self.photos_locataire.append({'photo': photo, 'coordonnees': coordonnees, 'prix': prix, 'superficie': superficie})
class Terrain:
    def __init__(self, id_terrain):
        self.id = id_terrain
        self.photos_vendeur = [] 
        self.photos_locataire = [] 
    def ajouter_photo_vendeur(self, photo, coordonnees, prix, superficie):
        """Ajoute une photo pour le vendeur avec ses coordonnées."""
        self.photos_vendeur.append({'photo': photo, 'coordonnees': coordonnees, 'prix': prix, 'superficie': superficie})
    def ajouter_photo_locataire(self, photo, coordonnees, prix, superficie):
        """Ajoute une photo pour le locataire avec ses coordonnées."""
        self.photos_locataire.append({'photo': photo, 'coordonnees': coordonnees, 'prix': prix, 'superficie': superficie}) 
class BienImmobilier:
    def __init__(self, id_bien, adresse, type_bien, surface, prix, statut="disponible"):
        self.id_bien = id_bien
        self.adresse = adresse
        self.type_bien = type_bien  
        self.surface = surface  
        self.prix = prix
        self.statut = statut  
        self.description = ""
    def __str__(self):
        return f"{self.id_bien} - {self.type_bien} à {self.adresse} ({self.surface}m²) - {self.prix}Dh - {self.statut}"