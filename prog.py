import random

# testée : renvoie une liste de listes contenant les coordonnées des bonus 
def init_bonus():
    bonus = []
    cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
    cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
    cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
    cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]
    for i in range(15):
        bonus.append([])
        for j in range(15):
            l = [i,j]
            if l in cases_MT:
                bonus[i].append("MT")
            elif l in cases_MD:
                bonus[i].append("MD")
            elif l in cases_LT:
                bonus[i].append("LT")
            elif l in cases_LD:
                bonus[i].append("LD")
            else:
                bonus[i].append("  ")
    return bonus

# testée : initialise les jetons sur le plateau (ici aucun)
def init_jetons():
    jetons = []
    for i in range(15):
        jetons.append([])
        for j in range(15):
            jetons[i].append("  ")
    return jetons

# testée : affiche le plateau dans la console avec les jetons joués reçu en paramètre
def affiche_jetons(j): # on imagine que j est une liste de 3-uplets (j = [[lettre,i,j]...])
    jetons = init_jetons()
    bonus = init_bonus()
    for k in range(len(j)):
        lettre = j[k][0]
        ligne = j[k][1]
        colonne = j[k][2]
        jetons[ligne][colonne] = lettre
    for line in range(15):
        for col in range(15):
            if jetons[line][col] == "  ":
                if bonus[line][col] == "MT":
                    print('$$', end = '') 
                elif bonus[line][col] == "MD":
                    print('**', end = '')
                elif bonus[line][col] == "LT":
                    print('33', end = '')
                elif bonus[line][col] == "LD":
                    print('22', end = '')
                else:
                    print("  ", end = '')
            else:
                if bonus[line][col] == "MT":
                    print(jetons[line][col], end = '$')
                elif bonus[line][col] == "MD":
                    print(jetons[line][col], end = '*')
                elif bonus[line][col] == "LT":
                    print(jetons[line][col], end = '3')
                elif bonus[line][col] == "LD":
                    print(jetons[line][col], end = '2')
                else:
                    print(jetons[line][col], end = ' ')
            if (col<14):
                print('||', end='')
        print()
        for col in range(15):
            print("--", end = '')
            if col<14:
                print("||", end = '') # séparation des colonnes par || et des lignes par -- pour essayer de former un carré
        print()

# testée : renvoie le dico de tous les jetons avec leurs occurrences et leurs valeurs
def init_dico():
    dico = {'A': {'occ': 9, 'val': 1}, 'B': {'occ': 2, 'val': 3}, 'C': {'occ': 2, 'val': 3}, 'D': {'occ': 3, 'val': 2}, 'E': {'occ': 15, 'val': 1}, 'F': {'occ': 2, 'val': 4}, 'G': {'occ': 2, 'val': 2}, 'H': {'occ': 2, 'val': 4}, 'I': {'occ': 8, 'val': 1}, 'J': {'occ': 1, 'val': 8}, 'K': {'occ': 1, 'val': 10}, 'L': {'occ': 5, 'val': 1}, 'M': {'occ': 3, 'val': 2}, 'N': {'occ': 6, 'val': 1}, 'O': {'occ': 6, 'val': 1}, 'P': {'occ': 2, 'val': 3}, 'Q': {'occ': 1, 'val': 8}, 'R': {'occ': 6, 'val': 1}, 'S': {'occ': 6, 'val': 1}, 'T': {'occ': 6, 'val': 1}, 'U': {'occ': 6, 'val': 1}, 'V': {'occ': 2, 'val': 4}, 'W': {'occ': 1, 'val': 10}, 'X': {'occ': 1, 'val': 10}, 'Y': {'occ': 1, 'val': 10}, 'Z': {'occ': 1, 'val': 10}, '?': {'occ': 2, 'val': 0}}
    return dico

# Méthode pour faire le dictionnaire rapidement :
# lettre = 'A'
# dico = {}
# for i in range(26):
#     print(lettre)
#     dico[lettre] = {'occ':' ','val':' '}
#     dico[lettre]['occ'] = int(input("occurrence : "))
#     dico[lettre]['val'] = int(input("valeur : "))
#     lettre = chr(ord(lettre)+1)
# print(dico)

# testée : reçoit en paramètre le dictionnaire de la fonction précédente et renvoie une liste des clé du dictionnaire c'est-à-dire des jetons le nombres qu'ils doivent apparaître
def init_pioche(dico):
    alphab = list(dico.keys()) # on récupère la liste des clés du dictionnaire
    sac = []
    for e in alphab: # e prends la valeur de chaque clé
        for i in range(dico[e]['occ']): # boucle pour ajouter le jetons dans la liste autant de fois que son occurrence
            sac.append(e)
    return sac

# testée : reçoit en paramètre le nombre de jetons x à prendre dans le sac qui est la liste des jetons et renvoie la main d'un joueur ainsi créée
def piocher(x,sac):
    main = []
    for i in range(x):
        indice = random.randint(0,len(sac)-1) # on choisit un indice au hasard dans le sac
        main.append(sac[indice]) # on ajoute ce jeton à la main
        sac.pop(indice) # on le supprime de la liste sac
    return main

# testée : reçoit en paramètre la main du joueur et le sac sous forme de liste et complète la main si elle ne contient pas 7 jetons et si c'est possible
def completer_main(main,sac):
    x = 7 - len(main) # on définit le nombre de jetons à piocher
    if len(sac) >= x: # si c'est possible on complète
        pioche = piocher(x,sac)
    else: # sinon on complète juste avec ce qu'il reste
        pioche = piocher(len(sac),sac)
    for i in range(len(pioche)): # on rajoute ce qu'on a pioché à la main
        main.append(pioche[i])

# testée : reçoit en paramètre la liste de jetons que le joueur veut échanger, sa main et le sac de jetons et effectue l'échange si c'est possible sinon renvoie que c'est pas possible
def echanger(jetons,main,sac): # jetons est la liste des jetons défaussés
    possible = True # booléen qui va dire si l'échange est possible
    maintemp = list(main) # création d'une main temporaire pour comparer avec jetons
    if len(jetons) <= len(main):
        i = 0
        while i < len(jetons) and jetons[i] in maintemp:
            maintemp.remove(jetons[i])
            i = i + 1
        if i < len(jetons): # si la boucle n'est pas allée au bout c'est qu'un élément de jetons n'est pas dans la main
            possible = False
        else: 
            if possible and len(jetons) <= len(sac):
                for i in range(len(jetons)):
                    main.remove(jetons[i])
                completer_main(main, sac)
                for i in range(len(jetons)):
                    sac.append(jetons[i])
            else:
                possible = False
    else:
        possible = False
    return possible

# testée : reçoit en paramètre un fichier contenant tout les mots jouables au Scrabble et renvoie une liste de ces mots
def generer_dico(nf):
    autorises = []
    for ligne in nf: # on parcours toutes les lignes du fichier
        autorises.append(ligne.replace("\n", "")) # on ajoute le mot à la liste et on remplace le retour à la ligne par une chaîne vide pour ne pas avoir des \n dans la liste
    return autorises

# testée : reçoit en paramètre un mot que le joueur veut jouer et la main du joueur et renvoie si il est jouable ou non
def mot_jouable(mot,ll):
    lltemp = list(ll) # création d'une liste temporaire pour ne pas modifier l'original qui est la main du joueur
    possible = len(mot) <= len(ll) # vérifie que le mot est plus court que le nombre de jetons dans la main
    nbe = 0 # initialisation du nombre d'erreur
    for i in range(len(mot)): # boucle qui vérifie si chaque lettre du mot est dans la liste
        possible = possible and mot[i] in lltemp
        if possible: # si oui enlève la lettre en question dans la liste temporaire pour pas qu'elle soit réutilisée
            lltemp.remove(mot[i])
        elif mot[i] not in lltemp: # si la lettre n'est pas dans la liste temporaire augmente le nombre d'erreur
            nbe = nbe + 1
    if nbe <= ll.count('?'): # si le nombre d'erreur est inférieur ou égal au nombre de joker dans la main du joueur alors le mot est jouable
        possible = True and len(mot) <= len(ll) # on revérifie si le mot est plus court que la longueur de la main du joueur
    return possible

# testée : reçoit en paramètre la liste de tous les mots jouables au Scrabble et la main du joueur et renvoie une liste de tout les mots qui sont jouables à partir de la main
def mots_jouables(motsfr,ll):
    motsjouables = [] 
    for e in motsfr: # e prend successivement la valeur de chaque mot dans la liste des mots jouables
        if mot_jouable(e, ll): # si le mot est bien jouable à partir de la main du joueur on l'ajoute à la liste
            motsjouables.append(e)
    return motsjouables

# testée : reçoit en paramètre un mot que le joueur veut jouer ainsi que le dictionnaire contenant tous les jetons et leur valeur et renvoie la valeur du mot en question
def valeur_mot(mot,dico):
    val = 0
    if len(mot) == 7: # si le mot a une longueur de 7 lettre rajoute direct 50 points
        val = 50
    for e in mot: # e prend successivement chaque lettre du mot
        val = val + dico[e]['val'] # on rajoute la valeur de la lettre à la somme des valeurs de chaque lettre
    return val

# testée : reçoit en paramètre la liste de tous les mots jouables au Scrabble, la main du joueur et le dictionnaire de tous les jetons avec leur valeur et renvoie le mot jouable qui rapporte le plus de point 
def meilleur_mot(motsfr,ll,dico): 
    result = ""
    valmeilleurmot = 0
    motsjouables = mots_jouables(motsfr, ll) # on récupère la liste des mots jouables
    for mot in motsjouables: # on parcours chaque mot de cette liste
        valmot = valeur_mot(mot, dico) 
        if valmot > valmeilleurmot: # on vérifie si la valeur du mot est supérieur à celle du meilleur mot actuel
            result = mot
            valmeilleurmot = valmot
    return result # si il n'y a aucun mot on renvoie une chaîne vide

# testée :  reçoit en paramètre la liste de tous les mots jouables au Scrabble, la main du joueur et le dictionnaire de tous les jetons avec leur valeur et renvoie la liste de tous les meilleurs mots jouables (qui font gagner le même nombre de point) 
def meilleurs_mots(motsfr,ll,dico):
    res = []
    meilleurmot = meilleur_mot(motsfr, ll, dico) # on récupère le meilleur mot jouable
    if meilleurmot != "": # si il existe bien un meilleur mot on peut continuer
        motsjouables = mots_jouables(motsfr, ll) # on récupère la liste des mots jouables
        valmeilleurmot = valeur_mot(meilleurmot, dico) 
        for mot in motsjouables:
            if valeur_mot(mot, dico) == valmeilleurmot: # on compare avec la valeur du meilleur mot
                res.append(mot)
    return res
            
def lire_coord(jetons):
    jetons = init_jetons()
    i = int(input("Donnez la ligne sur laquelle vous voulez jouer (entre 1 et 16) : ")) # on demande de rentrer entre 1 et 16 car c'est plus intuitif pour le joueur mais par la suite on traitera i-1 et j-1 pour les indices de liste
    j = int(input("Donnez la colonne sur laquelle vous voulez jouer (entre 1 et 16) : "))
    while i < 1 or i > 16 or j < 1 or j > 16:
        print("Pas compris dans les coordonnées du plateau")
        i = int(input("Donnez la ligne sur laquelle vous voulez jouer (entre 1 et 16) : "))
        j = int(input("Donnez la colonne sur laquelle vous voulez jouer (entre 1 et 16) : "))
    liste_coord = [i-1, j-1]
    return liste_coord

def tester_placement(plateau,i,j,dir,mot):
    lln = []
    if plateau[i][j] == mot[0]:
        if dir.lower() == 'horizontal':
            if j + len(mot) - 1 < 15:
                k = 1
                while k < len(mot) and (plateau[i][j+k] == mot[k] or plateau[i][j+k] == "  "):
                    if plateau[i][j+k] == "  ":
                        lln.append(mot[k])
                    k = k + 1
        elif dir.lower() == 'vertical':
            if i + len(mot) - 1 < 15:
                k = 1
                while k < len(mot) and (plateau[i+k][j] == mot[k] or plateau[i+k][j] == "  "):
                    if plateau[i+k][j] == "  ":
                        lln.append(mot[k])
                    k = k + 1
    elif plateau[i][j] == "  ":
        if dir.lower() == 'horizontal':
            if j + len(mot) - 1 < 15:
                k = 0
                while k < len(mot) and (plateau[i][j+k] == mot[k] or plateau[i][j+k] == "  "):
                    if plateau[i][j+k] == "  ":
                        lln.append(mot[k])
                    k = k + 1
        elif dir.lower() == 'vertical':
            if i + len(mot) - 1 < 15:
                k = 0
                while k < len(mot) and (plateau[i+k][j] == mot[k] or plateau[i+k][j] == "  "):
                    if plateau[i+k][j] == "  ":
                        lln.append(mot[k])
                    k = k + 1
    return lln

def placer_mot(plateau,lm,mot,i,j,dir):
    lln = tester_placement(plateau, i , j, dir, mot)
    lmtemp = list(lm)
    possible = len(lln) <= len(lm) and len(mot) >= 2
    k = 0
    while possible and i < len(lln):
        possible = lln[i] in lmtemp
        if possible:
            lmtemp.remove(lln[i]) 
        k = k + 1
    if possible :
        if dir.lower() == 'horizontal':
            for k in range(len(mot)):
                if mot[k] in lln:
                    lm.remove(mot[k])
                    plateau[i][j+k] = mot[k]
        if dir.lower() == 'vertical':
            for k in range(len(mot)):
                if mot[k] in lln:
                    lm.remove(mot[k])
                    plateau[i+k][j] = mot[k]
    return possible

def valeur_mot_bonus(plateau,lm,mot,i,j,dir):
    reussi = placer_mot(plateau, lm, mot, i, j, dir)
    if reussi:
        

            
            






def tour_joueur(plateau):
    affiche_jetons(j)
    action=input("voulez vous passer/échanger/placer ?")
    while not (action=="passer" or action=="échanger" or action=="placer"):
        action=input("voulez vous passer/échanger/placer ?")
    if action=="échanger":
        
    elif action=="passer":
        
    else:


#prog.principal
affiche_jetons([]) # affiche le plateau avec les jetons joués dessus
dico = init_dico() # initialise le dictionnaire avec tous les jetons, leur occurrence et leur valeur
sac = init_pioche(dico) # initialise la pioche à partir du dictionnaire précédent
nbj = int(input("Donnez le nombre de joueurs (entre 2 et 4) : "))
while nbj < 2 or nbj > 4:
    nbj = int(input("ERREUR, redonnez un nombre de joueurs entre 2 et 4 : ")) # tant que le nombre de joueur n'est pas entre 2 et 4 on redemande
if nbj == 2:
    nom1=input("nom du premier joueur:")
    nom2=input("nom du deuxieme joueur:")
    mainj1 = piocher(7, sac)
    print("Voici la main de",nom1,":", mainj1)
    mainj2 = piocher(7, sac)
    print("Voici la main de",nom2,":", mainj2)
elif nbj == 3:
    nom1=input("nom du premier joueur:")
    nom2=input("nom du deuxieme joueur:")
    nom3=input("nom du troisième joueur:")
    mainj1 = piocher(7, sac)
    print("Voici la main de",nom1,":", mainj1)
    mainj2 = piocher(7, sac)
    print("Voici la main de",nom2,":", mainj2)
    mainj3 = piocher(7,sac)
    print("Voici la main de",nom3,":", mainj3)
else:
    nom1=input("nom du premier joueur:")
    nom2=input("nom du deuxieme joueur:")
    nom3=input("nom du troisième joueur:")
    nom4=input("nom du quatrième joueur:")
    mainj1 = piocher(7, sac)
    print("Voici la main de",nom1,":", mainj1)
    mainj2 = piocher(7, sac)
    print("Voici la main de",nom2,";" ,mainj2)
    mainj3 = piocher(7, sac)
    print("Voici la main de",nom3,":", mainj3)
    mainj4 = piocher(7, sac)
    print("Voici la main de",nom4,":", mainj4) # créer les mains en fonction du nombre de joueur

jetons = []
jeton = input("Quel jeton voulez vous échanger j1 ? ")
while len(jeton) == 1:
    jetons.append(jeton)
    jeton = input("Quel jeton voulez vous échanger j1 ? ")
print(echanger(jetons, mainj1, sac))
print(mainj1) # on teste la fonction echanger avec la main du joueur 1
lettre = input("Donnez le jeton que vous jouez j2 : ")
while lettre.upper() != 'STOP':
    mainj2.remove(lettre)
    lettre = input("Redonnez un jeton que vous jouez j2 (stop pour arrêter) : ")
completer_main(mainj2, sac)
print("Voici la main du joueur 2 recomplétée à partir de la pioche", sac, mainj2) # on teste la fonction completer_main avec la main du joueur 2
nf = open('littre.txt') # on ouvre le fichier contenant tout les mots jouables au Scrabble
motsfr = generer_dico(nf) # on créé une liste avec tous ces mots
mot = input("Donnez un mot à jouer j1 : ")
print("Le mot", mot, "est jouable", mot_jouable(mot, mainj1))
print("Voici la liste des mots jouables avec vos jetons :", mots_jouables(motsfr, mainj1)) # on teste les fonctions mot(s)_jouable(s)
les_meilleurs = meilleurs_mots(motsfr, mainj1, dico)
print("Voici la liste des meilleurs mots que vous pouvez jouer (ce qui rapport le plus de point) : ", les_meilleurs)
for e in les_meilleurs:
    print("Voici la valeur de", e, ":", valeur_mot(e, dico)) # on teste les fonctions qui donnent la valeur d'un mot