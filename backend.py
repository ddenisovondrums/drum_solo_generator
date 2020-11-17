import random
import user_settings

# GENERATION OF "piece" OBJECT
random.seed(user_settings.user_seed)

# Possible notes in beat are user-defined
possible_notes_in_beat = []
for enabled_note in user_settings.enabled_notes:
    note_is_enabled = user_settings.enabled_notes[enabled_note][0]
    notes_per_beat = user_settings.enabled_notes[enabled_note][1]
    if user_settings.enabled_notes[enabled_note][0]:
        possible_notes_in_beat.append(notes_per_beat)

# the piece consists of bars
# bars are made up of beats
# beats are made up of notes
piece = [[[{} for note in range(random.choice(possible_notes_in_beat))] for beat in range(random.choice(user_settings.beats_in_bar))] for bar in range(user_settings.bars_in_etude)]

# pause setup
for bar in piece:
    for beat in bar:
        for note in beat:
            note['its_pause'] = True if random.randint(0,99) < user_settings.proportion_of_pauses else False

# accents setup
for bar in piece:
    for beat in bar:
        for note in beat:
            if note['its_pause'] == False:
                note['its_accent'] = True if random.randint(0,99) < user_settings.proportion_of_accents else False

# applicature setup
previous_note = {
    'applicature': '_',
    'its_accent': '_',
    'overflow': 0,
}

first_note_has_applicature = False

for bar in piece:
    for beat in bar:
        for note in beat:
            # pauses update state
            if note['its_pause']:
                previous_note['applicature'] = '_'
                previous_note['its_accent'] = '_'
                previous_note['overflow'] = 0

            # only notes have reached here
            else:

                # assigning a applicature to the first note
                if not first_note_has_applicature:
                    note['applicature'] = random.choice(user_settings.starting_hand)
                    first_note_has_applicature = True
                    previous_note['applicature'] = note['applicature']
                    previous_note['its_accent'] = note['its_accent']
                    previous_note['overflow'] = 1

                # notes after pauses - assign random applicature
                elif previous_note['applicature'] == '_':
                    note['applicature'] = 'R' if random.randint(0, 1) == 1 else 'L'
                    previous_note['applicature'] = note['applicature']
                    previous_note['its_accent'] = note['its_accent']
                    previous_note['overflow'] = 1

                # notes after note
                else:
                    # note after one-accent note
                    if note['its_accent'] == previous_note['its_accent']:

                        # hand played over {user_settings.maximum_number_of_notes_played_with_one_hand_in_a_row} notes
                        if previous_note['overflow'] == user_settings.maximum_number_of_notes_played_with_one_hand_in_a_row:
                            note['applicature'] = 'R' if previous_note['applicature'] == 'L' else 'L'
                            previous_note['overflow'] = 1
                            previous_note['applicature'] = note['applicature']
                        
                        # hand played less {user_settings.maximum_number_of_notes_played_with_one_hand_in_a_row} notes
                        else:

                            # assign random applicature
                            note['applicature'] = 'R' if random.randint(0, 1) == 1 else 'L'

                            # the note is played with the same hand as the previous one
                            if note['applicature'] == previous_note['applicature']:
                                previous_note['overflow'] += 1
                            
                            # a note is played with the opposite hand
                            else:
                                previous_note['applicature'] = note['applicature']
                                previous_note['overflow'] = 1
                    # different accent notes
                    else:
                        note['applicature'] = 'R' if previous_note['applicature'] == 'L' else 'L'
                        previous_note['applicature'] = note['applicature']
                        previous_note['its_accent'] = note['its_accent']
                        previous_note['overflow'] = 1

# flams setup

flam_counter = 0

for bar in piece:
    for beat in bar:
        for note in beat:
            # pauses reset the counter
            if note['its_pause']:
                flam_counter = 0
            
            # only notes have reached here
            else:

                # If flam notes were played in a row more than{user_settings.maximum_flams_in_a_row} then the note will NOT become a flam note
                if flam_counter == user_settings.maximum_flams_in_a_row:
                    note['its_flam'] = False
                    flam_counter = 0
                
                
                else:
                    # or we accidentally assign a flam note to the note
                    if random.randint(0,99) < user_settings.proportion_of_flams:
                        note['its_flam'] = True
                        flam_counter += 1
                    # or not
                    else:
                        note['its_flam'] = False
                        flam_counter = 0


# doubles setup

next_note = {
    'its_pause': True,
    'applicature': '_',
}    

for bar in piece[::-1]:
    for beat in bar[::-1]:
        for note in beat[::-1]:

            # pauses 
            if note['its_pause']:
                # reset counter
                next_note['its_pause'] = True
                next_note['applicature'] = '_'

            # flam notes or accents or note before a note / flam note / accent played with the same hand, or notes before rests
            elif note['its_flam'] or note['its_accent'] or next_note['applicature'] == note['applicature'] or next_note['applicature'] == '_':
                # cannot become doubles
                note['its_double'] = False
                # reset counter
                next_note['its_pause'] = False
                next_note['applicature'] = note['applicature']

            # all other notes
            else:
                # can become doubles
                note['its_double'] = True if random.randrange(0, 99) < user_settings.proportion_of_doubles else False
                # reset counter
                next_note['its_pause'] = False
                next_note['applicature'] = note['applicature']

print('COMPLETED: backend.py')