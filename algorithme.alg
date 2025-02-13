<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="AFFICHER PrixFinale"/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2lignes="" F2para="" F2etat="inactif" F2defaut=""/>
    <repere repcode="-10#10#-10#10#2#2" repetat="inactif"/>
    <param arrondiAuto="vrai" epaisseurPoint="2" totalBoucles="5000000" nbDecimales="8" epaisseurLigne="2" maxBoucle="500000" totalAffichages="1000"/>
    <item algoitem="FONCTIONS_UTILISEES" code="200#declarationfonctions">
        <item algoitem="FONCTION CalculPrix(longueur, largeur, epaisseur, densite, prix_au_kg, cout_lame, cout_avance, coeff_forme)" code="201#CalculPrix#longueur, largeur, epaisseur, densite, prix_au_kg, cout_lame, cout_avance, coeff_forme">
            <item algoitem="VARIABLES_FONCTION" code="202#declarationsvariablesfonction">
                <item algoitem="volume_cm3 EST_DU_TYPE NOMBRE" code="1#NOMBRE#volume_cm3"/>
                <item algoitem="poids_kg EST_DU_TYPE NOMBRE" code="1#NOMBRE#poids_kg"/>
                <item algoitem="prix_matiere EST_DU_TYPE NOMBRE" code="1#NOMBRE#prix_matiere"/>
                <item algoitem="prix_main_oeuvre EST_DU_TYPE NOMBRE" code="1#NOMBRE#prix_main_oeuvre"/>
                <item algoitem="prix_total EST_DU_TYPE NOMBRE" code="1#NOMBRE#prix_total"/>
            </item>
            <item algoitem="DEBUT_FONCTION" code="203#debutfonction"/>
            <item algoitem="volume_cm3 PREND_LA_VALEUR longueur * largeur * epaisseur" code="5#volume_cm3#longueur * largeur * epaisseur#pasliste"/>
            <item algoitem="poids_kg PREND_LA_VALEUR densite * volume_cm3 / 1000.0" code="5#poids_kg#densite * volume_cm3 / 1000.0#pasliste"/>
            <item algoitem="prix_matiere PREND_LA_VALEUR poids_kg * prix_au_kg" code="5#prix_matiere#poids_kg * prix_au_kg#pasliste"/>
            <item algoitem="prix_main_oeuvre PREND_LA_VALEUR (cout_lame + cout_avance) * coeff_forme" code="5#prix_main_oeuvre#(cout_lame + cout_avance) * coeff_forme#pasliste"/>
            <item algoitem="prix_total PREND_LA_VALEUR prix_matiere + prix_main_oeuvre" code="5#prix_total#prix_matiere + prix_main_oeuvre#pasliste"/>
            <item algoitem="RENVOYER prix_total" code="205#prix_total"/>
            <item algoitem="FIN_FONCTION" code="204#finfonction"/>
        </item>
    </item>
    <item algoitem="VARIABLES" code="100#declarationsvariables">
        <item algoitem="longueur EST_DU_TYPE NOMBRE" code="1#NOMBRE#longueur"/>
        <item algoitem="largeur EST_DU_TYPE NOMBRE" code="1#NOMBRE#largeur"/>
        <item algoitem="epaisseur EST_DU_TYPE NOMBRE" code="1#NOMBRE#epaisseur"/>
        <item algoitem="densite EST_DU_TYPE NOMBRE" code="1#NOMBRE#densite"/>
        <item algoitem="prix_au_kg EST_DU_TYPE NOMBRE" code="1#NOMBRE#prix_au_kg"/>
        <item algoitem="cout_lame EST_DU_TYPE NOMBRE" code="1#NOMBRE#cout_lame"/>
        <item algoitem="cout_avance EST_DU_TYPE NOMBRE" code="1#NOMBRE#cout_avance"/>
        <item algoitem="coeff_forme EST_DU_TYPE NOMBRE" code="1#NOMBRE#coeff_forme"/>
        <item algoitem="PrixFinale EST_DU_TYPE NOMBRE" code="1#NOMBRE#PrixFinale"/>
    </item>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="AFFICHER &quot;Entrez la longueur (en cm) :&quot;" code="4#Entrez la longueur (en cm) :#0"/>
        <item algoitem="LIRE longueur" code="2#longueur#pasliste"/>
        <item algoitem="AFFICHER &quot;Entrez la largeur (en cm) :&quot;" code="4#Entrez la largeur (en cm) :#0"/>
        <item algoitem="LIRE largeur" code="2#largeur#pasliste"/>
        <item algoitem="AFFICHER &quot;Entrez l'épaisseur (en cm) :&quot;" code="4#Entrez l'épaisseur (en cm) :#0"/>
        <item algoitem="LIRE epaisseur" code="2#epaisseur#pasliste"/>
        <item algoitem="AFFICHER &quot;Entrez la densité (en g/cm3) :&quot;" code="4#Entrez la densité (en g/cm3) :#0"/>
        <item algoitem="LIRE densite" code="2#densite#pasliste"/>
        <item algoitem="AFFICHER &quot;Entrez le prix au kg :&quot;" code="4#Entrez le prix au kg :#0"/>
        <item algoitem="LIRE prix_au_kg" code="2#prix_au_kg#pasliste"/>
        <item algoitem="AFFICHER &quot;Entrez le coût de la lame :&quot;" code="4#Entrez le coût de la lame :#0"/>
        <item algoitem="LIRE cout_lame" code="2#cout_lame#pasliste"/>
        <item algoitem="AFFICHER &quot;Entrez le coût d'avance :&quot;" code="4#Entrez le coût d'avance :#0"/>
        <item algoitem="LIRE cout_avance" code="2#cout_avance#pasliste"/>
        <item algoitem="AFFICHER &quot;Entrez le coefficient de forme :&quot;" code="4#Entrez le coefficient de forme :#0"/>
        <item algoitem="LIRE coeff_forme" code="2#coeff_forme#pasliste"/>
        <item algoitem="PrixFinale PREND_LA_VALEUR CalculPrix(longueur, largeur, epaisseur, densite, prix_au_kg, cout_lame, cout_avance, coeff_forme)" code="5#PrixFinale#CalculPrix(longueur, largeur, epaisseur, densite, prix_au_kg, cout_lame, cout_avance, coeff_forme)#pasliste"/>
        <item algoitem="AFFICHER &quot;Le prix total est :&quot;" code="4#Le prix total est :#0"/>
        <item algoitem="AFFICHER PrixFinale" code="3#PrixFinale#0#pasliste"/>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>
