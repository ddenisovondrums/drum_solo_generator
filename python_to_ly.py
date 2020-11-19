import random
import backend
import user_settings

f= open("piece.ly","w")

version = '\\version "2.20.0" \n'
f.write(f"{version}")


f= open("piece.ly","a")

# ноты для title
possible_notes = []
for enabled_note in user_settings.enabled_notes:
  print(enabled_note)
  if user_settings.enabled_notes[enabled_note][0]:
    possible_notes.append(enabled_note)

header = """
\\header{{
  title = "{0}"
  composer = "www.drumsologenerator.com"
  subsubtitle = \markup {12} \\fontsize #-5 "generation_details: {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}" {13}
  
}}
""".format(
      user_settings.user_seed,  # {0}
      user_settings.bars_in_etude, # {1}
      user_settings.beats_in_bar, # {2}
      user_settings.proportion_of_pauses, # {3}
      user_settings.proportion_of_accents, # {4}
      user_settings.proportion_of_flams, # {5}
      user_settings.maximum_flams_in_a_row, # {6}
      user_settings.proportion_of_doubles, # {7} 
      user_settings.maximum_number_of_notes_played_with_one_hand_in_a_row, # {8} 
      user_settings.starting_hand, # {9}
      user_settings.draw_reverse_applicature['enabled'], # {10}
      possible_notes, # {11}
      '{', # {12}
      '}') # {13}

f.write(header)

######################## SCORE start ##########################
# score = r'''
# \score {
#   \new RhythmicStaff {
#     \set fontSize = -5'''

score = r'''
 \relative g'{
    \set fontSize = -3
    \stemUp'''

###############################################################



beat_draw_schemes = {
  'eight': { 
    'oo': ['c8','c8'],
    'o_': ['c4'],
    '_o': ['r8','c8'],
    '__': ['r4'],
  },
  'triplet': {
    'o__': ['c4'],
    '_o_': ['r8','c8','r8'],
    '__o': ['r4','c8'],
    'oo_': ['c8','c8','r8'],
    '_oo': ['r8','c8','c8'],
    'o_o': ['c4','c8'],
    'ooo': ['c8','c8','c8'],
    '___': ['r4'],
  },
  'sixteen': {
    'o___': ['c4'],
    '_o__': ['r16','c8.'],
    '__o_': ['r8','c8'],
    '___o': ['r8.','c16'],
    'oo__': ['c16','c16','r8'],
    '_oo_': ['r16','c16', 'c16', 'r16'],
    '__oo': ['r8', 'c16', 'c16'],
    'o__o': ['c8.','c16'],
    'o_o_': ['c8','c8'],
    '_o_o': ['r16','c8','c16'],
    'ooo_': ['c16','c16','c8'],
    '_ooo': ['r16','c16', 'c16', 'c16'],
    'o_oo': ['c8','c16','c16'],
    'oo_o': ['c16','c8','c16'],
    'oooo': ['c16','c16','c16','c16'],
    '____': ['r4'],
  },
}

# SCORE mid

# стэйт
state = {
  'time': 4, # размер предыдущего такта
}

# для каждого такта 
for bar in backend.piece:

  # если изменился размер
  if state['time'] != len(bar):
    
    # прописывает это в нотах
    score += f'''
    \\time {len(bar)}/4
      '''
    state['time'] = len(bar)
  
  # иначе 
  else:
    # просто переводим строку
    score += '''
      '''
  # для каждой доли
  for beat in bar:    
    
    # смотрим какие в ней длительности
    if len(beat) == 2:   notes_in_beat = 'eight'
    elif len(beat) == 3: notes_in_beat = 'triplet'
    elif len(beat) == 4: notes_in_beat = 'sixteen'
    elif len(beat) == 6: notes_in_beat = 'sixteen_triplets'
    elif len(beat) == 7: notes_in_beat = 'septoles'
    else: #len(beat) == 5: 
      quitniplets_are_enabled = user_settings.enabled_notes['quitniplets'][0]
      two_sixteenths_with_triplet_are_enabled = user_settings.enabled_notes['two_sixteenths_with_triplet'][0]
      if quitniplets_are_enabled and two_sixteenths_with_triplet_are_enabled:
        notes_in_beat = random.choice(['quitniplets','two_sixteenths_with_triplet'])
      elif quitniplets_are_enabled: notes_in_beat = 'quitniplets'
      else: notes_in_beat = 'two_sixteenths_with_triplet'
    # выяснили что за длительности в доле

    # решаем как будем рисовать долю (объединять мелкие паузы/ноты в более крупные длительности)
    notes_in_beat_draw_scheme = ''

    # и выясняем какие мелизмы/аппликатура у нот в доле
    melismas_of_note = []

    # перебираем ноты
    for note in beat:
      if note['its_pause']:
        # рисуем паузы
        notes_in_beat_draw_scheme += '_'
      else:
        # рисуем ноты
        notes_in_beat_draw_scheme += 'o'

        # переписываем мелизмы
        melismas_of_note.append([])
        current_note_melismas = melismas_of_note[-1]
        if note['its_flam']: current_note_melismas.append('flam')
        if note['its_accent']: current_note_melismas.append('accent')
        if note['its_double']: current_note_melismas.append('double')
        current_note_melismas.append(note['applicature'])
    
    # у нас есть схема отрисовки нот и мелизмы всех нот
    # print(beat_draw_schemes[notes_in_beat][notes_in_beat_draw_scheme],end=' ')
    # print(melismas_of_note)

    beat_score = ''
    
    # открываем нечетные группировки
    if notes_in_beat == 'triplet' and notes_in_beat_draw_scheme != 'o__' and notes_in_beat_draw_scheme != '___': beat_score += '\\tuplet 3/2 {'

    # соединяем ноты с их мелизмами и аппликатурой
    counter = 0
    for note in beat_draw_schemes[notes_in_beat][notes_in_beat_draw_scheme]:
      
      # паузы просто переписываем
      if note.startswith('r'):
        beat_score += f'{note} '
        
      # погнали присоединять мелизмы
      else:
        print(note, melismas_of_note[counter])
        # форшлаг
        if 'flam' in melismas_of_note[counter]: beat_score += '\\grace c16 '
        
        # нота
        beat_score += f'{note}'
        
        # двойка
        if 'double'in melismas_of_note[counter]: 
          if notes_in_beat == 'eight':  beat_score += f':16~'
          if notes_in_beat == 'sixteen':  beat_score += f':32~'
          if notes_in_beat == 'triplet':  beat_score += f':16~'
        
        # аппликатура
        if 'R' in melismas_of_note[counter] and user_settings.draw_reverse_applicature['enabled']: beat_score +='_"L"'
        elif 'L' in melismas_of_note[counter] and user_settings.draw_reverse_applicature['enabled']: beat_score +='_"Rr"'
        elif 'R' in melismas_of_note[counter]: beat_score +='_"R"'
        else: beat_score +='_"L"'

        # акцент
        if 'accent'in melismas_of_note[counter]: beat_score += '^>'
        
        
        beat_score += ' '
        counter += 1

    # закрываем нечетные группировки
    if notes_in_beat == 'triplet' and notes_in_beat_draw_scheme != 'o__' and notes_in_beat_draw_scheme != '___': beat_score += '} '

    print(beat_score)
    score += beat_score





######################## SCORE end ###########################
score += r'''\bar "|."
  }
}'''
##############################################################

f.write(score)
print('COMPLETED: python_to_ly.py')