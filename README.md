# Projet-Systeme-M1
Première version :

Ce programme indexe les intensités par fenêtres de longueurs d'ondes selon une taille de pas que vous lui renseigné. Il permet aussi d'afficher un graphe des intensités en fonction des longueurs d'ondes pour un intervalle fourni.

#blabla doit être contenu dans le même répertoire.

Ce programme ne nécessite pas d'arguments, cependant si vous lui en mettez qui n'est pas une option il affichera un message d'erreur et vous indiquera comment accéder à l'aide du programme. 

--Aide
Ce programme vient avec une aide qui est divisée en plusieurs catégories pour ne pas noyer l'utilisateur sous les informations ainsi si vous tapez le chemin du fichier suivi de l'option sous la forme -option vous pourrez avoir accès à ces aides. 

-h : Aide qui affiche l'aide générale du programme visant à vous renseigner sur les sous-catégories d'aide.
-help : Aide qui affiche l'aide générale du programme visang à vous renseigner sur les sous-catégories d'aide, similaire à -h.
-hp : Aide qui vous permet d'accéder à l'aide dédier aux paramètres. Cette aide liste tous les paramètres du programme ainsi que leurs conditions que vous devez vérifier pour le bon fonctionnement du programme.
-hg : Aide dédiée au graphique. Elle vous expliquera la manière dont est tracée le graphe et ce qui se passera dans certains cas spécifiques. Par exemple lorsque l'intervalle choisit pour le graphe n'est pas du tout contenu dans les données de votre fichier.
-ht : Aide dédiée au traitement des données. Vous donne quelques renseignements sur le format que doit avoir votre fichier.


--Paramètres
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


--SOS :

Comment trouver le chemin de mon fichier ?

Comment savoir quel est mon séparateur ?
