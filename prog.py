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
def affiche_jetons(jetons): # jetons est la liste créée à partie de init_jetons
    bonus = init_bonus()
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
        if mot[i] in lltemp: # si oui enlève la lettre en question dans la liste temporaire pour pas qu'elle soit réutilisée
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

# testée : qui demande à l'utilisateur là où il veut jouer au début et renvoie ces coordonnées sous forme d'une liste de deux éléments         
def lire_coord():
    i = int(input("Donnez la ligne sur laquelle vous voulez jouer (entre 1 et 16) : ")) # on demande de rentrer entre 1 et 16 car c'est plus intuitif pour le joueur mais par la suite on traitera i-1 et j-1 pour les indices de liste
    j = int(input("Donnez la colonne sur laquelle vous voulez jouer (entre 1 et 16) : "))
    while i < 1 or i > 16 or j < 1 or j > 16:
        print("Pas compris dans les coordonnées du plateau")
        i = int(input("Donnez la ligne sur laquelle vous voulez jouer (entre 1 et 16) : "))
        j = int(input("Donnez la colonne sur laquelle vous voulez jouer (entre 1 et 16) : ")) # si l'utilisateur ne rentre pas des coordonnées compris dans le plateau on redemande
    liste_coord = [i-1, j-1] # on revient en base 0-15 pour correspondre à l'indice des listes
    return liste_coord # return i-1, j-1 possible

# testée : reçoit en paramètre le plateau, les coordonnées où le joueur veut jouer, la direction et le mot à jouer, elle renvoie la liste des lettres nécessaires à rajouter depuis la main si le placement est possible, sinon elle renvoie une liste vide
def tester_placement(plateau,i,j,dir,mot):
    lln = [] # initialisation de la liste des lettres nécessaires pour jouer le mot
    if mot[0] in plateau[i][j]: # on vérifie si la première lettre de notre mot est là où on veut jouer
        if dir.lower() == 'horizontal': # si place à l'horizontal, on va incrémenter les colonnes
            if j + len(mot) - 1 < 15: # on test si ça va pas sortir du plateau
                k = 1
                while k < len(mot): # tant qu'on rencontre pas une lettre qui n'est pas sensée être dans notre mot, on continue
                    if plateau[i][j+k] == "  ": # si la lettre n'est pas sur le plateau, on rajoute la lettre à placer dans la liste de lettre nécessaire
                        lln.append(mot[k])
                    elif plateau[i][j+k] != mot[k]:
                        lln=[]
                        break
                    k = k + 1 
        elif dir.lower() == 'vertical': # idem si on va à la vertical sauf qu'on incrémente les lignes
            if i + len(mot) - 1 < 15:
                k = 1
                while k < len(mot):
                    if plateau[i+k][j] == "  ":
                        lln.append(mot[k])
                    elif plateau[i+k][j] != mot[k]:
                        lln=[]
                        break
                    k = k + 1
    elif plateau[i][j] == "  ": # si la première de notre mot n'est pas là où on commence, on partir de k = 0 dans les for pour tester la première lettre
        if dir.lower() == 'horizontal':
            if j + len(mot) - 1 < 15:
                k = 0
                while k < len(mot):
                    if plateau[i][j+k] == "  ":
                        lln.append(mot[k])
                    elif plateau[i][j+k] != mot[k]:
                        lln=[]
                        break
                    k = k + 1
        elif dir.lower() == 'vertical':
            if i + len(mot) - 1 < 15:
                k = 0
                while k < len(mot):
                    if plateau[i+k][j] == "  ":
                        lln.append(mot[k])
                    elif plateau[i+k][j] != mot[k]:
                        lln=[]
                        break
                    k = k + 1
    return lln

# testée : reçoit en paramètre la plateau, la main du joueur, le mot à jouer, les coordonnées de départ ainsi que la direction de placement et renvoie si le placement a pu s'effectuer ou non (effectue le placement si possible) ainsi que le mot au cas où si il a été modifié par les bonus "?"
def placer_mot(plateau,lm,mot,i,j,dir):
    lln = tester_placement(plateau, i , j, dir, mot) # on récupère la liste de lettre nécessaire
    if len(lln)!=0:
        lmtemp = list(lm) # on créé une copie temporaire de la main du joueur pour la modifier
        possible = len(lln) <= len(lm) and len(mot) >= 2 and len(lln) > 0 # on teste si on a assez de lettre dans la main pour combler les lettres manquantes, si le mot à bien un longueur de 2 au minimum et si il y a au moins une lettre à rajouter
        k = 0
        while possible and k < len(lln): # on teste si le placement est possible en vérifiant si les les lettres nécessaires sont dans la main du joueur
            possible = lln[k] in lmtemp
            if possible: # si oui on enlève la lettre de la liste temporaire
                lmtemp.remove(lln[k]) 
            else:
                if "?" in lmtemp:
                    lmtemp.remove("?")
                    possible = True
                    lln[k] = "?"
                    lmottemp = list(mot)
                    lmottemp[k] = "?"
                    mot = "".join(lmottemp)
            k = k + 1
        if possible : # si c'est possible on place les lettres manquantes
            if dir.lower() == 'horizontal':
                if mot[0] in plateau[i][j]:
                    for k in range(1,len(mot)):
                        if mot[k] in lln:
                            lm.remove(mot[k])
                            plateau[i][j+k] = mot[k]
                            lln.remove(mot[k])
                else:
                    for k in range(len(mot)):
                        if mot[k] in lln: # si la lettre du mot est dans la liste nécessaire, on le place
                            lm.remove(mot[k])
                            plateau[i][j+k] = mot[k]
                            lln.remove(mot[k])
            elif dir.lower() == 'vertical':
                if mot[0] in plateau[i][j]:
                    for k in range(1,len(mot)):
                        if mot[k] in lln:
                            lm.remove(mot[k])
                            plateau[i+k][j] = mot[k]
                            lln.remove(mot[k])
                else:
                    for k in range(len(mot)):
                        if mot[k] in lln:
                            lm.remove(mot[k])
                            plateau[i+k][j] = mot[k]
                            lln.remove(mot[k])
    else:
        possible=False
    d={}
    d["possible"]=possible
    d["mot"]=mot
    return d

# testée : reçoit en paramètre le plateau, la main du joueur, le mot à jouer, les coordonnées de placement, la direction ainsi que le dictionnaire contenant tous les jetons avec leur valeur et la liste de listes des bonus; renvoie la valeur du mot en prenant en compte les bonus du plateau (0 si le mot n'est pas jouable)
def valeur_mot_bonus(plateau,lm,mot,i,j,dir,dico,bonus):
    valeurmot = valeur_mot(mot, dico) # on récupère la valeur initiale du mot
    if dir.lower() == 'horizontal':
        for k in range(len(mot)): # si la lettre est sur une case bonus, on applique le bonus
            if bonus[i][j+k] == "MT":
                valeurmot = valeurmot * 3 # on multiplie par 3 la valeur du mot pour mot compte triple
            elif bonus[i][j+k] == "MD":
                valeurmot = valeurmot * 2 # on multiplie par 2 la valeur du mot pour mot compte double
            elif bonus[i][j+k] == "LT":
                valeurmot = valeurmot + dico[mot[k]]['val'] * 2 # on ajoute 2 fois la valeur de la lettre pour lettre compte triple
            elif bonus[i][j+k] == "LD":
                valeurmot = valeurmot + dico[mot[k]]['val'] # on ajoute 1 fois la valeur de la lettre pour lettre compte double
            bonus[i][j+k] = "  " # on annule le bonus de la case utilisée pour pas qu'elle soit réutilisée
    elif dir.lower() == 'vertical':
        for k in range(len(mot)):
            if bonus[i+k][j] == "MT":
                valeurmot = valeurmot * 3
            elif bonus[i+k][j] == "MD":
                valeurmot = valeurmot * 2
            elif bonus[i+k][j] == "LT":
                valeurmot = valeurmot + dico[mot[k]]['val'] * 2
            elif bonus[i+k][j] == "LD":
                valeurmot = valeurmot + dico[mot[k]]['val'] 
            bonus[i][j+k] = "  "
    return valeurmot

# testée : reçoit en paramètre l'inventaire de tous les joueurs ainsi que la pioche et vérifie si la partie est finie
def fin_partie(inventaire_joueur,numeroj,sac):
    return len(sac) < 7 - len(inventaire_joueur[numeroj]['main']) or len(sac) == 0

# testée : reçoit en paramètre le plateau, l'inventaire de tous les joueurs, la pioche, le dictionnaire des jetons ainsi que la liste des mots autorisés au Scrabble; gère le tour du joueur et renvoie un booléen qui dit si la partie est finie 
def tour_joueur(plateau,inventaire_joueur,sac,motsfr,dico,bonus,numeroj):
    affiche_jetons(plateau)
    print("Tour de", inventaire_joueur[numeroj]['nom'])
    print("Voici votre main", inventaire_joueur[numeroj]['nom'], ":", inventaire_joueur[numeroj]['main'])
    action = input("Voulez-vous passer/échanger/placer ? ").lower()
    while not (action == "passer" or action == "échanger" or action == "placer"):
        action = input("ERREUR; Voulez-vous passer/échanger/placer ? ")
    if action == "échanger":
        jetonsdefausses = [] 
        j = input("Donnez un jeton que vous voulez échanger : ")
        while len(j) == 1:
            jetonsdefausses.append(j.upper())
            j = input("Donnez un autre jeton que vous voulez échanger : ") # créer la liste de jetons que le joueur veut défausser
        if len(jetonsdefausses) > 0: # si le joueur a bien échanger des jetons alors on appelle la fonction
            print("L'échange a réussi :", echanger(jetonsdefausses, inventaire_joueur[numeroj]['main'], sac))
        print("Voici votre main :", inventaire_joueur[numeroj]['main']) # montre la nouvelle main du joueur
    elif action == "placer":
        liste_coord = lire_coord() # demande les coordonnées de départ au joueur
        i = liste_coord[0]
        j = liste_coord[1] # on récupère ces coordonnées sous forme de liste (on aurait pu faire un return avec deux valeurs)
        dir = input("Donnez la direction dans laquelle vous voulez jouer (horizontal/vertical) : ")
        while not (dir == "horizontal" or dir == "vertical"):
            dir = input("ERREUR; Donnez la direction dans laquelle vous voulez jouer (horizontal/vertical) : ")
        mot = input("Donnez le mot que vous voulez jouer en majuscule : ")
        passe="n"
        while not mot.upper() in motsfr and passe != "o": # on vérifie si le mot est autorisés
            print("ERREUR,le mot que vous voulez jouez n'existe pas")
            passe = input("Voulez passer finalement ? (o/n) : ")
            if passe=="n":
                aide = input("Voulez-vous des idées de mots jouables ? (o/n) :") # on propose de l'aide si le joueur bloque et ne sais pas quoi jouer 
                if aide=="o":
                    print("Voici une liste de mot que vous pouvez jouer avec votre main :", mots_jouables(motsfr, inventaire_joueur[numeroj]['main']))
            elif passe=="o":
                reussi=True
                break
            mot = input( "Donnez le mot que vous voulez jouer en majuscule : ")
        if not passe=="o":
            possible_et_mot = placer_mot(plateau, inventaire_joueur[numeroj]['main'], mot.upper(), i, j, dir)
            reussi=possible_et_mot["possible"]
            print("Le placement a réussi :", reussi) # dit si le placement a réussi
            while not reussi : # tant qu'il n'a pas réussi on recommence (il peut décider de passer finalement)
                aide = input("Voulez-vous des idées de mots jouables ? (o/n) :") # on propose de l'aide si le joueur bloque et ne sais pas quoi jouer
                if aide == 'o':
                    print("Voici une liste de mot que vous pouvez jouer avec votre main :", mots_jouables(motsfr, inventaire_joueur[numeroj]['main']))
                liste_coord = lire_coord()
                i = liste_coord[0]
                j = liste_coord[1]
                dir = input("Donnez la direction dans laquelle vous voulez jouer (horizontal/vertical) : ")
                while not (dir == "horizontal" or dir == "vertical"):
                    dir = input("ERREUR; Donnez la direction dans laquelle vous voulez jouer (horizontal/vertical) : ")
                mot = input("Donnez le mot que vous voulez jouer en majuscule : ")
                passe="n"
                while not mot.upper() in motsfr and passe != "o": # on vérifie si le mot est autorisés
                    print("ERREUR,le mot que vous voulez jouez n'existe pas")
                    passe = input("Voulez passer finalement ? (o/n) : ")
                    if passe=="n":
                        aide = input("Voulez-vous des idées de mots jouables ? (o/n) :") # on propose de l'aide si le joueur bloque et ne sais pas quoi jouer 
                        if aide=="o":
                            print("Voici une liste de mot que vous pouvez jouer avec votre main :", mots_jouables(motsfr, inventaire_joueur[numeroj]['main']))
                    elif passe=="o":
                        reussi=True
                        break
                    mot = input("Donnez le mot que vous voulez jouer en majuscule : ")
                if not passe=="o":
                    possible_et_mot = placer_mot(plateau, inventaire_joueur[numeroj]['main'], mot.upper(), i, j, dir)
                    reussi=possible_et_mot["possible"]
                    print("Le placement a réussi :", reussi) # dit si le placement a réussi
        if not passe=="o":
            mot=possible_et_mot["mot"]
            affiche_jetons(plateau)
            valeurmot = valeur_mot_bonus(plateau, inventaire_joueur[numeroj]['main'], mot, i, j, dir, dico, bonus)
            print("Voici la valeur du mot que vous venez de jouer :", valeurmot)
            inventaire_joueur[numeroj]['score'] = inventaire_joueur[numeroj]['score'] + valeurmot # on récupère la valeur du mot avec les bonus et on l'ajoute au score du joueur
            print("Voici votre score :", inventaire_joueur[numeroj]['score'])
            print("Voici votre main :", inventaire_joueur[numeroj]['main'])
    finpartie = fin_partie(inventaire_joueur, numeroj, sac)
    if not finpartie: # on vérifie si c'est la fin de la partie
        completer_main(inventaire_joueur[numeroj]['main'], sac)
        print("Voici votre main complétée :", inventaire_joueur[numeroj]['main'])
    return finpartie

# testée : reçoit en paramètre le numéro du joueur qui a joué et le nombre de joueur dans la partie et renvoie le numéro du prochain joueur
def detection_prochainj(numeroj,nbj):
    if numeroj < nbj - 1: # tant qu'on est pas au dernier joueur on incrémente
        numeroj = numeroj + 1
    else: # dès qu'on est au dernier joueur on repart du premier joueur
        numeroj = 0
    return numeroj

#prog.principal
plateau = init_jetons() # on initialise le plateau
bonus = init_bonus() # on initialise les bonus
affiche_jetons(plateau) # affiche le plateau avec les jetons joués dessus
dico = init_dico() # initialise le dictionnaire avec tous les jetons, leur occurrence et leur valeur
sac = init_pioche(dico) # initialise la pioche à partir du dictionnaire précédent
nf = open('littre.txt') # on ouvre le fichier contenant tout les mots jouables au Scrabble
motsfr = generer_dico(nf) # on créé une liste avec tous ces mots
nbj = int(input("Donnez le nombre de joueurs (entre 2 et 4) : "))
while nbj < 2 or nbj > 4:
    nbj = int(input("ERREUR, redonnez un nombre de joueurs entre 2 et 4 : ")) # tant que le nombre de joueur n'est pas entre 2 et 4 on redemande
inventaire_joueurs = []
for i in range(nbj):
    d = {}
    nom = input("Nom du joueur : ")
    d["nom"] = nom
    main = piocher(7,sac)
    d["main"] = main
    score = 0
    d["score"] = score
    inventaire_joueurs.append(d)
    print("Voici la main de", nom, ":", main) # créer un inventaire de tous les joueurs avec leurs noms, mains et scores dans une liste de dictionnaires
finpartie = False
numeroj = 0
while not finpartie: # tant qu'on a pas fini la partie on joue
    finpartie = tour_joueur(plateau, inventaire_joueurs, sac, motsfr, dico, bonus, numeroj) # gère le tour du joueur
    numeroj = detection_prochainj(numeroj, nbj) # passe au joueur suivant
meilleurscore = -1 # on initialise le meilleur score
for j in range(len(inventaire_joueurs)):
    main = inventaire_joueurs[j]['main'] # on récupère la main du joueur
    score = inventaire_joueurs[j]['score'] # ainsi que son score
    malus = 0 # on initialise le malus
    for lettre in main: # on regarde toutes les lettres qui reste dans la main du joueur et on ajoute leur valeur au malus
        malus = malus + dico[lettre]['val']
    inventaire_joueurs[j]['score'] = score - malus # on soustrait le malus au score
    if inventaire_joueurs[j]['score'] > meilleurscore: # si son score est plus grand que le meilleur score on garde en mémoire son score
        meilleurscore = inventaire_joueurs[j]['score']
        vainqueur = inventaire_joueurs[j]['nom']
    print("Voici le score de", inventaire_joueurs[j]['nom'], ":", inventaire_joueurs[j]['score']) # on affiche le score du joueur
print("Le vainqueur est :", vainqueur, "avec", meilleurscore, "points") # on affiche le vainqueur
