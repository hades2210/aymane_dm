<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="AFFICHER PrixFinale"/>
    <extension extnom="inactif"/>
    <fonction fctcode="" fctetat="inactif"/>
    <F2 F2lignes="" F2etat="inactif" F2defaut="" F2para=""/>
    <repere repcode="-10#10#-10#10#2#2" repetat="inactif"/>
    <param maxBoucle="500000" epaisseurPoint="2" totalBoucles="5000000" epaisseurLigne="2" totalAffichages="1000" arrondiAuto="vrai" nbDecimales="8"/>
    <item algoitem="FONCTIONS_UTILISEES" code="200#declarationfonctions">
        <item algoitem="FONCTION CalculPrix(CoutMatiere, CoutLame, FraisFixe, CoefForme)" code="201#CalculPrix#CoutMatiere, CoutLame, FraisFixe, CoefForme">
            <item algoitem="VARIABLES_FONCTION" code="202#declarationsvariablesfonction">
                <item algoitem="prix EST_DU_TYPE NOMBRE" code="1#NOMBRE#prix"/>
            </item>
            <item algoitem="DEBUT_FONCTION" code="203#debutfonction"/>
            <item algoitem="prix PREND_LA_VALEUR (CoutMatiere * 10 + CoutLame * 5) * CoefForme + FraisFixe" code="5#prix#(CoutMatiere * 10 + CoutLame * 5) * CoefForme + FraisFixe#pasliste"/>
            <item algoitem="RENVOYER prix" code="205#prix"/>
            <item algoitem="FIN_FONCTION" code="204#finfonction"/>
        </item>
    </item>
    <item algoitem="VARIABLES" code="100#declarationsvariables">
        <item algoitem="CoutMatiere EST_DU_TYPE NOMBRE" code="1#NOMBRE#CoutMatiere"/>
        <item algoitem="CoutLame EST_DU_TYPE NOMBRE" code="1#NOMBRE#CoutLame"/>
        <item algoitem="FraisFixe EST_DU_TYPE NOMBRE" code="1#NOMBRE#FraisFixe"/>
        <item algoitem="CoefForme EST_DU_TYPE NOMBRE" code="1#NOMBRE#CoefForme"/>
        <item algoitem="PrixFinale EST_DU_TYPE NOMBRE" code="1#NOMBRE#PrixFinale"/>
    </item>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="AFFICHER &quot;Entrez le coût de la matière :&quot;" code="4#Entrez le coût de la matière :#0"/>
        <item algoitem="LIRE CoutMatiere" code="2#CoutMatiere#pasliste"/>
        <item algoitem="AFFICHER &quot;Entrez le coût de la lame :&quot;" code="4#Entrez le coût de la lame :#0"/>
        <item algoitem="LIRE CoutLame" code="2#CoutLame#pasliste"/>
        <item algoitem="AFFICHER &quot;Entrez l'avance (frais fixe) :&quot;" code="4#Entrez l'avance (frais fixe) :#0"/>
        <item algoitem="LIRE FraisFixe" code="2#FraisFixe#pasliste"/>
        <item algoitem="AFFICHER &quot;Entrez le coefficient de forme :&quot;" code="4#Entrez le coefficient de forme :#0"/>
        <item algoitem="LIRE CoefForme" code="2#CoefForme#pasliste"/>
        <item algoitem="PrixFinale PREND_LA_VALEUR CalculPrix(CoutMatiere, CoutLame, FraisFixe, CoefForme)" code="5#PrixFinale#CalculPrix(CoutMatiere, CoutLame, FraisFixe, CoefForme)#pasliste"/>
        <item algoitem="AFFICHER &quot;Le prix de vente pour ce devis est : &quot;" code="4#Le prix de vente pour ce devis est : #0"/>
        <item algoitem="AFFICHER PrixFinale" code="3#PrixFinale#0#pasliste"/>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>
