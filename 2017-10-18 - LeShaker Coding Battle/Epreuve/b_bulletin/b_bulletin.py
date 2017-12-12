from statistics import mean


TEXTE_JACK_VA_PRENDRE_CHER = "Jack ! Viens ici !"
TEXTE_JACK_EST_BIEN = "RAS"


def test_note_min(note_jack, note_min):
    return note_jack < note_min


def test_note_max(note_jack, note_max):
    return note_jack > note_max


def test_moyenne(note_jack, notes_camarades, moyenne):
    return abs(mean(notes_camarades + [note_jack]) - moyenne) > 0.02


def test_nombre_camarades(notes_camarades, nombre_camarades):
    return len(notes_camarades) != nombre_camarades


def main():
    note_jack = int(input())
    note_min, note_max = [int(s) for s in input().split()]
    moyenne = float(input())
    nombre_camarades = int(input())
    notes_camarades = [int(s) for s in input().split()]

    if test_note_min(note_jack, note_min) or\
       test_note_max(note_jack, note_max) or\
       test_moyenne(note_jack, notes_camarades, moyenne) or\
       test_nombre_camarades(notes_camarades, nombre_camarades):
        print(TEXTE_JACK_VA_PRENDRE_CHER)
    else:
        print(TEXTE_JACK_EST_BIEN)


if __name__ == '__main__':
    main()
