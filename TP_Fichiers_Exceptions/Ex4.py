import json
import os


def sauvegarder(clients, chemin):
    f = open(chemin, "w", encoding="utf-8")
    json.dump(clients, f, ensure_ascii=False, indent=4)
    f.close()


def charger(chemin):
    if not os.path.exists(chemin):
        return {}
    f = open(chemin, "r", encoding="utf-8")
    clients = json.load(f)
    f.close()
    return clients


clients = charger("clients.json")
if clients == {}:
    clients = {"C001": {"nom": "Sidi", "ville": "Nouakchott"},
               "C002": {"nom": "Aicha", "ville": "Atar"}}
clients["C003"] = {"nom": "Mariem", "ville": "Nouadhibou"}
sauvegarder(clients, "clients.json")

verif = charger("clients.json")
print(verif)
print(verif == clients)