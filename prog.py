import random

# testée : renvoie une liste de listes contenant les coordonnées des bonus 
def init_bonus():
    bonus = []
    cases_MT = [[0,JE CASSE TOUT !!!!
            elif l in cases_LT:
                bonus[i].append("LT")
            elif l in cases_LD:
                bonus[i].append("LD")
            else:
                bonus[i].append("  ")
    return bonus

#testée : initialise les jetons sur le plateau (ici aucun)
def init_jetons():
    jetons = []
    for i in range(15):
        jetons.append([])
        for j in range(15):
            jetons[i].append("  ")
    return jetons

#testée : affiche le plateau dans la console avec les jetons joués reçu en paramètre
def affiche_jetons(j): #on imagine que j est une liste de 3-uplets (j = [[lettre,i,j]...])
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
                print("||", end = '')
        print()

# testée
def init_dico():
    dico = {'A': {'occ': 9, 'val': 1}, 'B': {'occ': 2, 'val': 3}, 'C': {'occ': 2, 'val': 3}, 'D': {'occ': 3, 'val': 2}, 'E': {'occ': 15, 'val': 1}, 'F': {'occ': 2, 'val': 4}, 'G': {'occ': 2, 'val': 2}, 'H': {'occ': 2, 'val': 4}, 'I': {'occ': 8, 'val': 1}, 'J': {'occ': 1, 'val': 8}, 'K': {'occ': 1, 'val': 10}, 'L': {'occ': 5, 'val': 1}, 'M': {'occ': 3, 'val': 2}, 'N': {'occ': 6, 'val': 1}, 'O': {'occ': 6, 'val': 1}, 'P': {'occ': 2, 'val': 3}, 'Q': {'occ': 1, 'val': 8}, 'R': {'occ': 6, 'val': 1}, 'S': {'occ': 6, 'val': 1}, 'T': {'occ': 6, 'val': 1}, 'U': {'occ': 6, 'val': 1}, 'V': {'occ': 2, 'val': 4}, 'W': {'occ': 1, 'val': 10}, 'X': {'occ': 1, 'val': 10}, 'Y': {'occ': 1, 'val': 10}, 'Z': {'occ': 1, 'val': 10}, '?': {'occ': 2, 'val': 0}}
    return dico

# Méthode pour faire le dictionnaire rapidement :
# lettre = 'A'
# dico = {}
# for i in range(26):
#     print(lettre)
#     dico[lettre] = {'occ':' ','val':' '}
#     dico[lettre]['occ'] = int(input("occurence : "))
#     dico[lettre]['val'] = int(input("valeur : "))
#     lettre = chr(ord(lettre)+1)
# print(dico)

# testée
def init_pioche(dico):
    alphab = list(dico.keys())
    sac = []
    for e in alphab:
        for i in range(dico[e]['occ']):
            sac.append(e)
    return sac

#testée
def piocher(x,sac):
    main = []
    for i in range(x):
        indice = random.randint(0,len(sac)-1)
        main.append(sac[indice])
        sac.pop(indice)
    return main

#testé
def completer_main(main,sac):
    x = 7 - len(main)
    if len(sac) >= x:
        pioche = piocher(x,sac)
    else:
        pioche = piocher(len(sac),sac)
    for i in range(len(pioche)):
        main.append(pioche[i])

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

def generer_dico(nf):
    autorises = []
    for ligne in nf:
        autorises.append(ligne.replace("\n", ""))
    return autorises

def mot_jouable(mot,ll):
    lltemp = list(ll)
    possible = len(mot) <= len(ll)
    i = 0
    nbe = 0
    while i < len(mot):
        possible = possible and mot[i] in lltemp
        if possible:
            lltemp.remove(mot[i])
        elif mot[i] not in lltemp:
            nbe = nbe + 1
        i = i + 1
    if nbe <= ll.count('?'):
        possible = True and len(mot) <= len(ll)
    return possible

def mots_jouables(motsfr,ll):
    motsjouables = [] 
    for e in motsfr:
        if mot_jouable(e, ll):
            motsjouables.append(e)
    return motsjouables

def valeur_mot(mot,dico):
    val = 0
    if len(mot) == 7:
        val = 50
    for e in mot:
        val = val + dico[e]['val']
    return val

def meilleur_mot(motsfr,ll,dico): 
    result = ""
    valmeilleurmot = 0
    motsjouables = mots_jouables(motsfr, ll)
    for mot in motsjouables:
        valmot = valeur_mot(mot, dico)
        if valmot > valmeilleurmot:
            result = mot
            valmeilleurmot = valmot
    return result

def meilleurs_mots(motsfr,ll,dico):
    res = []
    meilleurmot = meilleur_mot(motsfr, ll, dico)
    if meilleurmot != "":
        motsjouables = mots_jouables(motsfr, ll)
        valmeilleurmot = valeur_mot(meilleurmot, dico)
        for mot in motsjouables:
            if valeur_mot(mot, dico) == valmeilleurmot:
                res.append(mot)
    return res
            

            
            





















#prog.principal
# affiche_jetons([])
dico = init_dico()
sac = init_pioche(dico)
nbj = int(input("Donnez le nombre de joueurs (entre 2 et 4) : "))
while nbj < 2 or nbj > 4:
    nbj = int(input("ERREUR, redonnez un nombre de joueurs entre 2 et 4 : "))
if nbj == 2:
    mainj1 = piocher(7, sac)
    print("Voici la main du joueur 1 :", mainj1)
    mainj2 = piocher(7, sac)
    print("Voici la main du joueur 2 :", mainj2)
elif nbj == 3:
    mainj1 = piocher(7, sac)
    print("Voici la main du joueur 1 :", mainj1)
    mainj2 = piocher(7, sac)
    print("Voici la main du joueur 2 :", mainj2)
    mainj3 = piocher(7,sac)
else:
    mainj1 = piocher(7, sac)
    print("Voici la main du joueur 1 :", mainj1)
    mainj2 = piocher(7, sac)
    print("Voici la main du joueur 2 :", mainj2)
    mainj3 = piocher(7, sac)
    print("Voici la main du joueur 3 :", mainj3)
    mainj4 = piocher(7, sac)
    print("Voici la main du joueur 4 :", mainj4)
# jetons = []
# jeton = input("Quel jeton voulez vous échanger ? ")
# while len(jeton) == 1:
#     jetons.append(jeton)
#     jeton = input("Quel jeton voulez vous échanger ? ")
# print(echanger(jetons, mainj1, sac))
# print(mainj1)
nf = open('littre.txt')
motsfr = generer_dico(nf)
mot = input("Donnez un mot à jouer : ")
print("Le mot", mot, "est jouable", mot_jouable(mot, mainj1))
print("Voici la liste des mots jouables avec vos jetons :", mots_jouables(motsfr, mainj1))
