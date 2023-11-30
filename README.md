# Projet-Systeme-M1
Première version :

Ce programme indexe les intensités par fenêtres de longueurs d'ondes selon une taille de pas que vous lui renseigné. Il permet aussi d'afficher un graphe des intensités en fonction des longueurs d'ondes pour un intervalle fourni.

#blabla doit être contenu dans le même répertoire.

Ce programme ne nécessite pas d'arguments, cependant si vous lui en mettez qui n'est pas une option il affichera un message d'erreur et vous indiquera comment accéder à l'aide du programme. 

--fichiers du projet--

main.sh : Ce fichier est entièrement codé en bash et sert principalement à deux choses : récupérer et vérifier les paramètres nécessaires aux autres fichiers et donner les paramètres nécessaires à ces fichiers pour que recherche_plot.py faisant appel à intensite.py puisse s'exécuter. Ce fichier est commenté.

intensite.py : Ce fichier est entièrement codé en python3 . Il sert à récupérer vos données et à les traiter. A partir de vos données il créera un dictionnaire et une liste. La liste servira au fichier recherche_plot.py tandis que le dictionnaire servira à l'affichage de vos valeurs. En effet en fin d'exécution ce fichier affichera les commentaires de votre fichier suivit des intervalles de votre dictionnaire selon le pas choisit préalablement et certaines informations utiles sur ces intervalles. Ce fichier est commenté.

--Modules utilisés--

Les modules des bibliothèques python utilisés dans les différents fichiers sont les suivants : sys, os, re, matplotlib.

--Aide--
Ce programme vient avec une aide qui est divisée en plusieurs catégories pour ne pas noyer l'utilisateur sous les informations ainsi si vous tapez le chemin du fichier suivi de l'option sous la forme -option vous pourrez avoir accès à ces aides. 

-h : Aide qui affiche l'aide générale du programme visant à vous renseigner sur les sous-catégories d'aide.
-help : Aide qui affiche l'aide générale du programme visang à vous renseigner sur les sous-catégories d'aide, similaire à -h.
-hp : Aide qui vous permet d'accéder à l'aide dédier aux paramètres. Cette aide liste tous les paramètres du programme ainsi que leurs conditions que vous devez vérifier pour le bon fonctionnement du programme.
-hg : Aide dédiée au graphique. Elle vous expliquera la manière dont est tracée le graphe et ce qui se passera dans certains cas spécifiques. Par exemple lorsque l'intervalle choisit pour le graphe n'est pas du tout contenu dans les données de votre fichier.
-ht : Aide dédiée au traitement des données. Vous donne quelques renseignements sur le format que doit avoir votre fichier.


--Paramètres--
Voici une liste des paramètres du programme ainsi que des conditions qu'ils doivent respecter. Vous retrouverez cette liste dans l'option -hp.

Chemin du fichier (chemin) : Si vous êtes actuellement dans le répertoire ou se trouve votre fichier vous pouvez simplement mettre le nom du fichier ou bien ./nom_du_fichier. Sinon mettez le chemin complet depuis la racine.
Le chemin du fichier doit forcément correspondre à un fichier régulier existant ayant l'extension csv ou text. Vous ne pouvez pas renseigner un fichier vide.
Exemple de chemin : /mnt/c/Users/33782/Desktop/Donnees.txt

Numéro de la colonne de votre fichier contenant les longueurs d'ondes (colonne_longueur_onde) : Doit être un nombre entier strictement positif et ne doit pas être supérieur au nombre de colonnes contenues dans votre fichier.
La première colonne de votre fichier a le numéro 1 et non le numéro 0. 

Numéro de la colonne de votre fichier contenant les intensitées (colonne_intensitees) : Doit être un nombre entier strictement positif et ne doit pas être supérieur au nombre de colonnes contenues dans votre fichier.
La première colonne de votre fichier a le numéro 1 et non le numéro 0.

Taille du pas pour vos intervalles (taille_fenetre) : Doit être un nombre strictement positif mais peut être entier comme décimal. Si vous voulez un nombre décimal rentrez par exemple la valeur 28.3 et non 28,3 . 

Unité de vos longueurs d'ondes (unite_long_onde) : Il n'y a pas de conditions sur ce paramètres, vous pouvez mettre ce qu'il vous plaira. Il ne servira qu'à l'affichage de votre graphe.

Unité de vos intensitées (unite_intens) : Il n'y a pas de conditions sur ce paramètre, vous pouvez mettre ce qu'il vous plaira. Il ne servira qu'à l'affichage de votre graphe.

Longueur d'onde de début d'intervalle de votre graphe (long_deb) : Doit être un nombre positif (0 autorisé) et peut être un entier comme un décimal. Comme pour la taille du pas si vous voulez rentrez une valeur décimal veuillez rentrer par exemple la valeur 127.9 et non 127,9. Cette valeur de longueur d'onde doit être renseignée dans l'unité que vous avez choisit pour unite_long_onde.

Longueur d'onde de fin d'intervalle de votre graphe (long_fin) : Doit être un nombre strictement positif (0 non autorisé) et peut être un entier comme un décimal. Comme pour la taille du pas si vous voulez rentrez une valeur décimal veuillez rentrer par exemple la valeur 127.9 et non 127,9. Cette valeur de longueur d'onde doit être renseignée dans l'unité que vous avez choisit pour unite_long_onde.

Le séparateur (sep) : Correspond à la chaîne de caractères entre deux de vos valeurs numériques dans votre fichier. Faites attention de ne pas oublier les guillemets " . Il vous sera demandé en amont si votre séparateur est par défaut un espace ou une tabulation.

Grâce à cette liste vous pouvez avoir une idées des informations qu'il vout faut connaître en amont d'exécuter le programme. Cependant pas d'inquiétudes, pour certains paramètres comme par exemple la taille du pas, si vous rentrez dans le programme une valeur invalide, celui-ci vous donnera 2 autres chances de rectifier votre valeur en vous rappelant les conditions que doit respecter votre paramètre. Si au bout des 2 chances vous ne lui aurez toujours pas donné une valeur valide alors le programme prendera fin avec un message d'erreur.

--Traitement du fichier--

Si vous avez un commentaire en début de votre fichier et que vous souhaitez qu'il soit correctement affichés avec les caractères du type : é,è,à...etc. Alors veillez à ce que votre fichier soit encodé en utf-8. 

Il vous sera demandé si la première ligne de votre fichier (hors commentaires) correspond aux noms de vos colonnes. Si vous répondez oui alors cette première ligne ne sera pas traitée. Autrement elle le sera. Si vous dites non (N) alors que vous avez bel et bien des noms à vos colonnes cela risque d'entraîner des messages d'erreurs ou bien de fausser vos résultats. Faites attention.
Si vous dites que vous avez des noms à vos colonnes (Y) et que vous n'avez qu'une ligne dans votre fichier en tout et pour tout (hors commentaire) alors le programme considèrera que vous n'avez pas de données et affichera un message d'erreur avant d'arrêter de s'éxécuter.

Si vous voulez ajouter des lignes de commentaires dans votre fichier, ces dernières seront affichées comme premiers résultats du programme comme rappel. Cependant ces lignes de commentaires doivent automatiquement être précédées du caractère # . 
De même les lignes commençant par > ne seront pas prises en compte pour faciliter l'usage de certains logiciels. Mais ces lignes ne seront pas considérées comme des commentaires.

Pendant le traitement du fichier une vérification de type sera effectuée. En effet si les données que vous avez indiquées pour longueurs d'onde et les intensités ne sont pas des nombres (entiers ou décimaux) alors un message d'erreur sera afficher et le programme ne s'exécutera pas. Veillez à ce que toutes vos données soient bien numériques.
De même il ne sera pas accepté que vous aillez une longueur d'onde mais pas d'intensitée correspondante ou vice-versa.

Il n'est pas nécessaire de trier vos longueur d'ondes dans un ordre croissante préalablement car le programme le fera automatiquement et ce sans pour autant mélanger les intensitées correspondantes. 

A partir de vos données et de la taille du pas (taille_fenetre) fournit préalablement un dictionnaire sera créé. Ce dictionnaira aura pour clé les intervalles de taille choisit et pour valeur les intensités des longueurs d'ondes situées dans ces intervalles triées dans un ordre croissant. Pour tous les intervalles sauf le dernier, la dernière valeur de longueur d'onde est exclus, ainsi il n'y aura pas de doublons.
Le premier intervalle commence à la première donnée de votre fichier mais la réciproque n'est pas vraie pour le dernier intervalle.
Suite à vos commentaires sera affiché votre dictionnaire avec pour chaque intervalle le nombre de données d'intensitées, le minimum de ces données, le maximum et la moyenne. 
Si il existe des intervalles sans données correspondantes dans votre fichier alors le nombre de données d'intensitées affichera "Aucunes" et les autres informations "null" mais cela n'affectera pas les autres intervalles contenant des valeurs.

--Mon graphe--

Fonctionnement du graphe : Vous fournissez une valeur de début d'intervalle pour le graphe et une valeur de fin d'intervalle pour le graphe et vous avez précédemment défini un pas. Tout d'abord vos données de longueurs d'ondes et leurs intensités correspondantes sont séparées en intervalles selon le pas choisi. Si par exemple vous avez des données entre 300 et 400 nm et que vous choisissez un pas de 10 vous aurez des intervalles tels que [300,310[;[310, 320[ ... [380,390[;[390,400]. 
Ensuite dans le fichier recherche_plot.py le programme regarde dans quel intervalle se situe votre valeur de début d'intervalle pour le graphe et garde en mémoire cette intervalle. Il fait ensuite de même pour votre valeur de fin d'intervalle pour le graphe.
Ce qui sera au final affiché sur le graphe sera les intervalles dans lesquels sont contenus vos valeurs de début et de fin d'intervalle pour le graphe ainsi que tous les intervalles entre.

--SOS--

Comment trouver le chemin de mon fichier ?

Comment savoir quel est mon séparateur ?

Comment savoir comment est encodé mon fichier ?
