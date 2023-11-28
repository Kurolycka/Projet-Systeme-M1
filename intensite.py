#commentaire à la con 

#Importation des modules nécessaires et autorisés :
import sys
import os
import re
os.system("clear")

fich=open(sys.argv[1], "r", encoding='ISO-8859-1') #j'ouvre le fichier qui est le premier paramètre de ce programme en mode lecture 

lamba=[] #ma liste de longueur d'onde
intens=[] #ma liste d'intensités
liste_retour=[]

#Je traite la valeur du pas pour si jamais c'est un float :
taille_pas=sys.argv[2]
taille_pas=float(taille_pas) 

colonne_longueur_onde=int(sys.argv[3])
colonne_intens=int(sys.argv[4])

dico={} #je créé un dictionnaire vide pour le print


#Je regarde si le séparateur est celui par défaut ou non 
sep_none=str(input("\033[1;32mSi votre séparateur est un espace ou une tabulation tapez Y sinon tapez N : \033[0m"))
somme_none=0
if (sep_none!="Y" and sep_none!="N"):
    somme_none+=1
    if somme_none==3:
        sys.exit()
    else:
        sep_none=str(input("\033[1;91mValeur remplie incorrecte, il vous reste 2 chances.\nSi votre séparateur est un espace ou une tabulation tapez Y sinon tapez N : \033[0m"))

if sep_none=="N":
    sep=str(input("\033[1;32mLe séparateur est la chaîne de caractère entre deux valeurs numériques.\nSi votre séparateur est une tabulation ou un espace mettez None. \nFaites attention à mettre les guillemets si il y en.\n Entrez le séparateur: \033[0m"))

nombre_total_lignes = len(list(fich))
premiere_ligne=True #Variable de contrôle pour détecter la première ligne

#---------------------------Traitement de mes données------------------------------------


if nombre_total_lignes == 1 :
    print("\033[1;91mVotre fichier ne contient que une seule ligne qui devrait correspondre aux noms des colonnes. Soit vous n'avez pas de données mais juste des noms de colonnes et il est donc impossible de faire fonctionner ce programme soit vous n'avez pas de noms de colonnes. Merci d'en mettre en première ligne.\033[0m")
    sys.exit()
else :
    fich.seek(0) #je rembobine au début sinon ça marche pas 
#Traitement des lignes et récupération des longueurs d'onde et des intensités :
    for indice, ligne in enumerate(fich): #je parcours toutes les lignes de mon fichier 
        if premiere_ligne:
            premiere_ligne = False
            continue 
        else : 
            ligne=ligne.strip() #Pour enlever les retour à la ligne \n
            if sep_none=="Y":
                longueur=ligne.split()
            else :
                longueur=ligne.split(sep)
            size = len(longueur)
            if (colonne_longueur_onde>size or colonne_intens>size):
                print("\033[1;91mLes valeurs données pour les indices de vos colonnes sont incorrects. Veuillez relancer le programme.\033[0m")
                quit()
            longueur=[longueur[k].strip('"') for k in range(0,len(longueur))]
            longueur=[longueur[k].replace(",",".") for k in range(0,len(longueur))]
            lamba.append(longueur[colonne_longueur_onde-1]) 
            intens.append(longueur[colonne_intens-1])


for i in range(0,len(lamba)):
    try:
        testi = float(lamba[i])
        testj = float(intens[i])
    except (ValueError,TypeError) as e:
        print("\033[1;91mUne de vos valeurs de longueur d'onde ou d'intensitée n'est pas un nombre entier ou décimal. Veuillez revoir vos valeurs avant de relancer le programme. Attention aux valeurs null.\033[0m")
        exit()

#Je convertis les valeurs qui étaient en string en float dans les deux listes :
lamba=[float(lamba[i]) for i in range(0,len(lamba))]
intens=[float(intens[i]) for i in range(0,len(intens))]

print(lamba)
print(intens)

#je sort les valeurs de lambda et fait en sorte que elles soient associées aux bonnes valeurs de longueur d'onde :
reliees=list(zip(lamba, intens)) #je fais correspondre mes valeurs de longueurs d'onde avec mes valeurs d'intensité
sort_reliees= sorted(reliees, key=lambda x: x[0])
liste_sorted=list(zip(*sort_reliees))

print(liste_sorted)

lamba=liste_sorted[0]
intens=liste_sorted[1]

#je veux ensuite faire des fenêtres donc je cherche le nombre de fenêtres qu'il y a :
nb_fenetres=(lamba[len(lamba)-1]-lamba[0])/taille_pas
nb_fenetres=int(nb_fenetres)+1


#Je veux maintenant stocker mes valeurs d'intensité dans mon dictionnaire en mettant en clef les intervalles 
lamba_rendu=int(lamba[0]) #valeur que j'incrémenterai pour avoir les débuts de mes intervalles
maximum=[] #liste pour les maximums des intervalles
minimum=[] #liste pour les minimums des intervalles
moyenne=[] #liste pour les moyennes des intervalles
nombre=[] #liste pour le nombre de valeurs d'intensités dans chaque intervalle
for i in range(0, nb_fenetres): #d'où l'utilité de calculer le nombre de fenêtres 
    tempo_long=[]
    tempo_inten=[]
    inten_fenetre=[] #liste que je mettrai en valeur de mon dico 
    clef=[round(lamba_rendu,2), round(lamba_rendu+taille_pas,2)] #liste que je mettrai en clef 
    lamba_rendu=lamba_rendu+taille_pas #j'incrémente
    for k in range(0,len(lamba)):
        if k != (len(lamba)-1) : #pour voir si l'intervalle est inclus ou exclus à la dernière longueur d'onde
            if lamba[k]>=clef[0] and lamba[k]<clef[1]:
                inten_fenetre.append(intens[k])
                tempo_long.append(lamba[k])
                tempo_inten.append(intens[k])
        else :
             if lamba[k]>=clef[0] and lamba[k]<=clef[1]:
               inten_fenetre.append(intens[k])
               tempo_long.append(lamba[k])
               tempo_inten.append(intens[k])
    tempo_1=[tempo_long,tempo_inten]
    liste_retour.append(tempo_1)
    if len(inten_fenetre) != 0:
        inten_fenetre=sorted(inten_fenetre) #je sort mes valeurs 
        clef_dic = str(clef).split("]")[0] #puis j'affiche correctement l'intervalle en string en fonction de si il est exclu ou inclus 
        if i != (nb_fenetres-1):
          clef_dic=clef_dic+"["
        else :
            clef_dic=clef_dic+"]"
        dico[clef_dic]=inten_fenetre
        minimum.append(inten_fenetre[0])
        maximum.append(inten_fenetre[len(inten_fenetre)-1])
        moyenne.append(sum(inten_fenetre)/len(inten_fenetre))
        nombre.append(len(inten_fenetre))
    else :
        clef_dic = str(clef).split("]")[0] #puis j'affiche correctement l'intervalle en string en fonction de si il est exclu ou inclus 
        if i != (nb_fenetres-1):
          clef_dic=clef_dic+"["
        else :
            clef_dic=clef_dic+"]"
        dico[clef_dic]="Aucunes"
        minimum.append("null")
        maximum.append("null")
        moyenne.append("null")
        nombre.append("null")


#Bel affichage de mon dictionnaire :
indice=0
for i in dico.keys():
    print("Intervalle :",i,"\n nombre de données d'intensité :",nombre[indice],"\n minimum des données : ",minimum[indice],
          "\n maximum des données : ", maximum[indice], "\n moyenne des données : ",moyenne[indice],"\n")
    indice += 1



