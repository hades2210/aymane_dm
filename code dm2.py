import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
import os

########################################################################
#                              CONSTANTES                              #
########################################################################

CLIENTS_CSV = "Clients.csv"
DEVIS_CSV = "Devis.csv"

# Exemple (simplifié) de densités par matière
# Vous pouvez adapter et lier la matière à sa densité
DENSITES = {
    "Acier": 7.85,
    "Aluminium": 2.70,
    "Cuivre": 8.96
}

########################################################################
#                 FONCTIONS DE CALCUL ET DE MANIPULATION CSV           #
########################################################################

def verifier_ou_creer_fichier(nom_fichier, en_tetes):
    """
    Vérifie si le fichier CSV existe, si non, le crée avec les en-têtes spécifiés.
    """
    if not os.path.exists(nom_fichier):
        with open(nom_fichier, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(en_tetes)

def calculer_prix_devis(matiere, longueur, largeur, epaisseur,
                        forme, prix_au_kg, cout_lame, cout_avance, coeff_forme):
    """
    Fonction de calcul du prix de vente d'un devis, inspirée du pseudocode AlgoBox.
    ----------------------------------------------------------------------------
    Vous pouvez modifier la formule pour correspondre à vos besoins exacts.
    """
    try:
        longueur = float(longueur)
        largeur = float(largeur)
        epaisseur = float(epaisseur)
        prix_au_kg = float(prix_au_kg)
        cout_lame = float(cout_lame)
        cout_avance = float(cout_avance)
        coeff_forme = float(coeff_forme)
    except ValueError:
        # Si un champ n'est pas numérique, on renvoie un prix négatif pour signaler l'erreur
        return -1.0

    # Récupération de la densité en fonction de la matière
    if matiere in DENSITES:
        densite = DENSITES[matiere]
    else:
        # Si la matière n'est pas dans le dictionnaire, on prend une densité par défaut
        densite = 1.0

    # Calcul du volume (cm3) -> conversion en kg : densite (g/cm3) => densite * volume / 1000
    volume_cm3 = longueur * largeur * epaisseur
    poids_kg = densite * volume_cm3 / 1000.0

    # Exemple de calcul simplifié
    prix_matiere = poids_kg * prix_au_kg
    prix_main_oeuvre = (cout_lame + cout_avance) * coeff_forme

    # Prix total
    prix_total = prix_matiere + prix_main_oeuvre
    return round(prix_total, 2)


########################################################################
#                          CLASSE APPLICATION                          #
########################################################################

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Outil de Gestion des Clients et Devis")
        self.geometry("900x500")

        # Vérification/Création des fichiers CSV
        verifier_ou_creer_fichier(CLIENTS_CSV,
            ["RAISON_SOCIALE", "ADRESSE", "CODE_POSTAL", "TELEPHONE", "SIRET", "REPRESENTANT_NOM", "REPRESENTANT_PRENOM"]
        )
        verifier_ou_creer_fichier(DEVIS_CSV,
            ["MATIERE", "LONGUEUR", "LARGEUR", "EPAISSEUR", "FORME",
             "PRIX_AU_KG", "COUT_LAME", "COUT_AVANCE", "COEFF_FORME", "PRIX_CALCULE"]
        )

        # Onglets via Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        # Frame pour Clients
        self.frame_clients = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_clients, text="Clients")

        # Frame pour Devis
        self.frame_devis = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_devis, text="Devis")

        # Construction des onglets
        self._build_clients_tab()
        self._build_devis_tab()

    ####################################################################
    #                       ONGLET CLIENTS                             #
    ####################################################################

    def _build_clients_tab(self):
        """Construction de l'onglet 'Clients'."""
        # Éléments de saisie pour les informations du client
        label_raison_sociale = ttk.Label(self.frame_clients, text="Raison Sociale :")
        label_raison_sociale.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_raison_sociale = ttk.Entry(self.frame_clients, width=30)
        self.entry_raison_sociale.grid(row=0, column=1, padx=5, pady=5)

        label_adresse = ttk.Label(self.frame_clients, text="Adresse :")
        label_adresse.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_adresse = ttk.Entry(self.frame_clients, width=30)
        self.entry_adresse.grid(row=1, column=1, padx=5, pady=5)

        label_code_postal = ttk.Label(self.frame_clients, text="Code Postal :")
        label_code_postal.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_code_postal = ttk.Entry(self.frame_clients, width=10)
        self.entry_code_postal.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        label_telephone = ttk.Label(self.frame_clients, text="Téléphone :")
        label_telephone.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_telephone = ttk.Entry(self.frame_clients, width=15)
        self.entry_telephone.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        label_siret = ttk.Label(self.frame_clients, text="SIRET :")
        label_siret.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_siret = ttk.Entry(self.frame_clients, width=20)
        self.entry_siret.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        label_nom_rep = ttk.Label(self.frame_clients, text="Représentant (Nom) :")
        label_nom_rep.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.entry_nom_rep = ttk.Entry(self.frame_clients, width=15)
        self.entry_nom_rep.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        label_prenom_rep = ttk.Label(self.frame_clients, text="Représentant (Prénom) :")
        label_prenom_rep.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.entry_prenom_rep = ttk.Entry(self.frame_clients, width=15)
        self.entry_prenom_rep.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        # Barre de recherche de client
        label_recherche = ttk.Label(self.frame_clients, text="Recherche par Nom :")
        label_recherche.grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.entry_recherche = ttk.Entry(self.frame_clients, width=15)
        self.entry_recherche.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        btn_recherche = ttk.Button(self.frame_clients, text="Rechercher", command=self.rechercher_client)
        btn_recherche.grid(row=7, column=2, padx=5, pady=5)

        # Boutons d'action pour l'onglet client
        btn_nettoyer = ttk.Button(self.frame_clients, text="Nettoyer", command=self.nettoyer_champs_client)
        btn_nettoyer.grid(row=8, column=0, padx=5, pady=10)

        btn_enregistrer = ttk.Button(self.frame_clients, text="Enregistrer", command=self.enregistrer_client)
        btn_enregistrer.grid(row=8, column=1, padx=5, pady=10)

    def nettoyer_champs_client(self):
        """Vide tous les champs de saisie de l'onglet 'Clients'."""
        self.entry_raison_sociale.delete(0, tk.END)
        self.entry_adresse.delete(0, tk.END)
        self.entry_code_postal.delete(0, tk.END)
        self.entry_telephone.delete(0, tk.END)
        self.entry_siret.delete(0, tk.END)
        self.entry_nom_rep.delete(0, tk.END)
        self.entry_prenom_rep.delete(0, tk.END)
        self.entry_recherche.delete(0, tk.END)

    def enregistrer_client(self):
        """
        Récupère les données saisies, les formate et les enregistre dans le fichier CSV des clients.
        Affiche un message de succès ou d'erreur via messagebox.
        """
        raison_sociale = self.entry_raison_sociale.get().upper()
        adresse = self.entry_adresse.get().upper()
        code_postal = self.entry_code_postal.get().upper()
        telephone = self.entry_telephone.get().upper().replace(" ", "")
        siret = self.entry_siret.get().upper()
        rep_nom = self.entry_nom_rep.get().upper()
        rep_prenom = self.entry_prenom_rep.get().upper()

        if not raison_sociale:
            messagebox.showwarning("Attention", "Le champ 'Raison Sociale' est obligatoire.")
            return

        # Ouverture du fichier CSV en mode 'append' pour ajouter la nouvelle ligne
        with open(CLIENTS_CSV, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([
                raison_sociale,
                adresse,
                code_postal,
                telephone,
                siret,
                rep_nom,
                rep_prenom
            ])

        messagebox.showinfo("Succès", f"Le client '{raison_sociale}' a été enregistré.")
        self.nettoyer_champs_client()

    def rechercher_client(self):
        """
        Recherche un client par sa raison sociale ou son nom de représentant dans le fichier CSV.
        """
        recherche = self.entry_recherche.get().strip().upper()
        if not recherche:
            messagebox.showinfo("Info", "Veuillez saisir un nom pour la recherche.")
            return

        trouve = False
        try:
            with open(CLIENTS_CSV, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=';')
                next(reader, None)  # Passer la ligne d'en-tête
                for row in reader:
                    if len(row) >= 7:
                        raison_sociale = row[0].upper()
                        nom_representant = row[5].upper()  # REPRESENTANT_NOM
                        # Recherche dans raison sociale OU nom du représentant
                        if recherche in raison_sociale or recherche in nom_representant:
                            self.nettoyer_champs_client()
                            self.entry_raison_sociale.insert(0, row[0])
                            self.entry_adresse.insert(0, row[1])
                            self.entry_code_postal.insert(0, row[2])
                            self.entry_telephone.insert(0, row[3])
                            self.entry_siret.insert(0, row[4])
                            self.entry_nom_rep.insert(0, row[5])
                            self.entry_prenom_rep.insert(0, row[6])
                            trouve = True
                            break

            if not trouve:
                messagebox.showinfo("Résultat", f"Aucun client trouvé pour : {recherche}")

        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la recherche : {str(e)}")


    ####################################################################
    #                       ONGLET DEVIS                               #
    ####################################################################

    def _build_devis_tab(self):
        """Construction de l'onglet 'Devis'."""
        # Sélection de la matière via Combobox
        label_matiere = ttk.Label(self.frame_devis, text="Matière :")
        label_matiere.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.combo_matiere = ttk.Combobox(
            self.frame_devis, values=list(DENSITES.keys()), state="readonly" # Lecture seule, choix limité aux matières définies
        )
        self.combo_matiere.set("Acier") # Matière par défaut
        self.combo_matiere.grid(row=0, column=1, padx=5, pady=5)

        # Champs de saisie pour les dimensions et coûts
        label_longueur = ttk.Label(self.frame_devis, text="Longueur (mm) :")
        label_longueur.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_longueur = ttk.Entry(self.frame_devis, width=10)
        self.entry_longueur.grid(row=1, column=1, padx=5, pady=5)

        label_largeur = ttk.Label(self.frame_devis, text="Largeur (mm) :")
        label_largeur.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_largeur = ttk.Entry(self.frame_devis, width=10)
        self.entry_largeur.grid(row=2, column=1, padx=5, pady=5)

        label_epaisseur = ttk.Label(self.frame_devis, text="Épaisseur (mm) :")
        label_epaisseur.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_epaisseur = ttk.Entry(self.frame_devis, width=10)
        self.entry_epaisseur.grid(row=3, column=1, padx=5, pady=5)

        label_forme = ttk.Label(self.frame_devis, text="Forme :")
        label_forme.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_forme = ttk.Entry(self.frame_devis, width=15)
        self.entry_forme.insert(0, "Rectangle") # Forme par défaut
        self.entry_forme.grid(row=4, column=1, padx=5, pady=5)

        label_prix_au_kg = ttk.Label(self.frame_devis, text="Prix au kg (€) :")
        label_prix_au_kg.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.entry_prix_au_kg = ttk.Entry(self.frame_devis, width=10)
        self.entry_prix_au_kg.insert(0, "1.0") # Prix par défaut
        self.entry_prix_au_kg.grid(row=5, column=1, padx=5, pady=5)

        label_cout_lame = ttk.Label(self.frame_devis, text="Coût Lame (€) :")
        label_cout_lame.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.entry_cout_lame = ttk.Entry(self.frame_devis, width=10)
        self.entry_cout_lame.insert(0, "1.0") # Coût par défaut
        self.entry_cout_lame.grid(row=6, column=1, padx=5, pady=5)

        label_cout_avance = ttk.Label(self.frame_devis, text="Coût Avance (€) :")
        label_cout_avance.grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.entry_cout_avance = ttk.Entry(self.frame_devis, width=10)
        self.entry_cout_avance.insert(0, "1.0") # Coût par défaut
        self.entry_cout_avance.grid(row=7, column=1, padx=5, pady=5)

        label_coeff_forme = ttk.Label(self.frame_devis, text="Coefficient Forme :")
        label_coeff_forme.grid(row=8, column=0, padx=5, pady=5, sticky="e")
        self.entry_coeff_forme = ttk.Entry(self.frame_devis, width=10)
        self.entry_coeff_forme.insert(0, "1.0") # Coefficient par défaut
        self.entry_coeff_forme.grid(row=8, column=1, padx=5, pady=5)

        # Label pour afficher le prix calculé
        self.label_prix_resultat = ttk.Label(self.frame_devis, text="Prix du Devis : 0.00 €")
        self.label_prix_resultat.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        # Boutons d'action pour l'onglet devis
        btn_calculer = ttk.Button(self.frame_devis, text="Calculer", command=self.calculer_prix)
        btn_calculer.grid(row=10, column=0, padx=5, pady=10)

        btn_nettoyer = ttk.Button(self.frame_devis, text="Nettoyer", command=self.nettoyer_champs_devis)
        btn_nettoyer.grid(row=10, column=1, padx=5, pady=10)

        btn_enregistrer_devis = ttk.Button(self.frame_devis, text="Enregistrer", command=self.enregistrer_devis)
        btn_enregistrer_devis.grid(row=10, column=2, padx=5, pady=10)

    def nettoyer_champs_devis(self):
        """Réinitialise les champs de saisie de l'onglet 'Devis' à leurs valeurs par défaut."""
        self.combo_matiere.set("Acier")
        self.entry_longueur.delete(0, tk.END)
        self.entry_largeur.delete(0, tk.END)
        self.entry_epaisseur.delete(0, tk.END)
        self.entry_forme.delete(0, tk.END)
        self.entry_forme.insert(0, "Rectangle")
        self.entry_prix_au_kg.delete(0, tk.END)
        self.entry_prix_au_kg.insert(0, "1.0")
        self.entry_cout_lame.delete(0, tk.END)
        self.entry_cout_lame.insert(0, "1.0")
        self.entry_cout_avance.delete(0, tk.END)
        self.entry_cout_avance.insert(0, "1.0")
        self.entry_coeff_forme.delete(0, tk.END)
        self.entry_coeff_forme.insert(0, "1.0")
        self.label_prix_resultat.config(text="Prix du Devis : 0.00 €")

    def calculer_prix(self):
        """
        Récupère les valeurs des champs de l'onglet 'Devis', calcule le prix du devis
        en utilisant la fonction 'calculer_prix_devis', et affiche le résultat.
        Gère les erreurs si les champs numériques ne sont pas valides.
        """
        matiere = self.combo_matiere.get()
        longueur = self.entry_longueur.get()
        largeur = self.entry_largeur.get()
        epaisseur = self.entry_epaisseur.get()
        forme = self.entry_forme.get()
        prix_au_kg = self.entry_prix_au_kg.get()
        cout_lame = self.entry_cout_lame.get()
        cout_avance = self.entry_cout_avance.get()
        coeff_forme = self.entry_coeff_forme.get()

        prix = calculer_prix_devis(matiere, longueur, largeur, epaisseur,
                                   forme, prix_au_kg, cout_lame, cout_avance, coeff_forme)
        if prix < 0:
            messagebox.showerror("Erreur", "Les champs doivent être numériques.")
        else:
            self.label_prix_resultat.config(text=f"Prix du Devis : {prix} €")

    def enregistrer_devis(self):
        """
        Calcule le prix du devis et enregistre toutes les informations du devis,
        y compris le prix calculé, dans le fichier CSV des devis.
        Affiche un message de succès ou d'erreur via messagebox.
        """
        matiere = self.combo_matiere.get()
        longueur = self.entry_longueur.get()
        largeur = self.entry_largeur.get()
        epaisseur = self.entry_epaisseur.get()
        forme = self.entry_forme.get()
        prix_au_kg = self.entry_prix_au_kg.get()
        cout_lame = self.entry_cout_lame.get()
        cout_avance = self.entry_cout_avance.get()
        coeff_forme = self.entry_coeff_forme.get()

        # Calcul du prix avant enregistrement
        prix = calculer_prix_devis(matiere, longueur, largeur, epaisseur,
                                   forme, prix_au_kg, cout_lame, cout_avance, coeff_forme)
        if prix < 0:
            messagebox.showerror("Erreur", "Les champs doivent être numériques.")
            return

        # Enregistrement des données du devis dans le fichier CSV
        with open(DEVIS_CSV, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([
                matiere,
                longueur,
                largeur,
                epaisseur,
                forme,
                prix_au_kg,
                cout_lame,
                cout_avance,
                coeff_forme,
                prix
            ])

        messagebox.showinfo("Succès", "Le devis a été enregistré avec succès.")
        self.label_prix_resultat.config(text=f"Prix du Devis : {prix} €")


########################################################################
#                               MAIN                                   #
########################################################################

if __name__ == "__main__":
    app = Application()
    app.mainloop()