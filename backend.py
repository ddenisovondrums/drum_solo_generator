import random

# НАСТРОЙКИ
bars_in_etude = 8
beats_in_bar = [4] # [3,4,5]
notes_in_beat = [4] # [3,4,5,6]
user_seed = "Brother's wedding"
proportion_of_pauses = 20
proportion_of_accents = 20
proportion_of_flams = 30
maximum_flams_in_a_row = 2
maximum_number_of_notes_played_with_one_hand_in_a_row = 2
starting_hand = ['R','L'] # ['R'], ['L']

# ГЕНЕРАЦИЯ ФОРМЫ ПЬЕСЫ
random.seed(user_seed)
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

print('generation complete')