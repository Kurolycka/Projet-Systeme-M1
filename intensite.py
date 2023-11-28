
#-----------------------Importation des modules nécessaires et autorisés------------------------------

import sys
import os
import re
os.system("clear") #Je clear aussi ma fenêtre pour plus de clareté. Je ne l'ai pas fait avant si jamais l'utilisateur veut faire un ls pour le nom du fichier.



#-----------------------J'ouvre mon fichier en mode lecture------------------------------


fich=open(sys.argv[1], "r", encoding='ISO-8859-1') #Le fichier correspond au premier paramètre donné au programme intensite.py.



#-----------------------J'initialise mes listes et dictionnaires------------------------------


lamba=[] #ma liste de longueur d'onde
intens=[] #ma liste d'intensités
liste_retour=[] #ma liste de liste de liste pour faire le graphe
dico={} #dictionnaire pour le print

maximum=[] #liste pour les maximums des intervalles
minimum=[] #liste pour les minimums des intervalles
moyenne=[] #liste pour les moyennes des intervalles
nombre=[] #liste pour le nombre de valeurs d'intensités dans chaque intervalle



#-----------------------Conversion de mes paramètres dans le bon type------------------------------


taille_pas=float(sys.argv[2]) 
colonne_longueur_onde=int(sys.argv[3])
colonne_intens=int(sys.argv[4])



#-----------------------Je récupère mon séparateur------------------------------


#Je regarde si le séparateur est celui par défaut ou non.
sep_none=str(input("\033[1;32mSi votre séparateur est un espace ou une tabulation tapez Y sinon tapez N : \033[0m"))

somme_none=0 #Pour savoir combien de fois l'utilisateur a déjà donné une valeur invalide.

if (sep_none!="Y" and sep_none!="N"):
    somme_none+=1
    if somme_none==3: #Lorsqu'il a dejà fait trop de tentatives (3).
        print("\e[1;31mTrop de tentatives erronées. Veuillez relancer le programme une fois que vous saurez quelle valeur rentrer.\e[0m")
        sys.exit()
    else: #Sinon je lui laisse encore une chance.
        sep_none=str(input("\033[1;91mValeur remplie incorrecte, il vous reste 2 chances.\nSi votre séparateur est un espace ou une tabulation tapez Y sinon tapez N : \033[0m"))

#Je récupère le paramètre si il me dit que ce n'est pas celui par défaut
if sep_none=="N":
    sep=str(input("\033[1;32mLe séparateur est la chaîne de caractère entre deux valeurs numériques.\nSi votre séparateur est une tabulation ou un espace mettez None. \nFaites attention à mettre les guillemets si il y en.\n Entrez le séparateur: \033[0m"))



#-----------------------Traitement de mes données------------------------------


nombre_total_lignes = len(list(fich)) 
premiere_ligne=True #Variable de contrôle pour détecter la première ligne.


if nombre_total_lignes == 1 : #Je regarde si le fichier n'a qu'une seule ligne ou pas.
    print("\033[1;91mVotre fichier ne contient que une seule ligne qui devrait correspondre aux noms des colonnes. Soit vous n'avez pas de données mais juste des noms de colonnes et il est donc impossible de faire fonctionner ce programme soit vous n'avez pas de noms de colonnes. Merci d'en mettre en première ligne.\033[0m")
    sys.exit() #Dans ce cas j'arrête le programme avec un message d'erreur.
else :
    fich.seek(0) #Je rembobine au début de mon fichier.
    for indice, ligne in enumerate(fich): #Je parcours toutes les lignes de mon fichier.
        if premiere_ligne: #Je fais en sorte de sauter la première ligne du fichier dédiée aux noms des colonnes. 
            premiere_ligne = False
            continue 
        else : #Puis je traite les autres lignes.
            ligne=ligne.strip() 
            if sep_none=="Y":
                longueur=ligne.split()
            else :
                longueur=ligne.split(sep)
            size = len(longueur)
            if (colonne_longueur_onde>size or colonne_intens>size): #Je vérifie qu'il ne m'a pas donné un numéro de colonne plus grand que le nombre de colonnes du fichier.
                print("\033[1;91mLes valeurs données pour les indices de vos colonnes sont incorrects. Veuillez relancer le programme.\033[0m")
                sys.exit() #Si il l'a fait le programme s'arrête.
            longueur=[longueur[k].strip('"') for k in range(0,len(longueur))]
            longueur=[longueur[k].replace(",",".") for k in range(0,len(longueur))]
            lamba.append(longueur[colonne_longueur_onde-1]) #Je rajoute mes valeurs de longueurs d'ondes à la liste correspondante.
            intens.append(longueur[colonne_intens-1]) #Je rajoute mes valeurs d'intensitées à la liste correspondante. 



#-----------------------Je vérifie que les valeurs dans mes listes sont bien des nombres------------------------------


for i in range(0,len(lamba)):
    try:
        testi = float(lamba[i])
        testj = float(intens[i])
    except (ValueError,TypeError) as e: #Si j'ai une erreur car il ne peut pas les convertir en float.
        print("\033[1;91mUne de vos valeurs de longueur d'onde ou d'intensitée n'est pas un nombre entier ou décimal. Veuillez revoir vos valeurs avant de relancer le programme. Attention aux valeurs null.\033[0m")
        exit() #Dans ce cas là j'affiche un message d'erreur et je sors du programme.



#-----------------------Je convertis les valeurs en float dans les deux listes------------------------------


lamba=[float(lamba[i]) for i in range(0,len(lamba))]
intens=[float(intens[i]) for i in range(0,len(intens))]



#-----------------------Je trie mes valeurs en fonction des longueurs d'onde------------------------------


reliees=list(zip(lamba, intens)) #Je fais correspondre mes valeurs de longueurs d'ondes avec mes valeurs d'intensitées.
sort_reliees= sorted(reliees, key=lambda x: x[0]) #Je les trie en fonction des longueurs d'ondes (ordre croissant).
liste_sorted=list(zip(*sort_reliees)) #J'arrête de les faire correspondre.

lamba=liste_sorted[0]
intens=liste_sorted[1]



#-----------------------Je cherche le nombre de fenêtres qu'il y aura dans mon dictionnaire------------------------------


nb_fenetres=(lamba[len(lamba)-1]-lamba[0])/taille_pas
nb_fenetres=int(nb_fenetres)+1



#-----------------------Je créé mon dictionnaire------------------------------

#Je veux stocker mes valeurs d'intensitées dans mon dictionnaire en mettant en clefs les intervalles.

lamba_rendu=int(lamba[0]) #Valeur que j'incrémenterai pour avoir les débuts de mes intervalles.
for i in range(0, nb_fenetres): #D'où l'utilité de calculer le nombre de fenêtres.
    tempo_long=[] #Pour la liste destinée à mon graphe.
    tempo_inten=[] #idem
    inten_fenetre=[] #Liste que je mettrai en valeur de mon dico.
    clef=[round(lamba_rendu,2), round(lamba_rendu+taille_pas,2)] #Liste que je mettrai en clef.
    lamba_rendu=lamba_rendu+taille_pas #J'incrémente.
    for k in range(0,len(lamba)):
        if k != (len(lamba)-1) : #Pour voir si l'intervalle est inclus ou exclus à la dernière longueur d'onde.
            if lamba[k]>=clef[0] and lamba[k]<clef[1]: #Je remplis mes listes.
                inten_fenetre.append(intens[k])
                tempo_long.append(lamba[k])
                tempo_inten.append(intens[k])
        else : #Si je suis à mon dernier intervalle alors ce sera inclus.
             if lamba[k]>=clef[0] and lamba[k]<=clef[1]: #Je remplis mes listes.
               inten_fenetre.append(intens[k])
               tempo_long.append(lamba[k])
               tempo_inten.append(intens[k])
    tempo_1=[tempo_long,tempo_inten] #Pour la liste pour le graphe.
    liste_retour.append(tempo_1) #Liste finale pour le graphe pour cet intervalle.
    if len(inten_fenetre) != 0: #Dans le cas où j'ai des valeurs dans mon intervalle.
        inten_fenetre=sorted(inten_fenetre) #Je trie mes valeurs d'intensitées. 
        clef_dic = str(clef).split("]")[0] #Puis j'affiche correctement l'intervalle en string en fonction de si il est exclu ou inclus.
        if i != (nb_fenetres-1): #Dans le cas où ce n'est pas le dernier intervalle.
          clef_dic=clef_dic+"["
        else : #Dans le cas où c'est le dernier intervalle.
            clef_dic=clef_dic+"]"
        dico[clef_dic]=inten_fenetre #Puis j'ajoute à mes listes et à mon dictionnaire.
        minimum.append(inten_fenetre[0])
        maximum.append(inten_fenetre[len(inten_fenetre)-1])
        moyenne.append(sum(inten_fenetre)/len(inten_fenetre))
        nombre.append(len(inten_fenetre))
    else : #Dans le cas où je n'ai pas de valeurs pour cet intervalle.
        clef_dic = str(clef).split("]")[0] #J'affiche correctement l'intervalle en string en fonction de si il est exclu ou inclus.
        if i != (nb_fenetres-1): #Pour exclus.
          clef_dic=clef_dic+"["
        else : #Pour inclus.
            clef_dic=clef_dic+"]"
        dico[clef_dic]="Aucunes" #Puis j'ajoute à mes listes et à mon dictionnaire.
        minimum.append("null")
        maximum.append("null")
        moyenne.append("null")
        nombre.append("null")




#-----------------------Bel affichage de mon dictionnaire------------------------------


indice=0 #Pour parcourir mon dictionnaire, valeur que j'incrémenterai.
for i in dico.keys():
    print("Intervalle :",i,"\n nombre de données d'intensité :",nombre[indice],"\n minimum des données : ",minimum[indice],
          "\n maximum des données : ", maximum[indice], "\n moyenne des données : ",moyenne[indice],"\n")
    indice += 1



