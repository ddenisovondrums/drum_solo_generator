from math import floor
from subprocess import Popen

# SETTINGS
# generation_details: 16, [2], 3, 35, 0, 1, 0, 1, ['R'], False, ['quitniplets'], False
user_seed = "Ted Reed turn "
bars_in_etude = 4 # number of measures in a piece 4/8/16/32
beats_in_bar = [4] # possible time signatures 1/2/3/4/5/6/7/8/9
proportion_of_pauses = 45    # 0-100
proportion_of_accents = 0  # 0-100
proportion_of_flams = 0 # 0-100
maximum_flams_in_a_row = 1 # 1-4
proportion_of_doubles = 0 # 0-100
maximum_number_of_notes_played_with_one_hand_in_a_row = 1 # 1-4
starting_hand = ['R'] # ['R', 'L'] ['R'], ['L']

# al least one of them == True
enabled_notes = {
    'eight': [True, 2],
    'triplets': [False, 3],
    'sixteen': [False, 4],
    'quitniplets': [False, 5],
    'sixteen_triplets': [False, 6],
    'septoles': [False, 7],
    
    # will be enabled automatically
    'two_sixteenths_with_triplet': [False, 5],
}

# ноты для title
note_info_for_tile = []
for enabled_note in enabled_notes:
  if enabled_notes[enabled_note][0]:
    note_info_for_tile.append(enabled_note)

# automatic enabling 'two_sixteenths_with_triplet'
if enabled_notes['sixteen'][0] and enabled_notes['sixteen_triplets'][0]:
    enabled_notes['two_sixteenths_with_triplet'][0] = True

# APPLICATURE SETTINGS

draw_reverse_applicature = {
    'enabled': False,
    'R': 'L',
    'L': 'R'
}

show_applicature_in_score = False


# TEMPO SETTINGS
tempo = 0 # zero means auto, else 30-360

if tempo == 0:
    tempo = 500
    for enabled_note in enabled_notes:
        if enabled_notes[enabled_note][0]:
            tempo = floor(min(tempo, 480/enabled_notes[enabled_note][1] - 8))
    if proportion_of_flams == 0 and proportion_of_doubles == 0:
        tempo = floor(tempo * 1.5)


print('COMPLETED: user_settings.py')

import python_to_ly