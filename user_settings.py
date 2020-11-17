# SETTINGS
user_seed = "Brother's wedding"
bars_in_etude = 1 # number of measures in a piece
beats_in_bar = [3,4] # possible time signatures
proportion_of_pauses = 0
proportion_of_accents = 50
proportion_of_flams = 0
maximum_flams_in_a_row = 0
proportion_of_doubles = 0
maximum_number_of_notes_played_with_one_hand_in_a_row = 1
starting_hand = ['R'] # ['R', 'L'] ['R'], ['L']

enabled_notes = {
    'eight': [False, 2],
    'triplets': [False, 3],
    'sixteen': [True, 4],
    'quitniplets': [False, 5],
    'sixteen_triplets': [False, 6],
    
    # will be enabled automatically
    'two_sixteenths_with_triplet': [False, 5],
}

# automatic enabling 'two_sixteenths_with_triplet'
if enabled_notes['sixteen'][0] and enabled_notes['sixteen_triplets'][0]:
    enabled_notes['two_sixteenths_with_triplet'][0] = True


draw_reverse_applicature = {
    'enabled': False,
    'R': 'L',
    'L': 'R'
}

print('COMPLETED: user_settings.py')