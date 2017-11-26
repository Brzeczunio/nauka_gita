import f
import main2
import os

if __name__ == "__main__":
    imie = 'Damian'
    nazwisko = 'Brzeczek'
    wiek = 26.3
    if f.sprawdz(wiek, 20):
        print('mlody czlowiek')
    else:
        print('emeryt')
    f.wypisz(imie, nazwisko)

    print(os.getenv('USERNAME'))
