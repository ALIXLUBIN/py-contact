# Documentation d'utilisation de contacte.py

## Description
contacte.py est un programme qui permet de gérer une liste de managers. Il peut être utilisé de deux manières différentes: avec des arguments l'ors de l'execution ou bien en ligne de commande ou via un dialoge interactif.

> ce program utilise la dépendence tabulate il faut donc l'installer  `pip install tabulate`

## Utilisation avec des arguments en ligne de commande

> il est important de noter que les ==espaces== ne peuvent pas être utilsier dans un même argument

Le programme peut être appelé avec les arguments suivants:

- `add`: ajoute un nouveau manager à la liste. Les sous-arguments requis sont le nom, le prenom, l'e-mail et le numéro de téléphone du manager, un pseudo peux être ajouter si vous le shouaitez. Exemple: `python.exe .\contacte.py add -name John -surname Doe -email johndoe@example.com -phone 0673971175 -address 104-rue-des-merisier`

- `display`: affiche tous les managers actuellement enregistrés. Aucun sous-argument n'est requis. Exemple: `python.exe .\contacte.py display`

- `edit`: met à jour les informations d'un manager existant. Le sous-arguments requis est l'identifiant du manager et les nouvelles informations (nom, e-mail et/ou numéro de téléphone). Exemple: `python.exe .\contacte.py edit -id 4 -name John -email newemail@example.com`

- `search`: recherche un manager par le filtre que vous souhaitez et affiche ses informations. il utilise les même sous argument que `add` Exemple: `python.exe .\contacte.py search -name John -email newemail@example.com` affiche tout les manager avec le nom Jhon et l'email newemail@example.com

- `delete`: supprime un manager de la liste. Le sous-argument requis est l'identifiant du manager à supprimer. Exemple: `python.exe .\contacte.py delete -id 5`

## Utilisation avec le prompt interactif
Si le programme est lancé sans arguments, un prompt interactif s'affichera. Le menu principal offrira les options suivantes:

`1. Ajouter un manager`
`2. Afficher tous les managers`
`3. Mettre à jour un manager`
`4. Supprimer un manager`
`5. Quitter le programme`

il suffit de répondre avec le numéro de l'action souhaiter
Pour chaque option, le programme demandera les informations nécessaires (nom, e-mail, numéro de téléphone, etc.) et effectuera l'action correspondante.

### Ajout d'un manager

Pour ajouter un manager il faut donc faire le choix numéro `1` demanderas :

- Le prénom
- Le Nom
- Le Pseudo qui est optionnel
- L'addresse email
- L'adresse postale

#### Exemple d'utilisation
Pour ajouter un manager nommé "Jane Doe" avec l'e-mail "janedoe@example.com" et le numéro de téléphone "0785754598" et l'addresse "10-Rue-des-chemin", vous pouvez utiliser le numéro 1 et vous demanderas les inforamtion suivante se qui donneras le résultat suivant :

`Entrez votre choix : 1`
`Entrez le prénom du manager : Jane`
`Entrez le nom du manager : Doe`
`Entrez le pseudo de famille du manager (optionnel) :`
`Entrez l'adresse email du manager : janedoe@example.com`
`Entrez le numéro de téléphone du manager : 0785754598`
`Entrez l'adresse du manager : 10-Rue-des-chemin`
`Manager ajouté avec succès.`

### Affichage des managers

Pour afficher la liste de tous les managers enregistrés, choisissez l'option `2` dans le menu principal. Vous pourrez ensuite utiliser un filtre pour afficher uniquement les managers correspondant à certains critères. Pour cela, choisissez l'option correspondant au critère que vous souhaitez filtrer (nom, nom de famille, pseudo, numéro de téléphone, e-mail ou adresse) et suivez les instructions pour entrer la valeur de recherche.

### Mise à jour d'un manager

Pour mettre à jour les informations d'un manager enregistré, choisissez l'option `3` dans le menu principal, entrez l'identifant et suivez les instructions pour modifier les inforamtion du manager que vous souhaitez mettre à jour. Si vous ne souhaitez pas modifier une information, laissez-les vide.

### Suppression d'un manager

Pour supprimer un manager enregistré, choisissez l'option `4` dans le menu principal,  entrez l'identifant  du manager que vous souhaitez supprimer et suivez les instructions. Vous serez invité à confirmer votre choix avant que le manager ne soit supprimé.

### Quitter le programme
Pour quitter le programme, choisissez l'option `5` dans le menu principal.

Nous espérons que ce gestionnaire de manager vous sera utile !