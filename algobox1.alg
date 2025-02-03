<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="AFFICHER prix1"/>
    <extension extnom="inactif"/>
    <fonction fctcode="" fctetat="inactif"/>
    <F2 F2para="" F2defaut="" F2lignes="" F2etat="inactif"/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param epaisseurLigne="2" totalBoucles="5000000" nbDecimales="8" totalAffichages="1000" maxBoucle="500000" epaisseurPoint="2" arrondiAuto="vrai"/>
    <item code="200#declarationfonctions" algoitem="FONCTIONS_UTILISEES">
        <item code="201#calculerPrixDevis#matiere, longueur, largeur, epaisseur, forme, prixAuKg, coutLame, coutAvance, coefficientForme" algoitem="FONCTION calculerPrixDevis(matiere, longueur, largeur, epaisseur, forme, prixAuKg, coutLame, coutAvance, coefficientForme)"/>
    </item>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#NOMBRE#volume" algoitem="volume EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#poids" algoitem="poids EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#prixMatiere" algoitem="prixMatiere EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#prixTotal" algoitem="prixTotal EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#densite" algoitem="densite EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#prix1" algoitem="prix1 EST_DU_TYPE NOMBRE"/>
        <item code="1#CHAINE#matiere" algoitem="matiere EST_DU_TYPE CHAINE"/>
        <item code="1#NOMBRE#longueur" algoitem="longueur EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#largeur" algoitem="largeur EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#epaisseur" algoitem="epaisseur EST_DU_TYPE NOMBRE"/>
        <item code="1#CHAINE#forme" algoitem="forme EST_DU_TYPE CHAINE"/>
        <item code="1#NOMBRE#prixAuKg" algoitem="prixAuKg EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#coutLame" algoitem="coutLame EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#coutAvance" algoitem="coutAvance EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#coefficientForme" algoitem="coefficientForme EST_DU_TYPE NOMBRE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="5#matiere#&quot;Acier&quot;#pasliste" algoitem="matiere PREND_LA_VALEUR &quot;Acier&quot;"/>
        <item code="5#longueur#100#pasliste" algoitem="longueur PREND_LA_VALEUR 100"/>
        <item code="5#largeur#100#pasliste" algoitem="largeur PREND_LA_VALEUR 100"/>
        <item code="5#epaisseur#10#pasliste" algoitem="epaisseur PREND_LA_VALEUR 10"/>
        <item code="5#forme#&quot;Rectangle&quot;#pasliste" algoitem="forme PREND_LA_VALEUR &quot;Rectangle&quot;"/>
        <item code="5#prixAuKg#1#pasliste" algoitem="prixAuKg PREND_LA_VALEUR 1"/>
        <item code="5#coutLame#1#pasliste" algoitem="coutLame PREND_LA_VALEUR 1"/>
        <item code="5#coutAvance#1#pasliste" algoitem="coutAvance PREND_LA_VALEUR 1"/>
        <item code="5#coefficientForme#1#pasliste" algoitem="coefficientForme PREND_LA_VALEUR 1"/>
        <item code="5#prix1#calculerPrixDevis(matiere, longueur, largeur, epaisseur, forme, prixAuKg, coutLame, coutAvance, coefficientForme)#pasliste" algoitem="prix1 PREND_LA_VALEUR calculerPrixDevis(matiere, longueur, largeur, epaisseur, forme, prixAuKg, coutLame, coutAvance, coefficientForme)"/>
        <item code="4#Prix du devis 1 : #0" algoitem="AFFICHER &quot;Prix du devis 1 : &quot;"/>
        <item code="3#prix1#0#pasliste" algoitem="AFFICHER prix1"/>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>
