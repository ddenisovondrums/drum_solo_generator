import random

# НАСТРОЙКИ
user_seed = "Brother's wedding"
bars_in_etude = 8 # Количество тактов
beats_in_bar = [1] # Возможные размеры
proportion_of_pauses = 20
proportion_of_accents = 100
proportion_of_flams = 0
maximum_flams_in_a_row = 0
proportion_of_doubles = 0
maximum_number_of_notes_played_with_one_hand_in_a_row = 1
starting_hand = ['R'] # ['R', 'L'] ['R'], ['L']

enabled_notes = {
    'eight': (True, 2),
    'triplets': (True, 3),
    'sixteen': (True, 4),
    'two_sixteenths_with_triplet': (True, 5),
    'sixteen_triplets': (True, 6),
    'quitniplets': (True, 5),
}

# ГЕНЕРАЦИЯ ФОРМЫ ПЬЕСЫ
random.seed(user_seed)

# Возможные длитлельности в доле
notes_in_beat = []

for enabled_note in enabled_notes:
    note_is_enabled = enabled_notes[enabled_note][0]
    notes_per_beat = enabled_notes[enabled_note][1]
    if enabled_notes[enabled_note][0]:
        notes_in_beat.append(notes_per_beat)

piece = [[[{} for note in range(random.choice(notes_in_beat))] for beat in range(random.choice(beats_in_bar))] for bar in range(bars_in_etude)]

# РАССТАНОВВКА ПАУЗ
for bar in piece:
    for beat in bar:
        for note in beat:
            note['its_pause'] = True if random.randint(0,99) < proportion_of_pauses else False

# РАССТАНОВКА АКЦЕНТОВ
for bar in piece:
    for beat in bar:
        for note in beat:
            if note['its_pause'] == False:
                note['its_accent'] = True if random.randint(0,99) < proportion_of_accents else False

# РАССТАНОВКА АППЛИКАТУРЫ
previous_note = {
    'applicature': '_',
    'its_accent': '_',
    'overflow': 0,
}

first_note_has_applicature = False

for bar in piece:
    for beat in bar:
        for note in beat:
            # паузы обновляют стэйт
            if note['its_pause']:
                previous_note['applicature'] = '_'
                previous_note['its_accent'] = '_'
                previous_note['overflow'] = 0

            # до сюда дошли только ноты
            else:

                # Присваеваем аппликатуру для первой ноты
                if not first_note_has_applicature:
                    note['applicature'] = random.choice(starting_hand)
                    first_note_has_applicature = True
                    previous_note['applicature'] = note['applicature']
                    previous_note['its_accent'] = note['its_accent']
                    previous_note['overflow'] = 1

                # ноты после пауз - присваиваем случайную аппликатуру
                elif previous_note['applicature'] == '_':
                    note['applicature'] = 'R' if random.randint(0, 1) == 1 else 'L'
                    previous_note['applicature'] = note['applicature']
                    previous_note['its_accent'] = note['its_accent']
                    previous_note['overflow'] = 1

                # ноты после ноты
                else:
                    # нота после одноакцентной ноты
                    if note['its_accent'] == previous_note['its_accent']:

                        # рукой сыграно более {maximum_number_of_notes_played_with_one_hand_in_a_row} нот -
                        if previous_note['overflow'] == maximum_number_of_notes_played_with_one_hand_in_a_row:
                            note['applicature'] = 'R' if previous_note['applicature'] == 'L' else 'L'
                            previous_note['overflow'] = 1
                            previous_note['applicature'] = note['applicature']
                        
                        # одной рукой сыграно менее {maximum_number_of_notes_played_with_one_hand_in_a_row} нот
                        else:

                            # присваеваем ей случайную апликатуру
                            note['applicature'] = 'R' if random.randint(0, 1) == 1 else 'L'

                            # нота играется той же рукой, что и предыдущая
                            if note['applicature'] == previous_note['applicature']:
                                previous_note['overflow'] += 1
                            
                            # нота играется противоположной рукой
                            else:
                                previous_note['applicature'] = note['applicature']
                                previous_note['overflow'] = 1
                    # разноакцентные ноты
                    else:
                        note['applicature'] = 'R' if previous_note['applicature'] == 'L' else 'L'
                        previous_note['applicature'] = note['applicature']
                        previous_note['its_accent'] = note['its_accent']
                        previous_note['overflow'] = 1

# РАССТАНОВКА ФОРШЛАГОВ

flam_counter = 0

for bar in piece:
    for beat in bar:
        for note in beat:
            # паузы обнуляют счетчик форшлагов
            if note['its_pause']:
                flam_counter = 0
            
            # до сюда дошли только ноты
            else:

                # Если форшлагов подряд сыграно более чем {maximum_flams_in_a_row} то нота НЕ станет форшлагом
                if flam_counter == maximum_flams_in_a_row:
                    note['its_flam'] = False
                    flam_counter = 0
                
                
                else:
                    # либо случайно присваиваем ноте форшлаг
                    if random.randint(0,99) < proportion_of_flams:
                        note['its_flam'] = True
                        flam_counter += 1
                    # либо нет
                    else:
                        note['its_flam'] = False
                        flam_counter = 0


# РАССТАНОВКА ДВОЕК

next_note = {
    'its_pause': True,
    'applicature': '_',
}    

for bar in piece[::-1]:
    for beat in bar[::-1]:
        for note in beat[::-1]:

            # паузы 
            if note['its_pause']:
                # обновляют стэйт
                next_note['its_pause'] = True
                next_note['applicature'] = '_'

            # форшлаги или акценты или нота перед нотой/форшлагом/акцентом играемыми той же рукой или ноты перед паузами
            elif note['its_flam'] or note['its_accent'] or next_note['applicature'] == note['applicature'] or next_note['applicature'] == '_':
                # не могут стать двойками
                note['its_double'] = False
                # обновляют стэйт
                next_note['its_pause'] = False
                next_note['applicature'] = note['applicature']

            # все остальные ноты
            else:
                # могут стать двойками
                note['its_double'] = True if random.randrange(0, 99) < proportion_of_doubles else False
                # обновляют стэйт 
                next_note['its_pause'] = False
                next_note['applicature'] = note['applicature']

print('generation complete')