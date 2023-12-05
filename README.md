# Projet-Systeme-M1

Ce programme traite un fichier que vous lui renseignez contenant des longueurs d'onde et des intensités correspondantes. Il indexe dans un dictionnaire les intensités par fenêtres de longueurs d'onde selon une taille de pas que vous lui renseignez. Il permet aussi d'afficher un graphe des intensités en fonction des longueurs d'onde pour un intervalle fourni en prenant en compte les intervalles de votre dictionnaire.

:small_blue_diamond: Les fichiers **main.sh**, **intensite.py** et **recherche_plot.py** doivent être enregistrés dans le même répertoire/dossier. Ce n'est cependant pas une obligation pour le fichier que vous souhaitez traiter.  <br>
Pour lancer le programme allez dans votre terminal, puis tapez le chemin du fichier main.sh. Si vous êtes dans le répertoire où ce dernier est enregistré vous pouvez juste taper **./main.sh** 

:small_blue_diamond: Ce programme ne nécessite pas d'arguments, cependant si vous lui en mettez un qui n'est pas une option il affichera un message d'erreur et vous indiquera comment accéder à l'aide du programme. 

## :page_facing_up: Fichiers du projet 

**main.sh** : Ce fichier est entièrement codé en bash et sert principalement à deux choses : récupérer et vérifier les paramètres nécessaires aux autres fichiers, puis les donner à recherche_plot.py qui fera appel à intensite.py. Ce fichier est commenté.

**intensite.py** : Ce fichier est entièrement codé en python3 . Il sert à récupérer vos données et à les traiter. A partir de vos données il créera un dictionnaire et une liste. La liste servira au fichier recherche_plot.py tandis que le dictionnaire servira à l'affichage de vos valeurs. En effet en fin d'exécution ce fichier affichera les commentaires de votre fichier suivit des intervalles de votre dictionnaire (créés à l'aide du pas choisit préalablement). Vous aurez quelques informations complémentaires pour chaque intervalle. Ce fichier est commenté.

**recherche_plot.py** : Ce fichier est entièrement codé en python3. Il sert à réaliser une représentation graphique de l'intervalle de longueurs d'onde que vous aurez renseigné en prenant en compte la taille du pas que vous avez choisit pour vos intervalles. Ce fichier est commenté.

## :books: Modules utilisés

Les modules utilisés dans les différents fichiers sont les suivants : **sys**, **os**, **re**, **matplotlib**.

## :loudspeaker: Aide
Ce programme vient avec une aide qui est divisée en plusieurs catégories pour ne pas noyer l'utilisateur sous les informations. Ainsi, si vous tapez le chemin du fichier suivi de l'option vous pourrez avoir accès à ces aides. <br>
Exemple d'utilisation : ./main.sh -help

**-h** : Aide qui affiche l'aide générale du programme visant à vous renseigner sur les sous-catégories d'aide.  <br>
**-help** : Aide qui affiche l'aide générale du programme visang à vous renseigner sur les sous-catégories d'aide, similaire à -h.  <br>
**-hp** : Aide qui vous permet d'accéder à l'aide dédiée aux paramètres. Cette aide liste tous les paramètres du programme ainsi que leurs conditions que vous devez vérifier pour le bon fonctionnement du programme.  <br>
**-hg** : Aide dédiée au graphique. Elle vous expliquera la manière dont est tracée le graphe et ce qui se passera dans certains cas spécifiques. Par exemple lorsque l'intervalle choisit pour le graphe n'est pas du tout contenu dans les données de votre fichier.  <br>
**-ht** : Aide dédiée au traitement des données. Vous donne quelques renseignements sur le format que doit avoir votre fichier.


## :gear: Paramètres
Voici une liste des paramètres du programme ainsi que des conditions qu'ils doivent respecter. Vous retrouverez cette liste dans l'option -hp.

**Chemin du fichier (chemin) :** Si vous êtes actuellement dans le répertoire ou se trouve votre fichier vous pouvez simplement mettre le nom du fichier ou bien ./nom_du_fichier. Sinon mettez le chemin complet depuis la racine.  <br>
Le chemin du fichier doit forcément correspondre à un fichier régulier existant ayant l'extension csv ou txt. Vous ne pouvez pas renseigner un fichier vide.  <br>
Exemple de chemin : /mnt/c/Users/33782/Desktop/Donnees.txt

**Numéro de la colonne de votre fichier contenant les longueurs d'onde (colonne_longueur_onde) :** Doit être un nombre entier strictement positif et ne doit pas être supérieur au nombre de colonnes contenues dans votre fichier.  <br>
La première colonne de votre fichier a le numéro 1 et non le numéro 0.   

**Numéro de la colonne de votre fichier contenant les intensitées (colonne_intensitees) :** Doit être un nombre entier strictement positif et ne doit pas être supérieur au nombre de colonnes contenues dans votre fichier.  <br>
La première colonne de votre fichier a le numéro 1 et non le numéro 0.  

**Taille du pas pour vos intervalles (taille_fenetre) :** Doit être un nombre strictement positif mais peut être entier comme décimal. Si vous voulez un nombre décimal rentrez par exemple la valeur 28.3 et non 28,3 . 

**Unité de vos longueurs d'ondes (unite_long_onde) :** Il n'y a pas de conditions sur ce paramètre, vous pouvez mettre ce qu'il vous plaira. Il ne servira qu'à l'affichage de votre graphe.

**Unité de vos intensitées (unite_intens) :** Il n'y a pas de conditions sur ce paramètre, vous pouvez mettre ce qu'il vous plaira. Il ne servira qu'à l'affichage de votre graphe.

**Longueur d'onde de début d'intervalle de votre graphe (long_deb) :** Doit être un nombre positif (0 autorisé) et peut être un entier comme un décimal. Comme pour la taille du pas si vous voulez rentrer une valeur décimal veuillez rentrer par exemple la valeur 127.9 et non 127,9. Cette valeur de longueur d'onde doit être renseignée dans l'unité que vous avez choisie pour unite_long_onde.

**Longueur d'onde de fin d'intervalle de votre graphe (long_fin) :** Doit être un nombre strictement positif (0 non autorisé) et peut être un entier comme un décimal. Comme pour la taille du pas si vous voulez rentrer une valeur décimal veuillez rentrer par exemple la valeur 127.9 et non 127,9. Cette valeur de longueur d'onde doit être renseignée dans l'unité que vous avez choisie pour unite_long_onde.

**Le séparateur (sep) :** Correspond à la chaîne de caractères entre deux de vos valeurs numériques dans votre fichier. Faites attention de ne pas oublier les guillemets " . Il vous sera demandé en amont si votre séparateur est par défaut un espace ou une tabulation.
 
Grâce à cette liste vous pouvez avoir une idée des informations qu'il vout faut connaître en amont d'exécuter le programme. Cependant pas d'inquiétudes, pour certains paramètres, comme par exemple la taille du pas, si vous rentrez dans le programme une valeur invalide celui-ci vous donnera 2 autres chances de rectifier votre valeur en vous rappelant les conditions que doit respecter votre paramètre. Si au bout des 2 chances vous ne lui avez toujours pas donné une valeur valide alors le programme prendra fin avec un message d'erreur.

## :bookmark_tabs: Traitement du fichier

:small_blue_diamond: Si vous avez un commentaire en début de votre fichier et que vous souhaitez qu'il soit correctement affiché avec les caractères du type : é,è,à...etc, alors veillez à ce que votre fichier soit encodé en utf-8. 

:small_blue_diamond: Il vous sera demandé si la première ligne de votre fichier (hors commentaires) correspond aux noms de vos colonnes. Si vous répondez oui alors cette première ligne ne sera pas traitée. Autrement elle le sera. Si vous dites non (N) alors que vous avez bel et bien des noms à vos colonnes cela risque d'entraîner des messages d'erreurs ou bien de fausser vos résultats. Faites attention.  <br>
Si vous dites que vous avez des noms à vos colonnes (Y) et que vous n'avez qu'une ligne dans votre fichier en tout et pour tout (hors commentaire) alors le programme considèrera que vous n'avez pas de données et affichera un message d'erreur avant d'arrêter de s'éxécuter.

:small_blue_diamond: Si vous voulez ajouter des lignes de commentaires dans votre fichier, ces dernières seront affichées comme premiers résultats du programme. Cependant ces lignes de commentaires doivent automatiquement être précédées du caractère # .  <br> 
De même les lignes commençant par > ne seront pas prises en compte pour faciliter l'usage de certains logiciels. Ces lignes ne seront pas pour autant considérées comme des commentaires.

:small_blue_diamond: Pendant le traitement du fichier une vérification de type sera effectuée. En effet si les données que vous avez indiquées pour longueurs d'onde et les intensités ne sont pas des nombres (entiers ou décimaux) alors un message d'erreur sera affiché et le programme ne s'exécutera pas. Veillez à ce que toutes vos données des colonnes choisies soient bien numériques.  <br>
De même il ne sera pas accepté que vous aillez une longueur d'onde mais pas d'intensité correspondante ou vice-versa.

:small_blue_diamond: Il n'est pas nécessaire de trier vos longueur d'ondes dans un ordre croissant préalablement car le programme le fera automatiquement et ce sans pour autant mélanger les intensités correspondantes. 

:small_blue_diamond: A partir de vos données et de la taille du pas (taille_fenetre) fournit préalablement un dictionnaire sera créé. Ce dictionnaira aura pour clé les intervalles de taille choisie et pour valeur les intensités des longueurs d'onde situées dans ces intervalles triées dans un ordre croissant. Pour tous les intervalles sauf le dernier, la dernière valeur de longueur d'onde est exclus, ainsi il n'y aura pas de doublons.  <br>
Le premier intervalle commence à la première donnée de votre fichier mais la réciproque n'est pas vraie pour le dernier intervalle.  <br>
Suite à vos commentaires sera affiché votre dictionnaire avec pour chaque intervalle le nombre de données d'intensités, le minimum de ces données, le maximum et la moyenne.   <br>
Si il existe des intervalles sans données correspondantes dans votre fichier alors le nombre de données d'intensités affichera "Aucunes" et les autres informations "null" mais cela n'affectera pas les autres intervalles contenant des valeurs.

## :chart_with_upwards_trend: Mon graphe

**Fonctionnement du graphe :** Vous fournissez une valeur de début d'intervalle pour le graphe et une valeur de fin d'intervalle pour le graphe et vous avez précédemment défini un pas. Tout d'abord vos données de longueurs d'ondes et leurs intensités correspondantes sont séparées en intervalles selon le pas choisi. Si par exemple vous avez des données entre 300 et 400 nm et que vous choisissez un pas de 10 vous aurez des intervalles tels que [300,310[;[310, 320[ ... [380,390[;[390,400].   <br>
Ensuite dans le fichier recherche_plot.py le programme regarde dans quel intervalle se situe votre valeur de début d'intervalle pour le graphe et garde en mémoire cet intervalle. Il fait ensuite de même pour votre valeur de fin d'intervalle pour le graphe.  
Ce qui sera au final affiché sur le graphe seront les intervalles dans lesquels sont contenus vos valeurs de début et de fin d'intervalle pour le graphe ainsi que tous les intervalles entre.  

:small_blue_diamond: Il vous sera demandé si vous souhaitez afficher des données relatives à votre graphe (valeur max de longueur d'onde et d'intensité, valeur min de longueur d'onde et d'intensité, moyenne de l'intensité et moyenne de la longueur d'onde). Vous n'aurez qu'à répondre par oui (Y) ou non (N). 

:small_blue_diamond: Il vous sera aussi demandé si vous souhaitez afficher votre graphe sous la forme de points non reliés (scatter), vous n'aurez à nouveau qu'à répondre oui (Y) ou non (N). Si vous répondez non alors votre graphe sera affiché sous la forme d'une courbe continue violette.

:small_blue_diamond: Le graphe possédera une grille afin que vous puissiez plus facilement réaliser une étude visuelle. <br>
Il possédera également un nom d'abscisse, un nom d'ordonnée et un titre. 

:small_blue_diamond: Si votre valeur de début d'intervalle de graphe est plus petite que la plus petite donnée de longueur d'onde de votre fichier alors par défaut votre graphe commencera à la plus petite donnée de longueur d'onde de votre fichier.  <br>
De manière similaire si votre valeur de fin d'intervalle de graphe est plus grande que la plus grande donnée de longueur d'onde de votre fichier alors par défaut votre graphe se finira à la plus grande donnée de longueur d'onde de votre fichier.

:small_blue_diamond: Si votre intervalle choisit pour le graphe n'est pas du tout contenu dans les données de votre fichier alors le graphe montrera l'entièreté de vos données pour que vous puissez vous rendre compte d'intervalles qui correspondrait mieux à vos données.

:small_blue_diamond: Si vous voulez avoir strictement l'intervalle que vous avez choisi de tracer alors vous devez choisir un pas de 1 pour vos intervalles de dictionnaire.De plus si vous voulez un intervalle de 500 à 600 par exemple vous devez mettre 599 comme valeur de fin d'intervalle. En effet, exception faites du dernier intervalle, les intervalles sont semi-ouverts.

:small_blue_diamond: Si vous choisissez une longueur d'onde de fin d'intervalle plus petite que la longueur d'onde de votre début d'intervalle alors vous aurez un graphe allant de l'intervalle de dictionnaire contenant votre longueur d'onde de début d'intervalle jusqu'à la plus grande valeur de longueur d'onde de vos données.


## :telephone: SOS

**Comment trouver le chemin de mon fichier ?**

:small_blue_diamond: Si vous êtez sous Windows alors ouvrez l'explorateur de fichiers et allez jusqu'à l'emplacement du fichier. Ensuite faites un clic droit sur le fichier et sélectionnez "Propriétés". Dans l'onglet "Général" vous verrez le chemin complet du fichier sous "Emplacement".

:small_blue_diamond: Si vous êtes sous macOs ou Linux alors vous pouvez ouvrir le terminal puis utiliser la commande "cd" pour naviguer jusqu'au répertoire du fichier. Tapez alors "pwd" pour afficher le chemin du répertoire actuel. Vous n'aurez plus qu'à y ajouter le nom du fichier à la fin pour obtenir son chemin complet.

**Comment savoir quel est mon séparateur ?**

Ouvrez votre fichier csv ou txt dans un éditeur de texte comme Notepad sur Windows ou bien TextEdit sur macOS. Si vos valeurs sur une même ligne sont séparées par des caractères spécifiques autre que l'espace ou la tabulation alors ces caractères sont votre séparateur. Attention à ne pas oublier les guillemets s'il y en a. <br>
Exemple de séparateur : , ou bien encore "," 

**Comment savoir comment est encodé mon fichier ?**

Ouvrez votre fichier csv ou txt dans un éditeur de texte comme Notepad sur Windows ou bien TextEdit sur macOS. La plupart des éditeurs de texte affichent l'encodage du fichier dans la barre d'état ou dans un menu déroulant. Vous devez chercher des termes comme "Encodage", "Charset" ou bien "Character Set".   <br>
Si votre fichier est un txt ou un csv et n'est pas encodé en utf-8 ce n'est pas dramatique. Vos commentaires ne seront juste pas très esthétiques.

## Exemples de résultats du programme.

Pour un fichier nommé par exemple Spectre_photoluminescence.txt, qui a des valeurs de longueurs d'onde dans la première colonne et des valeurs d'intensités dans la deuxième colonne et dont le séparateur est "," je choisis les paramètres suivant : 

:small_blue_diamond: Taille du pas : 10.5 <br>
:small_blue_diamond: Unité des longueurs d'onde : nm <br>
:small_blue_diamond: Unité des intensités : A <br>
:small_blue_diamond: Longueur d'onde en nm de début d'intervalle pour le graphe : 410.9 <br>
:small_blue_diamond: Longueur d'onde en nm de fin d'intervalle pour le graphe : 508.7 <br>
:small_blue_diamond: Si votre séparateur est un espace ou une tabulation tapez Y sinon tapez N : N <br>
:small_blue_diamond: Le séparateur est la chaîne de caractère entre deux valeurs numériques. Si votre séparateur est une tabulation ou un espace mettez None. Faites attention à mettre les guillemets si il y en a. Entrez le séparateur: "," <br>
:small_blue_diamond: Si la première ligne de vos données correspond aux noms de vos colonnes et qu'elle n'est pas mise en commentaire (avec le #) tapez Y, sinon tapez N : N <br>

![Exemple d'affichage de votre commentaire](<img width="845" alt="image" src="https://github.com/Kurolycka/Projet-Systeme-M1/assets/150124061/dcabf9fa-a4b3-4dc5-ad97-5948bee88593">)

![Exemple d'affichage de votre dictionnaire d'intervalles](<img width="274" alt="image" src="https://github.com/Kurolycka/Projet-Systeme-M1/assets/150124061/58851816-1572-40a4-8d6c-6acee6986547">)

:small_blue_diamond: Voulez vous afficher les données (minimum, maximum...) correspondant au graphe ? Si oui tapez Y sinon tapez N: Y

![Exemple d'affichage des données spécifiques au graphe](<img width="785" alt="image" src="https://github.com/Kurolycka/Projet-Systeme-M1/assets/150124061/33f41f32-6c7a-4590-84e5-2d951f71030f">)

Si vous voulez afficher le graphe sous forme de points non reliés tapez Y, sinon tapez N: N

![Exemple d'affichage du graphe](https://github.com/Kurolycka/Projet-Systeme-M1/assets/150124061/8a1a6459-6e4c-48eb-b901-1a6aec091e6a)


## :pen: Autrice du programme

L'entièreté de ce programme a été écrite par Manon NOLOT, dans le cadre d'un projet de Système du master de Physique Numérique de l'université de Montpellier. 
