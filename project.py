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
        self.achetuer = []
        self.vendeur = [] 
        self.locataire = []
    
    ###la partie de lajout des personnes
    def ajouter_vendeur(self, nom, prenom, telephone, email):
        id_personne = len(self.vendeur) + 1
        vendeur = personne(id_personne, nom, prenom, telephone, email, "vendeur")
        self.vendeur.append(vendeur)
        print(f"Vendeur a etait ajoute avec succes : {vendeur}")
    
    def ajouter_acheteur(self, nom, prenom, telephone, email):
        id_personne = len(self.achetuer) + 1
        acheteur = personne(id_personne, nom, prenom, telephone, email, "acheteur")
        self.achetuer.append(acheteur)
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
        for acheteur in self.achetuer:
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
        else:
            print(" Personne non trouvée")
    ######## la partie de la suppression des personnes
    def suppr(self, c, i=None):  
        if i is None: 
            exec(f"{c}.clear()") if c != 'tous' else [x.clear() for x in [v,l,a]]
        else: 
            exec(f"{c}.pop({i})")
        print(f" {'tous' if i is None else c} supprimé(s)")
