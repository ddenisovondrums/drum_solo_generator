from backend import *

reverse = {
    'enabled': False,
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
Максимум ударов одной рукой подряд {maximum_number_of_notes_played_with_one_hand_in_a_row}
Пьеса начинается с {starting_hand} руки
Аппликатура "отзеркалена" {reverse['enabled']}'''

print(comment)

for bar in piece:
    # каждый такт выводим на новой строке
    print()

    for beat in bar:
        print('\'', end='')
        
        # вывод нот в формате "о_О"
        for note in beat:
            if note['its_pause']:
                print('_',end='')
            elif note['its_accent']:
                print('O',end='')
            else:
                print('o',end='')
        print('(',end='')

        # вывод аппликатуры в формате (RLrl)
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

print()