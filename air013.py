'''
Créez un programme qui vérifie si les exercices de votre épreuve de l’air sont présents dans le répertoire et qu’ils fonctionnent (sauf celui là). Créez au moins un test pour chaque exercice.


Exemples d’utilisation :
$> python exo.py
air00 (1/3) : success
air00 (2/3) : success
air00 (3/3) : success
air01 (1/2) : success
air01 (2/2) : failure
air02 (1/1) : success
... 
Total success: (56/62)


Bonus : trouvez le moyen d’utiliser du vert et du rouge pour rendre réussites et échecs plus visibles.



faire trois tests le premier si il existe le deuxieme est une erreur et le troisiem et une reussite 
le retour du r c'est pour le resultat global 
'''

# Import:

import subprocess as s
class bcolors:
    OK = '\033[92m' #GREEN
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR



# Teste pour voir si le fichier exist:
def toBe(x):
    r=0
    try:
        with open(x): pass
        print(bcolors.OK + f"air0{x[4]}{x[5]} (1/3) : success"+ bcolors.RESET)
        return r+1
    except IOError:
        print(bcolors.FAIL + f"air0{x[4]}{x[5]} (1/3) : fail"+ bcolors.RESET)
        return r

def test(a):
    return a


#Test d'erreur:
def erreurs(name,test1):
    r=0
    try:
        x=s.check_output(f"python3 {name} {test1}",shell=True)
        if x==b'erreur\n':
            r+=1
            print(bcolors.OK + f"air0{name[4]}{name[5]} (2/3) : success"+ bcolors.RESET)
        else:
            print(bcolors.FAIL + f"air0{name[4]}{name[5]} (2/3) : fail"+ bcolors.RESET)
    except:
            print(bcolors.FAIL + f"air0{name[4]}{name[5]} (2/3) : fail"+ bcolors.RESET)
    return r

# test avec correct entrée:
def correct(name,test2):
    r=0
    try:
        x=s.check_output(f"python3 {name} {test2}",shell=True)
        if x!=b'erreur\n':
            r+=1
            print(bcolors.OK + f"air0{name[4]}{name[5]} (3/3) : success"+ bcolors.RESET)
        else:
            print(bcolors.FAIL + f"air0{name[4]}{name[5]} (3/3) : fail"+ bcolors.RESET)
    except:
        print(bcolors.FAIL + f"air0{name[4]}{name[5]} (3/3) : fail"+ bcolors.RESET)
    return r





# Air000:
def air000():
    r=0
    name="air000.py"
    # Test de presence:
    r+=toBe(name)
    # test d'erreur:
    test1=""
    r+=erreurs(name, test1)
    # test reel
    test2="Je fais un test"
    r+=correct(name,test2)
    return r
    

# Air001:
def air001():   
    r=0
    name="air001.py"
    # Test de presence:
    r+=toBe(name)
    # test d'erreur:
    test1=" 'je fais un test' "
    r+=erreurs(name,test1)
    # test reel:
    test2= "'Crevette magique dans la mer des étoiles' 'la'"
    r+=correct(name, test2)
    return r

# Air001:
def air002():
    r=0
    name="air002.py"
    # Test de presence:
    r+=toBe(name)
    # test d'erreur:
    test1="je"
    r+=erreurs(name,test1)
    # test reel:
    test2=" 'je' 'teste' 'des' 'trucs' '-' "
    r+=correct(name,test2)
    return r

# Air003:
def air003():
    r=0
    name="air003.py"
    # Test de presence:
    r+=toBe(name)
    # test d'erreur:
    test1="1"
    r+=erreurs(name,test1)
    # test reel:
    test2="1 2 3 4 5 4 3 2 1"
    r+=correct(name,test2)
    return r

# Air004:
def air004():
    r=0
    name="air004.py"
    # Test de presence:
    r+=toBe(name)
    # test d'erreur:
    test1="yo"
    r+=erreurs(name,test1)
    # test reel:
    test2=" Hello milady,   bien ou quoi ?? "
    r+=correct(name,test2)
    return r

# Air005:
def air005():
    r=0
    name="air005.py"
    # Test de presence:
    r+=toBe(name)
    # test d'erreur:
    test1="1"
    r+=erreurs(name,test1)
    # test reel:
    test2="10 11 12 20 -5"
    r+=correct(name,test2)
    return r

# Air006:
def air006():
    r=0
    name="air006.py"
    # Test de presence:
    r+=toBe(name)
    # test d'erreur:
    test1="1"
    r+=erreurs(name,test1)
    # test reel:
    test2="Michel Albert Thérèse Benoit t"
    r+=correct(name,test2)
    return r

# Air007:
def air007():
    r=0
    name="air007.py"
    # Test de presence:
    r+=toBe(name)
    # test d'erreur:
    test1="1"
    r+=erreurs(name,test1)
    # test reel:
    test2="10 20 30 40 50 60 70 90 33"
    r+=correct(name,test2)
    return r

# Air008:
def air008():
    r=0
    name="air008.py"
    # Test de presence:
    r+=toBe(name)
    # test d'erreur:
    test1="1"
    r+=erreurs(name,test1)
    # test reel:
    test2="10 20 30 fusion 15 25 35"
    r+=correct(name,test2)
    return r

# Air009:
def air009():
    r=0
    name="air009.py"
    # Test de presence:
    r+=toBe(name)
    # test d'erreur:
    test1="1"
    r+=erreurs(name,test1)
    # test reel:
    test2=" Michel Albert Thérèse Benoit"
    r+=correct(name,test2)
    return r

# Air010:
def air010():
    r=0
    name="air010.py"
    # Test de presence:
    r+=toBe(name)
    # test d'erreur:
    test1="1 2"
    r+=erreurs(name,test1)
    # test reel:
    test2="a.txt"
    r+=correct(name,test2)
    return r

# Air011:
def air011():
    r=0
    name="air011.py"
    # Test de presence:
    r+=toBe(name)
    # test d'erreur:
    test1="1"
    r+=erreurs(name,test1)
    # test reel:
    test2="0 5"
    r+=correct(name,test2)
    return r

# Air012:
def air012():
    r=0
    name="air012.py"
    # Test de presence:
    r+=toBe(name)
    # test d'erreur:
    test1="1"
    r+=erreurs(name,test1)
    # test reel:
    test2="6 5 4 3 2 1"
    r+=correct(name,test2)
    return r


# Fonction global:
def total():
    r=0
    r+=air000()
    r+=air001()
    r+=air002()
    r+=air003()
    r+=air004()
    r+=air005()
    r+=air006()
    r+=air007()
    r+=air008()
    r+=air009()
    r+=air010()
    r+=air011()
    r+=air012()
    print("...")
    if r > (39/2):
        print(bcolors.OK + f"Total success: ({r}/39)"+ bcolors.RESET)
    else:
        print(bcolors.FAIL + f"Total success: ({r}/39)"+ bcolors.RESET)


#Appel des fonctions: 
total()

