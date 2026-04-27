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
class BienImmobilier:
    def __init__(self, id_bien, adresse, surface, prix, statut="disponible"):
        self.id_bien = id_bien
        self.adresse = adresse
        self.surface = surface  
        self.prix = prix
        self.statut = statut  
        self.description = ""
        self.photos_vendeur = []  
        self.photos_locataire = []  
    def ajouter_photo_vendeur(self, photo, coordonnees, prix, superficie):
        """Ajoute une photo pour le vendeur avec ses coordonnées."""
        self.photos_vendeur.append({
            'photo': photo, 
            'coordonnees': coordonnees, 
            'prix': prix, 
            'superficie': superficie
        })
    def ajouter_photo_locataire(self, photo, coordonnees, prix, superficie):
        """Ajoute une photo pour le locataire avec ses coordonnées."""
        self.photos_locataire.append({
            'photo': photo, 
            'coordonnees': coordonnees, 
            'prix': prix, 
            'superficie': superficie
        })
    def __str__(self):
        return f"{self.id_bien} - {self.type_bien} à {self.adresse} ({self.surface}m²) - {self.prix}Dh - {self.statut}"
class Appartement(BienImmobilier):
    def __init__(self, id_bien, adresse, surface, prix, statut="disponible"):
        super().__init__(id_bien, adresse, surface, prix, statut)
        self.type_bien = "Appartement"
class Magasin(BienImmobilier):
    def __init__(self, id_bien, adresse, surface, prix, statut="disponible"):
        super().__init__(id_bien, adresse, surface, prix, statut)
        self.type_bien = "Magasin"
class Terrain(BienImmobilier):
    def __init__(self, id_bien, adresse, surface, prix, statut="disponible"):
        super().__init__(id_bien, adresse, surface, prix, statut)
        self.type_bien = "Terrain"
class Maison(BienImmobilier):
    def __init__(self, id_bien, adresse, surface, prix, statut="disponible"):
        super().__init__(id_bien, adresse, surface, prix, statut)
        self.type_bien = "Maison"
class FiltreRecherche:
    def __init__(self):
        # Filtres de base
        self.type_bien: List[TypeBien] = []
        self.type_transaction: Optional[TypeTransaction] = None
        self.prix_min: Optional[float] = None
        self.prix_max: Optional[float] = None
        self.surface_min: Optional[float] = None
        self.surface_max: Optional[float] = None
        self.nb_pieces_min: Optional[int] = None
        self.nb_pieces_max: Optional[int] = None
        self.nb_chambres_min: Optional[int] = None
        self.localisation: Optional[str] = None
        self.rayon_km: Optional[float] = None  # Rayon de recherche autour d'un point
        # Filtres avancés
        self.prix_au_m2_min: Optional[float] = None
        self.prix_au_m2_max: Optional[float] = None
        self.annee_min: Optional[int] = None
        self.annee_max: Optional[int] = None
        self.energie_classe_min: Optional[str] = None  # A, B, C...
        self.energie_classe_max: Optional[str] = None
        # Équipements (booléens)
        self.jardin: Optional[bool] = None
        self.piscine: Optional[bool] = None
        self.garage: Optional[bool] = None
        self.ascenseur: Optional[bool] = None
        self.balcon: Optional[bool] = None
        self.meuble: Optional[bool] = None
        # Statut
        self.statuts: List[StatutBien] = []
        # Tri
        self.trier_par: str = "date_publication"  # prix, surface, date, prix_au_m2
        self.ordre_descendant: bool = True
        # Point de référence pour recherche par rayon
        self.point_reference: Optional[Coordonnees] = None        
