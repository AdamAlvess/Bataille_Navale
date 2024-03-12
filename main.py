import bateau
from enumBateau import EnumBateau


def main():

    bateau1 = bateau.Bateau("Bateau1", 2, EnumBateau.Vertical, 0)

    print(bateau1.orientation)


main()
