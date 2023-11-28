
#-----------------------Importation des modules nécessaires et autorisés------------------------------


import sys
import intensite as inten
import matplotlib.pyplot as plt



#-----------------------Je récupère les paramètres et la liste utiles au programme------------------------------


ma_liste=inten.liste_retour
long_deb=float(sys.argv[5])
long_fin=float(sys.argv[6])

unite_long_onde=sys.argv[7]
unite_intens=sys.argv[8]



#-----------------------J'initialise les listes pour mon graphe------------------------------


x_long=[]
y_inten=[]



#-----------------------Je cherche les intervalles à afficher------------------------------


#Mes valeurs par défaut des indices d'intervalles à afficher sont le premier et le dernier :
deb_ind=0
fin_ind=len(ma_liste)-1 

#Je cherche l'intervalle du dictionnaire dans lequel se trouve la longueur d'onde de début d'intervalle pour le graphe et j'en récupère l'indice dans deb_ind.:
for i in range(0,len(ma_liste)-1):
    if ma_liste[i] and ma_liste[i][0]: #Je regarde si il y a des valeurs dans cet intervalle.
        if len(ma_liste[i][0])==1: #Je regarde si l'intervalle n'a qu'une seule valeur.
            if long_deb<=ma_liste[i][0][0]:
                deb_ind=i
                break
        else:
            if long_deb >= ma_liste[i][0][0] and long_deb < ma_liste[i][0][-1] :
                deb_ind = i 
                break

#Je cherche l'intervalle du dictionnaire dans lequel se trouve la longueur d'onde de fin d'intervalle pour le graphe et j'en récupère l'indice dans deb_fin.:
for j in range(deb_ind, len(ma_liste)):
    if ma_liste[j] and ma_liste[j][0]: #Je regarde si il y a des valeurs dans cet intervalle.
        if len(ma_liste[j][0])==1: #Je regarde si l'intervalle n'a qu'une seule valeur.
            if ma_liste[j][0][0]>=long_fin:
                fin_ind=j
                break
        else :
            if j == len(ma_liste)-1: #Je regarde si c'est le dernier intervalle.
                if long_fin >= ma_liste[j][0][0] and long_fin <= ma_liste[j][0][-1]:
                    fin_ind = j
                    break
            else:
                if long_fin >= ma_liste[j][0][0] and long_fin < ma_liste[j][0][-1]:
                    fin_ind = j
                    break



#-----------------------J'ajoute à mes listes pour le graphe les valeurs------------------------------


for i in range(deb_ind,fin_ind+1):
    for k in range(0,len(ma_liste[i][0])):
        x_long.append(ma_liste[i][0][k])
        y_inten.append(ma_liste[i][1][k])



#-----------------------Je lui demande si il veut que j'affiche des données correspondant au graphe------------------------------


option_affichage=str(input("Voulez vous afficher les données (minimum, maximum...) correspondant au graphe ? Si oui tapez Y sinon tapez N: "))#Je lui demande si il veut que j'affiche les données.
while (option_affichage !="Y" and option_affichage != "N"): #Si il me répond pas la bonne chose.
    print("La valeur rentrée n'est pas correcte.") #Je lui demande en boucle une réponse au bon format et lui affiche un message d'erreur.
    option_affichage=str(input("Voulez vous afficher les données (minimum, maximum...) correspondant au graphe ? Si oui tapez Y sinon tapez N: "))
if option_affichage=="Y": #Je lui affiche les données si il répond positivement. 
    print("Valeur max de longueur d'onde: "+str(max(x_long))+" "+unite_long_onde+
          "\n Valeur min de longueur d'onde: "+str(min(x_long))+" "+unite_long_onde+
          "\n Moyenne de la longueur d'onde: "+str((sum(x_long)/len(x_long)))+" "+unite_long_onde+
          "\n Valeur max de l'intensité: "+str(max(y_inten))+" "+unite_intens+
          "\n Valeur min de l'intensité: "+str(min(y_inten))+" "+unite_intens+
          "\n Moyenne de l'intensité: "+str((sum(y_inten)/len(y_inten)))+" "+unite_intens)



#-----------------------J'affiche le graphe------------------------------


plt.plot(x_long,y_inten,color="purple")
plt.xlabel("Longueur d'onde ("+unite_long_onde+")")
plt.ylabel("Intensité ("+unite_intens+")")
plt.title("Graphe de l'intensité pour un intervalle de longueur d'onde fourni")
plt.grid(True)
plt.show()