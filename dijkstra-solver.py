from string import ascii_lowercase, ascii_uppercase
import itertools
import random
import timeit
from alive_progress import alive_bar
import time
from os import system, name

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def iter_all_strings():
    for size in itertools.count(1):
        for s in itertools.product(ascii_uppercase, repeat=size):
            yield "".join(s)

def genererGraphe(nombrePoint = 5):
    graphe = {
        "point_debut": "A",
        "points": {}
    }

    for s in itertools.islice(iter_all_strings(), nombrePoint):
        graphe["points"][s] = {"points_voisins" : {}}

    graphe["point_fin"] = list(graphe["points"])[-1]

    with alive_bar(len(graphe["points"])) as bar :
        for point in graphe["points"]:
            pointCheminAleatoire = point

            nombreDeBranche = random.randint(1,3)

            for i in range(nombreDeBranche):
                while pointCheminAleatoire == point:
                    pointCheminAleatoire = list(graphe["points"])[random.randint(0,nombrePoint)-1]

                distanceAleatoire = random.randint(1,10)
                graphe["points"][point]["points_voisins"][pointCheminAleatoire] = distanceAleatoire
                graphe["points"][pointCheminAleatoire]["points_voisins"][point] = distanceAleatoire
            bar()

    return graphe


def computeShortestPath() :

    pointDebut = graphe['point_debut']
    pointFin = graphe['point_fin']
    pointActuel = pointDebut
    points = graphe['points']
    cheminsPossible = []
    pointParcourus = [pointDebut]
    meilleurChemin = [pointDebut]
    historiqueMeilleursPoints = []
    meilleurPoint = ''
    distanceTotale = 0

    while pointFin not in pointParcourus :


        for point in points[pointActuel]['points_voisins']:
            if point not in pointParcourus:
                cheminsPossible.append({'point':point, 'distance':points[pointActuel]['points_voisins'][point] + distanceTotale, "point_precedent" : pointActuel})

        if len(cheminsPossible) == 0:
            print(bcolors.FAIL + "Il n'y a pas de solution pour ce graphe (aucun chemin n'existe entre le point de début et de fin)" + bcolors.ENDC)
            return

        plusCourteDistance = float('inf')

        for point in cheminsPossible:
            distanceTotaleVoisin = point['distance']
            if distanceTotaleVoisin < plusCourteDistance:
                plusCourteDistance = distanceTotaleVoisin
                meilleurPoint = point['point']

        if pointActuel != pointFin:
            for point in cheminsPossible:
                if point['point'] == meilleurPoint:
                    historiqueMeilleursPoints.append(point)
                    cheminsPossible.pop(cheminsPossible.index(point))

            if plusCourteDistance - distanceTotale > 0:
                distanceTotale = plusCourteDistance

        pointParcourus.append(pointActuel)
        pointActuel = meilleurPoint

    historiqueMeilleursPoints.reverse()
    pointHisto = historiqueMeilleursPoints[0]

    meilleurChemin.append(pointHisto["point"])
    for p in historiqueMeilleursPoints :
        if pointHisto["point_precedent"] == p["point"] :
            meilleurChemin.insert(1, pointHisto["point_precedent"])
            pointHisto = p

    print(bcolors.OKGREEN + 'Meilleur chemin : '+str(meilleurChemin) + bcolors.ENDC)
    print(bcolors.OKGREEN + 'Nombre de point du graphe : '+str(nombrePoint) + bcolors.ENDC)
    print(bcolors.OKGREEN + 'Distance la plus courte : '+str(distanceTotale) + bcolors.ENDC)
    print(bcolors.OKGREEN + 'Nombre de point à parcourir : '+str(len(meilleurChemin)) + bcolors.ENDC)

system('cls')
nombrePoint = input("Entrez un nombre de points à générer dans le graphe:\n")
system('cls')

graphe = {'point_debut': 'A', 'points': {'A': {'points_voisins': {'B': 9, 'F': 7}}, 'B': {'points_voisins': {'A': 9, 'K': 7, 'C': 5, 'J': 7}}, 'C': {'points_voisins': {'B': 5, 'H': 6, 'I': 10}}, 'D': {'points_voisins': {'I': 5, 'L': 4}}, 'E': {'points_voisins': {'L': 9, 'G': 4, 'K': 8}}, 'F': {'points_voisins': {'A': 7}}, 'G': {'points_voisins': {'E': 4}}, 'H': {'points_voisins': {'C': 6}}, 'I': {'points_voisins': {'D': 5, 'C': 10}}, 'J': {'points_voisins': {'B': 7}}, 'K': {'points_voisins': {'B': 7, 'E': 8}}, 'L': {'points_voisins': {'E': 9, 'D': 4}}}, 'point_fin': 'L'}
graphe = genererGraphe(int(nombrePoint))
print(bcolors.OKGREEN + "Graphe Généré" + bcolors.ENDC)

afficherGraphe = input("Afficher le graphe ? o/n\n")
system('cls')
if afficherGraphe == "o" or afficherGraphe == "O":
    print(bcolors.OKCYAN + str(graphe) + bcolors.ENDC)
    print("\n----------------------\n")

duration = timeit.timeit(computeShortestPath, number=1)
print(bcolors.OKBLUE + 'Temps d\'exécution de l\'algorithme : '+str(round(duration*1000, 3))+' ms' + bcolors.ENDC)




# Graphe de test :

# graphe = {
#     "point_debut": "A",
#     "point_fin": "G",
#     "points": {
#         "A": {
#             "points_voisins" : {
#                 "B": 3,
#                 "E": 1,
#                 "F": 4
#             }
#         },
#         "B": {
#             "points_voisins" : {
#                 "A": 3,
#                 "C": 6,
#                 "D": 3,
#                 "E": 1,
#                 "F": 1
#             }
#         },
#         "C": {
#             "points_voisins" : {
#                 "B": 6,
#                 "D": 1,
#                 "E": 5,
#                 "G": 1
#             }
#         },
#         "D": {
#             "points_voisins" : {
#                 "B": 3,
#                 "C": 1,
#                 "F": 1,
#                 "G": 4
#             }
#         },
#         "E": {
#             "points_voisins" : {
#                 "A": 1,
#                 "B": 1,
#                 "C": 5
#             }
#         },
#         "F": {
#             "points_voisins" : {
#                 "A": 4,
#                 "B": 1,
#                 "D": 1
#             }
#         },
#         "G": {
#             "points_voisins" : {
#                 "C": 1,
#                 "D": 4
#             }
#         }
#     }
# }
