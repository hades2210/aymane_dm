<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="AFFICHER prix1" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2defaut="" F2lignes="" F2para="" F2etat="inactif"/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param epaisseurPoint="2" maxBoucle="500000" arrondiAuto="vrai" totalAffichages="1000" epaisseurLigne="2" nbDecimales="8" totalBoucles="5000000"/>
    <item algoitem="FONCTIONS_UTILISEES" code="200#declarationfonctions">
        <item algoitem="FONCTION calculerPrixDevis(matiere, longueur, largeur, epaisseur, forme, prixAuKg, coutLame, coutAvance, coefficientForme)" code="201#calculerPrixDevis#matiere, longueur, largeur, epaisseur, forme, prixAuKg, coutLame, coutAvance, coefficientForme"/>
    </item>
    <item algoitem="VARIABLES" code="100#declarationsvariables">
        <item algoitem="volume EST_DU_TYPE NOMBRE" code="1#NOMBRE#volume"/>
        <item algoitem="poids EST_DU_TYPE NOMBRE" code="1#NOMBRE#poids"/>
        <item algoitem="prixMatiere EST_DU_TYPE NOMBRE" code="1#NOMBRE#prixMatiere"/>
        <item algoitem="prixTotal EST_DU_TYPE NOMBRE" code="1#NOMBRE#prixTotal"/>
        <item algoitem="densite EST_DU_TYPE NOMBRE" code="1#NOMBRE#densite"/>
        <item algoitem="prix1 EST_DU_TYPE NOMBRE" code="1#NOMBRE#prix1"/>
        <item algoitem="matiere EST_DU_TYPE CHAINE" code="1#CHAINE#matiere"/>
        <item algoitem="longueur EST_DU_TYPE NOMBRE" code="1#NOMBRE#longueur"/>
        <item algoitem="largeur EST_DU_TYPE NOMBRE" code="1#NOMBRE#largeur"/>
        <item algoitem="epaisseur EST_DU_TYPE NOMBRE" code="1#NOMBRE#epaisseur"/>
        <item algoitem="forme EST_DU_TYPE CHAINE" code="1#CHAINE#forme"/>
        <item algoitem="prixAuKg EST_DU_TYPE NOMBRE" code="1#NOMBRE#prixAuKg"/>
        <item algoitem="coutLame EST_DU_TYPE NOMBRE" code="1#NOMBRE#coutLame"/>
        <item algoitem="coutAvance EST_DU_TYPE NOMBRE" code="1#NOMBRE#coutAvance"/>
        <item algoitem="coefficientForme EST_DU_TYPE NOMBRE" code="1#NOMBRE#coefficientForme"/>
    </item>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="matiere PREND_LA_VALEUR &quot;Acier&quot;" code="5#matiere#&quot;Acier&quot;#pasliste"/>
        <item algoitem="longueur PREND_LA_VALEUR 100" code="5#longueur#100#pasliste"/>
        <item algoitem="largeur PREND_LA_VALEUR 100" code="5#largeur#100#pasliste"/>
        <item algoitem="epaisseur PREND_LA_VALEUR 10" code="5#epaisseur#10#pasliste"/>
        <item algoitem="forme PREND_LA_VALEUR &quot;Rectangle&quot;" code="5#forme#&quot;Rectangle&quot;#pasliste"/>
        <item algoitem="prixAuKg PREND_LA_VALEUR 1" code="5#prixAuKg#1#pasliste"/>
        <item algoitem="coutLame PREND_LA_VALEUR 1" code="5#coutLame#1#pasliste"/>
        <item algoitem="coutAvance PREND_LA_VALEUR 1" code="5#coutAvance#1#pasliste"/>
        <item algoitem="coefficientForme PREND_LA_VALEUR 1" code="5#coefficientForme#1#pasliste"/>
        <item algoitem="prix1 PREND_LA_VALEUR calculerPrixDevis(matiere, longueur, largeur, epaisseur, forme, prixAuKg, coutLame, coutAvance, coefficientForme)" code="5#prix1#calculerPrixDevis(matiere, longueur, largeur, epaisseur, forme, prixAuKg, coutLame, coutAvance, coefficientForme)#pasliste"/>
        <item algoitem="AFFICHER &quot;Prix du devis 1 : &quot;" code="4#Prix du devis 1 : #0"/>
        <item algoitem="AFFICHER prix1" code="3#prix1#0#pasliste"/>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>
