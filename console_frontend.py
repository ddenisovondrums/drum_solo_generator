from backend import *
from user_settings import *

comment = f'''
Пьеса "{user_seed}"
{bars_in_etude} тактов
Возможные размеры {beats_in_bar} четверти
Возможные длительности {possible_notes_in_beat}
Примерно {proportion_of_pauses}% пауз
Пьеса начинается с {starting_hand} руки
Максимум ударов одной рукой подряд {maximum_number_of_notes_played_with_one_hand_in_a_row} без учета мелизмов
Примерно {proportion_of_accents}% акцентов
Примерно {proportion_of_flams}% форшлагов
Максимум форшлагов подряд {maximum_flams_in_a_row}
Примерно {proportion_of_doubles}% двоек
Аппликатура "отзеркалена" {draw_reverse_applicature['enabled']}'''

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
            if not draw_reverse_applicature['enabled']:
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
                    print(draw_reverse_applicature[note['applicature']],end='')
                else:
                    print(str.lower(draw_reverse_applicature[note['applicature']]),end='')

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

        # Двойки
        print('{',end='')
        for note in beat:
            if note['its_pause']:
                print('_',end='')
            else:
                if note['its_double'] and note['its_accent']:
                    print('D',end='')
                elif not note['its_double'] and note['its_accent']:
                    print('S',end='')
                elif note['its_double'] and not note['its_accent']:
                    print('d',end='')
                else:
                    print('s',end='')
        print('}',end='')

print()