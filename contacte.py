import sqlite3
from tabulate import tabulate
import argparse

con = sqlite3.connect('manager.db')
cur = con.cursor()

# Création de la table managers
cur.execute('''CREATE TABLE IF NOT EXISTS  "manager" (
						"id"	INTEGER,
						"name"	TEXT NOT NULL,
						"surname"	TEXT NOT NULL,
						"nickname"	TEXT,
						"phone"	TEXT NOT NULL,
						"email"	TEXT NOT NULL,
						"address"	TEXT NOT NULL,
						PRIMARY KEY("id" AUTOINCREMENT)
						);'''
          )

def addManager(name, surname, nickname, phone, email, address) :
  cur.execute('''INSERT INTO manager (name, surname, nickname, phone, email, address)
                VALUES (?, ?, ?, ?, ?, ?)''', (name, surname, nickname, phone, email, address))
  con.commit()
  print("Manager ajouté avec succès.")

def displayManager() :
  result = cur.execute('''SELECT * FROM manager''').fetchall()
  len_res = len(result)
  if len_res == 0 and filter == None:
    print('Aucun manager n\'est enregister pour le moment')
  else :
    print("Il y a %s mananger" % (len_res))
    print(tabulate( result, headers=['identifiant', 'name', 'surname', 'nickname', 'phone', 'email', 'address']))

def editMnager(id, clause):

  sql = "UPDATE manager SET "
  set = ''
  for key, value in clause.items():
    if value != None:
      set += '%s=\'%s\',' % (key, value)
  sql = sql + set[:-1] + " Where id=?"
  cur.execute(sql, (id))
  con.commit()
  filter({'id': id})

def deleteManager(id):
    cur.execute('''DELETE FROM manager WHERE id=?''', (id,))
    con.commit()
    if cur.rowcount > 0:
      print(f"Suppression du manager avec ID {id} réussie.")
    else:
      print(f"Aucun manager avec l'ID {id} n'a été trouvé.")

def filter(clause):
  sql = "SELECT * FROM manager WHERE "
  set = ''
  for key, value in clause.items():
    if value != None:
      set += '%s=\'%s\' AND ' % (key, value)
  sql = sql + set[:-4]
  print(sql)
  result = cur.execute(sql).fetchall()
  if len(result) == 0:
    print('Aucun manager ne correspond à vos filtre')
    return False
  else:
    print(tabulate( result, headers=['identifiant', 'name', 'surname', 'nickname', 'phone', 'email', 'address']))
    if len(result) == 1:
      return result[0][0]

    return clause

# Gestion de l'exec avec argument
parser = argparse.ArgumentParser(description='Gestionnaire des manager.')
subparsers = parser.add_subparsers(dest='command')

parser_search = subparsers.add_parser('search', help='Rechercher un manager. (plusieurs argument peuvent être tuiliser en même temps)')
parser_search.add_argument('-name', required=False, help='Nom du manager à rechercher.')
parser_search.add_argument('-surname', required=False, help='Nom de Famille du manager à rechercher.')
parser_search.add_argument('-nickname', required=False, help='pseudo du manager à rechercher.')
parser_search.add_argument('-phone', required=False, help='Numéro de tel du manager à rechercher.')
parser_search.add_argument('-email', required=False, help='Email du manager à rechercher.')
parser_search.add_argument('-address', required=False, help='Addresse du manager à rechercher.')
parser_search.add_argument('-id', required=False, help='identifiant du manager à rechercher.')

parser_add = subparsers.add_parser('add', help='ajouter un manager.')
parser_add.add_argument('-name', required=True, help='Nom du manager à ajouter.')
parser_add.add_argument('-surname', required=True, help='Nom de Famille du manager à ajouter.')
parser_add.add_argument('-nickname', required=False, help='pseudo du manager à ajouter.')
parser_add.add_argument('-phone', required=True, help='Numéro de tel du manager à ajouter.')
parser_add.add_argument('-email', required=True, help='Email du manager à ajouter.')
parser_add.add_argument('-address', required=True, help='Addresse du manager à ajouter.')

parser_delete = subparsers.add_parser('delete', help='Supprimer un manager.')
parser_delete.add_argument('-id', required=True, help='identifiant du manager à supprimer.')

parser_display = subparsers.add_parser('display', help='Afficher tout managers.')

parser_edit = subparsers.add_parser('edit', help='Rechercher un manager. (plusieurs argument peuvent être tuiliser en même temps)')
parser_edit.add_argument('-id', required=True, help='identifiant du manager à modifier.')
parser_edit.add_argument('-name', required=False, help='Nouveau Nom du manager.')
parser_edit.add_argument('-surname', required=False, help='Nouveau Nom de Famille du manager.')
parser_edit.add_argument('-nickname', required=False, help='Nouveau pseudo du manager.')
parser_edit.add_argument('-phone', required=False, help='Nouveau Numéro de tel du manager.')
parser_edit.add_argument('-email', required=False, help='Nouveau Email du manager.')
parser_edit.add_argument('-address', required=False, help='Nouveau Addresse du manager.')

# Analyse des arguments de ligne de commande
args = parser.parse_args()

if args.command == 'search':
  filter({
    'id': args.id,
    'name': args.name,
    'surname': args.surname,
    'nickname': args.nickname,
    'phone': args.phone,
    'email': args.email,
    'address': args.address
  })
elif args.command == 'add':
  addManager(
    args.name,
    args.surname,
    args.nickname,
    args.phone,
    args.email,
    args.address
  )
elif args.command == 'delete':
  deleteManager(args.id)
elif args.command == 'display':
  displayManager()
elif args.command == 'edit':
  editMnager(args.id, {
    'name': args.name,
    'surname': args.surname,
    'nickname': args.nickname,
    'phone': args.phone,
    'email': args.email,
    'address': args.address
  })
elif args.command == None:


  # Boucle principale du programme
  while True:
    print("\nQue souhaitez-vous faire ?")
    print("1. Ajouter un manager")
    print("2. Afficher tous les managers")
    print("3. Mettre à jour un manager")
    print("4. Supprimer un manager")
    print("5. Quitter le programme")

    choix = input("\nEntrez votre choix : ")

    if choix == '1':
      name = input("Entrez le prénom du manager : ")
      surname = input("Entrez le nom du manager : ")
      nickname = input("Entrez le pseudo de famille du manager (optionnel) : ")
      nickname = nickname if nickname != '' else None
      email = input("Entrez l'adresse email du manager : ")
      phone = input("Entrez le numéro de téléphone du manager : ")
      address = input("Entrez l'adresse du manager : ")
      addManager(name, surname, nickname, phone, email, address)
    elif choix == '2':
      displayManager()
    elif choix == '3':
      id = input("Entrez l'id du manager : ")
      if filter({'id': id}) != False :
        print("laissez vide pour ne pas modifier")
        name = input("Nouveau prénom du manager : ")
        name = name if name != '' else None
        surname = input("Nouveau nom de famille du manager : ")
        surname = surname if surname != '' else None
        nickname = input("Nouveau nom du manager : ")
        nickname = nickname if nickname != '' else None
        email = input("Nouvelle email du manager : ")
        email = email if email != '' else None
        phone = input("Nouveau numéro de téléphone du manager : ")
        phone = phone if phone != '' else None
        address = input("Nouvelle addresse du manager : ")
        address = address if address != '' else None
        editMnager(id, {
          'name': name,
          'surname': surname,
          'nickname': nickname,
          'phone': phone,
          'email': email,
          'address': address
        })
    elif choix == '4':
      id = input("Entrez l'id du manager : ")
      if filter({'id': id}) != False :
        if input("voulez vous confirmer ? (oui / non) ") == 'oui':
          deleteManager(id)
    elif choix == "5":
        # Quitter le programme
        print("Merci d'avoir utilisé le gestionnaire de managers. À bientôt !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
# avec le prompt





# filter({'phone': 'test', 'surname': 'boop'})
# addManager('test', 'test', None, 'test', 'test', 'test')
# displayManager()
