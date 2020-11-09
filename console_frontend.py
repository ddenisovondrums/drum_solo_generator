from backend import *

reverse = {
    'enabled': True,
    'R': 'L',
    'L': 'R'
}

comment = f'''
Пьеса "{user_seed}"
{bars_in_etude} тактов
Возможные размеры {beats_in_bar}
Возможные длительности {notes_in_beat}
Примерно {proportion_of_pauses}% пауз
Примерно {proportion_of_accents}% акцентов
Примерно {proportion_of_flams}% форшлагов
Максимум ударов одной рукой подряд {maximum_number_of_notes_played_with_one_hand_in_a_row} без учета мелизмов
Максимум форшлагов подряд {maximum_flams_in_a_row}
Пьеса начинается с {starting_hand} руки
Аппликатура "отзеркалена" {reverse['enabled']}'''

print(comment)

for bar in piece:
    # каждый такт выводим на новой строке
    print()

    for beat in bar:
        print('\'', end='') 

        # вывод аппликатуры в формате (RLrl)
        print('(',end='')
        for note in beat:
            
            # вывод сгенерированной аппликатуры 
            if not reverse['enabled']:
                if note['its_pause']:
                    print('_',end='')
                elif note['its_accent']:
                    print(note['applicature'],end='')
                else:
                    print(str.lower(note['applicature']),end='')

            # вывод "зеркальной" аппликатуры
            else:
                if note['its_pause']:
                    print('_',end='')
                elif note['its_accent']:
                    print(reverse[note['applicature']],end='')
                else:
                    print(str.lower(reverse[note['applicature']]),end='')

        print(')',end='')

        # Форшлаги
        print('[',end='')
        for note in beat:
            if note['its_pause']:
                print('_',end='')
            else:
                if note['its_flam'] and note['its_accent']:
                    print('F',end='')
                elif not note['its_flam'] and note['its_accent']:
                    print('O',end='')
                elif note['its_flam'] and not note['its_accent']:
                    print('f',end='')
                else:
                    print('o',end='')


        print(']',end='')

print()