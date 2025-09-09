
import math


def recept(antal):
    eggs = math.floor(3/4*antal)
    socker = 3/4*antal
    vaniljsocker=2/4*antal
    bakpulver=2/4*antal
    vetemjol=3/4*antal
    butter=75/4*antal
    vatten=1/4*antal

    print("Recept:")
    print("- Ägg: " + str(eggs) + " st")
    print("- Socker: " + str(socker) + " dl")
    print("- Vaniljsocker: " + str(vaniljsocker) + " tsk")
    print("- Bakpulver: " + str(bakpulver) + " tsk")
    print("- Vetemjöl: " + str(vetemjol) + " dl")
    print("- Smör: " + str(butter) + " g")
    print("- Vatten: " + str(vatten) + " dl")


def tidblanda(antal):
    tid=10+antal
    return tid
def tidgradda(antal):
    tid=30+3*antal
    return tid
def sockerkaka(antal):
    recept(antal)
    print("tid: " + str(tidgradda(antal)+tidblanda(antal)) + " minuter")


sockerkaka(4)
sockerkaka(7)
