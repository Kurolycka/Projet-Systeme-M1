
#-----------------Création de l'help du programme---------------------------------


if [ "$1" == "-h" ] || [ "$1" == "-help" ]; then #Affichage de l'help de base, -h et -help.
    echo -e "\n $(basename $0) -- Programme qui indexe les intensités par fenêtres de longueurs d'ondes selon une taille de pas que vous nous donnez. Permet aussi d'afficher un graphe des intensités en fonction des longueurs d'ondes pour un intervalle fourni.
    \n Afin de ne pas noyer l'utilisateur sous les informations l'aide est divisée en catégorie avec plusieurs options. Choisissez celle correspondant aux informations que vous recherchez. 
    
    Options : 
    
    -h : Affiche cette aide.
    -help : Affiche également cette aide.
    -hp : Aide dédiée aux paramètres.
    -hg : Aide dédiée au graphique.
    -ht : Aide dédiée au traitement des données. \n"
    exit #Sortie du programme.

elif [ "$1" == "-hp" ]; then #Affichage d'une des ramifications de l'help qui est -hp pour les paramètres.
    echo -e "\e[1;32mAide dédiée aux paramètres. Pour revenir à l'aide principale utilisez l'option -h ou bien l'option -help.\e[0m

    \e[1;36;4mChemin du fichier (chemin):\e[0m  Si vous êtes actuellement dans le répertoire où se trouve votre fichier vous pouvez simplement mettre le nom du fichier ou bien ./nom_du_fichier. Sinon veuillez indiquer le chemin complet.
    Le chemin du fichier doit forcément correspondre à un fichier régulier existant ayant l'extension csv ou txt. Il ne doit également pas être vide.
    Exemple : /mnt/c/Users/33782/Desktop/Donnees.txt
    
    \e[1;36;4mNuméro de la colonne contenant les longueurs d'ondes (colonne_longueur_onde) :\e[0m  Doit être un nombre entier strictement positif et ne doit pas être supérieur au nombre de colonnes contenues dans votre fichier.
    La première colonne de votre fichier a le numéro 1 et non le numéro 0. 
    
    \e[1;36;4mNuméro de la colonne contenant les intensitées (colonne_intensitees) :\e[0m  Doit être un nombre entier strictement positif et ne doit pas être supérieur au nombre de colonnes contenues dans votre fichier.
    La première colonne de votre fichier a le numéro 1 et non le numéro 0. 
    
    \e[1;36;4mTaille du pas (taille_fenetre) :\e[0m  Doit être un nombre strictement positif. Cela peut être un entier comme un float, cependant si vous voulez un float rentrez par exemple 12.6 et non 12,6. 

    \e[1;36;4mUnité de vos longueurs d'ondes (unite_long_onde) :\e[0m  Il n'y a pas de conditions sur ce paramètre. Il servira à spécifier l'abscisse de votre graphe.

    \e[1;36;4mUnité de vos intensités (unite_intens) :\e[0m  Il n'y a pas de conditions sur ce paramètre. Il servira à spécifier l'ordonnée de votre graphe.

    \e[1;36;4mLongueur d'onde de début d'intervalle (long_deb) :\e[0m  Doit être un nombre positif (0 autorisé). Il peut être un float comme un entier mais si vous voulez un float rentrez par exemple 128.3 et non 128,3. 
    Renseignez la dans l'unité que vous avez choisit pour le paramètre 'Unité de vos longueurs d'ondes'.

    \e[1;36;4mLongueur d'onde de fin d'intervalle (long_fin) :\e[0m  Doit être un nombe strictement positif (0 non autorisé). Il peut être un float comme un entier mais si vous voulez un float rentrez par exemple 128.3 et non 128,3.
    Renseignez la dans l'unité que vous avez choisit pour le paramètre 'Unité de vos longueurs d'ondes'.

    \e[1;36;4m Le séparateur (sep) :\e[0m La chaîne de caractère entre deux de vos valeurs numériques dans votre fichier.

    \e[1;32mPour certains paramètres vous aurez de nouvelles chances de rentrer le bon paramètre sans quitter le programme si vous vous êtes trompés.\e[0m
    "
    exit #Sortie du programme..

elif [ "$1" == "-hg" ]; then #Affichage d'une des ramifications de l'help qui est -hg pour les graphes.
    echo -e "\e[1;32mAide dédiée au graphique. Pour revenir à l'aide principale utilisez l'option -h ou bien l'option -help.\e[0m
    
    \e[1;36;4mFonctionnement du graphe :\e[0m Vous fournissez une valeur de début d'intervalle pour le graphe et une valeur de fin d'intervalle pour le graphe et vous avez précédemment défini un pas.
    Tout d'abord vos données de longueurs d'ondes et leurs intensités correspondantes sont séparées en intervalles selon le pas choisi. Si par exemple vous avez des données entre 300 et 400 nm et que vous choisissez un pas de 10 vous aurez des intervalles tels que [300,310[;[310, 320[ ... [380,390[;[390,400].
    Ensuite le programme regarde dans quel intervalle se situe votre valeur de début d'intervalle pour le graphe et garde en mémoire cette intervalle.
    Il fait ensuite de même pour votre valeur de fin d'intervalle pour le graphe.
    Ce qui sera au final affiché sur le graphe sera les intervalles dans lesquels sont contenus vos valeurs de début et de fin d'intervalle pour le graphe ainsi que tous les intervalles entre.
    
    \e[1;36;4mVotre valeur de début d'intervalle de graphe est plus petite que la plus petite donnée de longueur d'onde de votre fichier :\e[0m Alors votre graphe commencera à la plus petite donnée de longueur d'onde de votre fichier.

    \e[1;36;4mVotre valeur de fin d'intervalle de graphe est plus grande que la plus grande donnée de longueur d'onde de votre fichier :\e[0m Alors votre graphe se finira à la plus grande donnée de longueur d'onde de votre fichier.

    \e[1;36;4mVotre intervalle choisit pour le graphe n'est pas du tout contenu dans les données de votre fichier :\e[0m Si par exemple les données de votre fichier vont de 300 à 400 nm et que vous choisissez un intervalle pour le graphe de 100 à 200 nm alors le graphe affichera l'entièreté des données de votre fichier pour que vous puissiez vous rendre compte d'intervalles qui conviendrait mieux.

    \e[1;36;4m Vous voulez avoir strictement l'intervalle que vous avez choisit pour votre graphe d'affiché :\e[0m Dans ce cas vous devez initialement choisir une taille de pas de 1. 

    \e[1;36;4m La longueur d'onde de votre fin d'intervalle est plus petite que la longueur d'onde de votre début d'intervalle :\e[0m Dans ce cas vous aurez un graphe allant de votre longueur d'onde de début d'intervalle jusqu'à la plus grande valeur de longueur d'onde de vos données.

    "
    exit #Sortie du programme..
elif [ "$1" == "-ht" ]; then #Affichage d'une des ramifications de l'help qui est -ht pour le traitement des données.
    echo -e "\e[1;32mAide dédiée au traitement des données. Pour revenir à l'aide principale utilisez l'option -h ou bien l'option -help. \e[0m

    Voici quelques informations concernant le traitement des données qui ne semblent probablement pas évidentes : 

    \e[1;36;4mPremière ligne :\e[0m Votre première ligne doit obligatoirement correspondre aux noms de vos colonnes. Si vous avez vos valeurs dès la première ligne, la colonne ne traitera pas cette première ligne. Ainsi si vous n'avez qu'une ligne dans votre fichier, le programme considère que ce sont les noms de vos colonnes et que vous n'avez donc pas de données. Le fichier ne sera donc pas traité.

    \e[1;36;4mValeur de longueur d'onde sans valeur d'intensité ou vice-versa :\e[0m Impossible. Si c'est le cas l'absence de valeur sera considéré comme un 'null' et vous ne remplirez pas la condition d'avoir des données qui sont des nombres entiers ou décimaux. Vous aurez donc un message d'erreur et le programme ne s'exécutera pas.

    \n"
    exit #Sortie du programme.
elif [ "$#" -gt 0 ]; then #Affichage d'un message d'erreur si on donne un argument au programme qui n'est pas une des options et aide pour revenir à l'help.
    echo -e "\e[1;32mCe programme ne prend pas d'arguments. Si c'est l'help que vous recherchez veuillez taper chemin_du_fichier -h . \e[0m"
    exit #Sortie du programme.
fi 






#----------------------Récupération et vérification du chemin du fichier--------------------


read -p "Entrez le chemin de votre fichier: " chemin #Je demande à l'utilisateur le chemin du fichier.

#Je vérifie si ce chemin correspond à un fichier régulier qui existe :
if ! [ -f "$chemin" ]; then
    echo -e "\e[1;31mLe chemin renseigné ne correspond pas à un fichier régulier qui existe. Veuillez relancer le programme avec un chemin correct.\e[0m"
    exit
fi

#Je vérifie si c'est la bonne extension :
ext=$(echo $chemin | rev | cut -d/ -f1 | rev)
ext=$(echo $ext | rev | cut -d. -f1 | rev)
if [ "$ext" != "csv" ] && [ "$ext" != "txt" ]; then
    echo -e "\e[1;31mVotre fichier doit avoir l'extension csv ou txt\e[0m"
    exit
fi 

#Je vérifie si le fichier est vide ou pas :
taille=$(du -h "$chemin" | cut -f1)
if [ $taille == 0 ]; then
    echo -e "\e[1;31mVotre fichier est vide. Veuillez relancer le programme avec un fichier qui n'est pas vide.\e[0m"
    exit
fi



#------------------Création d'une fonction pour vérifier si une variable est un entier positif----------------------


function entier_positif {
    re='^[0-9]+$' #chaîne composée uniquement de chiffres
    if [[ $1 =~ $re && $1 -gt 0 ]]; then 
        return 0 #la chaine est un entier positif
    else 
        return 1 #la chaine n'est pas un entier positif
    fi 
}



#-----------------------Récupération et vérification de la colonne des longueurs d'ondes------------------------------


read -p "Entrez le numéro de la colonne qui contient les longueurs d'onde: " colonne_longueur_onde #Je récupère la colonne des longueurs d'onde.

somme_cl=0 #Pour savoir combien de fois l'utilisateur a déjà donné une valeur invalide.

#Je vérifie que c'est un entier strictement positif.
while ! ( entier_positif $colonne_longueur_onde ); do
    ((somme_cl+=1))
    if [ "$somme_cl" -eq 3 ]; then #Lorsqu'il a dejà fait trop de tentatives (3).
        echo -e "\e[1;31mTrop de tentatives erronées. Veuillez relancer le programme une fois que vous saurez quelle valeur rentrer.\e[0m"
        exit
    else #Sinon je lui laisse encore une chance.
        echo -e "\e[1;31mLe numéro de la colonne doit être un entier strictement positif\e[0m"
        read -p "Entrez le numéro de la colonne qui contient les longueurs d'onde: " colonne_longueur_onde
    fi 
done



#-----------------------Récupération et vérification de la colonne des intensitées------------------------------


read -p "Entrez le numéro de la colonne qui contient les intensitées: " colonne_intensitees #Je récupère la colonne des intensitées.

somme_ci=0 #Pour savoir combien de fois l'utilisateur a déjà donné une valeur invalide.

#Je vérifie que c'est un entier strictement positif
while ! ( entier_positif $colonne_intensitees ); do
    ((somme_ci+=1))
    if [ "$somme_ci" -eq 3 ]; then #Lorsqu'il a dejà fait trop de tentatives (3).
        echo -e "\e[1;31mTrop de tentatives erronées. Veuillez relancer le programme une fois que vous saurez quelle valeur rentrer.\e[0m"
        exit 
    else #Sinon je lui laisse encore une chance.
        echo -e "\e[1;31mLe numéro de la colonne doit être un entier strictement positif\e[0m"
        read -p "Entrez le numéro de la colonne qui contient les longueurs d'onde: " colonne_longueur_onde
    fi
done

#-----------------------Récupération et vérification de la taille du pas------------------------------


read -p "Entrez la taille du pas: " taille_fenetre #Je récupère la taille du pas.

somme_p=0 #Pour savoir combien de fois l'utilisateur a déjà donné une valeur invalide.

#Je vérifie que la taille du pas est un nombre entier ou un float strictement plus grand que 0.
while ! [[ $taille_fenetre =~ ^[0-9]+(\.[0-9]+)?$ && $taille_fenetre > 0 ]] ; do #=~ est la correspondance de motif
    ((somme_p+=1))
    if [ "$somme_p" -eq 3 ]; then #Lorsqu'il a dejà fait trop de tentatives (3).
        echo -e "\e[1;31mTrop de tentatives erronées. Veuillez relancer le programme une fois que vous saurez quelle valeur rentrer.\e[0m"
        exit 
    else  #Sinon je lui laisse encore une chance.
        echo -e "\e[1;31mLa taille de votre fenêtre doit être un nombre strictement positif et si vous voulez un pas de 2,6 il faut rentrer 2.6 .\e[0m"
        read -p "Entrez la taille du pas: " taille_fenetre
    fi 
done



#-----------------------Récupération des unitées pour le graphe------------------------------


#Je lui demande quelles sont ses unitées et je les récupère, il n'y a pas de vérifications particulières.
read -p "Entrez l'unité de vos longueurs d'onde: " unite_long_onde
read -p "Entrez l'unité de vos intensités: " unite_intens



#-----------------------Récupération et vérification de la longueur de début d'intervalle pour le graphe------------------------------


read -p "Entrez la longueur d'onde en $unite_long_onde de début d'intervalle pour le graphe: " long_deb #Je récupère la longueur d'onde de début d'intervalle.

somme_ld=0 #Pour savoir combien de fois l'utilisateur a déjà donné une valeur invalide.

#Je vérifie que les longueurs d'onde renseignées sont des nombres positifs (entiers ou floats accepté et 0 aussi.)
while ! [[ $long_deb =~ ^[0-9]+(\.[0-9]+)?$  && ! ( $long_deb < 0 ) ]] ; do
    ((somme_ld+=1))
    if [ "$somme_ld" -eq 3 ]; then #Lorsqu'il a dejà fait trop de tentatives (3).
        echo -e "\e[1;31mTrop de tentatives erronées. Veuillez relancer le programme une fois que vous saurez quelle valeur rentrer.\e[0m"
        exit 
    else #Sinon je lui laisse encore une chance.
        echo -e "\e[1;31mVotre longueur d'onde doit être un nombre positif. Si vous voulez une longueur d'onde de 128,3 $unite_long_onde il faut rentrer 128.3 .\e[0m"
        read -p "Entrez la longueur d'onde en $unite_long_onde de début d'intervalle: " long_deb
    fi 
done




#-----------------------Récupération et vérification de la longueur de fin d'intervalle pour le graphe------------------------------


read -p "Entrez la longueur d'onde en $unite_long_onde de fin d'intervalle pour le graphe: " long_fin #Je récupère la longueur d'onde de fin d'intervalle.

somme_lf=0 #Pour savoir combien de fois l'utilisateur a déjà donné une valeur invalide.

#Je vérifie que les longueurs d'onde renseignées sont des nombres positifs (entiers ou floats accepté et 0 aussi.)
while ! [[ $long_fin =~ ^[0-9]+(\.[0-9]+)?$  &&  ( $long_fin > 0 ) ]] ; do
    ((somme_lf+=1))
    if [ "$somme_lf" -eq 3 ]; then #Lorsqu'il a dejà fait trop de tentatives (3).
        echo -e "\e[1;31mTrop de tentatives erronées. Veuillez relancer le programme une fois que vous saurez quelle valeur rentrer.\e[0m"
        exit 
    else #Sinon je lui laisse encore une chance.
        echo "\e[1;31mVotre longueur d'onde doit être un nombre positif. Si vous voulez une longueur d'onde de 128.3 $unite_long_onde il faut rentrer 128,3 .\e[0m"
        read -p "Entrez la longueur d'onde en $unite_long_onde de début d'intervalle: " long_fin
    fi
done

#-----------------------Execution du programme------------------------------


python3 recherche_plot.py "$chemin" "$taille_fenetre" "$colonne_longueur_onde" "$colonne_intensitees" "$long_deb" "$long_fin" "$unite_long_onde" "$unite_intens"




