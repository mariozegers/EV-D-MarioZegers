from retweeted import top10Retweeted
from emited import top10Emited
from topDays import top10Days
from hashtags import top10Hashtags

def main():
    option = int(input(
    "Eliga función (marcando número en la casilla): \nTop 10 tweets más retweeted [0] \nTop 10 usuarios en función a la cantidad de tweets que emitieron [1] \nTop 10 días donde hay más tweets [2] \nTop 10 hashtags más usados [3] \nIngrese opción:"))
    if option == 0:
        top10Retweeted()
    elif option == 1:
        top10Emited()
    elif option == 2:
        top10Days()
    elif option == 3:
        top10Hashtags()
    else:
        print("No existe esta opción")

main()