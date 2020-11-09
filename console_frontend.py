from backend import *

comment = f'''
Пьеса "{user_seed}"
{bars_in_etude} тактов
Возможные размеры {beats_in_bar}
Возможные длительности {notes_in_beat}
Примерно {proportion_of_pauses}% пауз
Примерно {proportion_of_accents}% акцентов
Максимум ударов одной рукой подряд {maximum_number_of_notes_played_with_one_hand_in_a_row}
Пьеса начинается с {starting_hand} руки'''

print(comment)

for bar in piece:
    print()
    for beat in bar:
        print('\'', end='')
        for note in beat:
            if note['its_pause']:
                print('_',end='')
            elif note['its_accent']:
                print('O',end='')
            else:
                print('o',end='')

        print('(',end='')
        for note in beat:
            if note['its_pause']:
                print('_',end='')
            elif note['its_accent']:
                print(note['applicature'],end='')
            else:
                print(str.lower(note['applicature']),end='')
        print(')',end='')

print()