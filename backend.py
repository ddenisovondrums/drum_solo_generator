import random

random.seed('фывафывафыв')

bars_in_etude = 16
beats_in_bar = [4] # [3,4,5]
notes_in_beat = [4] # [3,4,5,6]

piece = [[[{} for note in range(random.choice(notes_in_beat))] for beat in range(random.choice(beats_in_bar))] for bar in range(bars_in_etude)]

for bar in piece:
    for beat in bar:
        for note in beat:

            # Значение по умолчанию
            note['its_pause'] = False
            note['its_accent'] = False

            # Расставляем паузы
            if random.randint(0, 99) < 0:
                note['its_pause'] = True
                # applicature.append['']

            # Расставляем акценты
            if random.randint(0, 99) < 100:
                note['its_accent'] = True
            

# АППЛИКАТУРА

# Стэйт предыдущей ноты для принятия решения об аппликатуре
previous_note = {
    'applicature': '_',
    'its_accent': '_',
    'overflow': 0,
}

for bar in piece:
    for beat in bar:
        for note in beat:
            # паузы нахуй
            if note['its_pause']:
                previous_note['applicature'] = '_'
                previous_note['its_accent'] = '_'
                previous_note['overflow'] = 0
                # print('это пауза')

            # до сюда дошли все ноты
            else:
                # нотам после пауз присваиваем случайную аппликатуру
                if previous_note['applicature'] == '_':
                    note['applicature'] = 'R' if random.randint(0, 1) == 1 else 'L'
                    previous_note['applicature'] = note['applicature']
                    previous_note['its_accent'] = note['its_accent']
                    previous_note['overflow'] = 1
                    # print('нота после паузы')
                # до сюда дошли ноты после нот
                else:
                    # последовательность нот с одинаковой акцентностью
                    if note['its_accent'] == previous_note['its_accent']:
                        # если одной рукой сыграно уже три ноты
                        if previous_note['overflow'] == 3:
                            note['applicature'] = 'R' if previous_note['applicature'] == 'L' else 'L'
                            previous_note['overflow'] = 1
                        # одной рукой сыграно менее 3х нот
                        else:
                            note['applicature'] = 'R' if random.randint(0, 1) == 1 else 'L'
                            if note['applicature'] == previous_note['applicature']:
                                previous_note['overflow'] += 1
                            else:
                                previous_note['applicature'] = note['applicature']
                                previous_note['its_accent'] = note['its_accent']
                    # разноакцентные ноты
                    else:
                        note['applicature'] = 'R' if previous_note['applicature'] == 'L' else 'L'
                        previous_note['applicature'] = note['applicature']
                        previous_note['its_accent'] = note['its_accent']                        
                        # print('разноакцентная с предыдущей')
                





# console frontend
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

                # oO_o
print()        
print()        
# print(piece)