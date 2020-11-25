import random
import backend
import user_settings

f= open("piece.ly","w")

version = '\\version "2.20.0" \n'
f.write(f"{version}")


f= open("piece.ly","a")



header = """
\\header{{
  title = "{0}"
  composer = "www.drumsologenerator.com"
  subsubtitle = \markup {12} \\fontsize #-6 "generation_details: {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {14}" {13}
  
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
      user_settings.note_info_for_tile, # {11}
      '{', # {12}
      '}', # {13}
      user_settings.show_applicature_in_score) # {14}

f.write(header)

######################## SCORE start ##########################
# score = r'''
# \score {
#   \new RhythmicStaff {
#     \set fontSize = -5'''

score = r'''
 \relative c'{
    \set fontSize = -3
    \clef percussion 
    \stemUp
    '''

###############################################################

score += f'\\tempo 4 = {user_settings.tempo}'


beat_draw_schemes = {
  'eight': { 
    'oo': ['d8','d8'],
    'o_': ['d4'],
    '_o': ['r8','d8'],
    '__': ['r4'],
  },
  'triplet': {
    'o__': ['d4'],
    '_o_': ['r8','d8','r8'],
    '__o': ['r4','d8'],
    'oo_': ['d8','d8','r8'],
    '_oo': ['r8','d8','d8'],
    'o_o': ['d4','d8'],
    'ooo': ['d8','d8','d8'],
    '___': ['r4'],
  },
  'sixteen': {
    'o___': ['d4'],
    '_o__': ['r16','d8.'],
    '__o_': ['r8','d8'],
    '___o': ['r8.','d16'],
    'oo__': ['d16','d16','r8'],
    '_oo_': ['r16','d16', 'd16', 'r16'],
    '__oo': ['r8', 'd16', 'd16'],
    'o__o': ['d8.','d16'],
    'o_o_': ['d8','d8'],
    '_o_o': ['r16','d8','d16'],
    'ooo_': ['d16','d16','d8'],
    '_ooo': ['r16','d16', 'd16', 'd16'],
    'o_oo': ['d8','d16','d16'],
    'oo_o': ['d16','d8','d16'],
    'oooo': ['d16','d16','d16','d16'],
    '____': ['r4'],
  },
  'quitniplets':{
    '_____': ['r4'],
    '____o': ['r8',    'r8','d16'],
    '___o_': ['r8',    'r16', 'd16','r16'],
    '___oo': ['r8',    'r16', 'd16','d16'],
    '__o__': ['r8',    'd8.'],
    '__o_o': ['r8',    'd16', 'r16','d16'],
    '__oo_': ['r8',    'd16', 'd16','r16'],
    '__ooo': ['r8',    'd16', 'd16','d16'],

    '_o___': ['r16', 'd16',    'r8.'],
    '_o__o': ['r16', 'd16',    'r8','d16'],
    '_o_o_': ['r16', 'd16',    'r16', 'd16','r16'],
    '_o_oo': ['r16', 'd16',    'r16', 'd16','d16'],
    '_oo__': ['r16', 'd16',    'd8.'],
    '_oo_o': ['r16', 'd16',    'd16', 'r16','d16'],
    '_ooo_': ['r16', 'd16',    'd16', 'd16','r16'],
    '_oooo': ['r16', 'd16',    'd16', 'd16','d16'],

    'o____': ['d4'],
    'o___o': ['d8',   'r8','d16'],
    'o__o_': ['d8',   'r16', 'd16','r16'],
    'o__oo': ['d8',   'r16', 'd16','d16'],
    'o_o__': ['d8',   'd8.'],
    'o_o_o': ['d8',   'd16', 'r16','d16'],
    'o_oo_': ['d8',   'd16', 'd16','r16'],
    'o_ooo': ['d8',   'd16', 'd16','d16'],

    'oo___': ['d16', 'd16', 'r8.'],
    'oo__o': ['d16', 'd16', 'r8','d16'],
    'oo_o_': ['d16', 'd16', 'r16', 'd16','r16'],
    'oo_oo': ['d16', 'd16', 'r16', 'd16','d16'],
    'ooo__': ['d16', 'd16', 'd8.'],
    'ooo_o': ['d16', 'd16', 'd16', 'r16','d16'],
    'oooo_': ['d16', 'd16', 'd16', 'd16','r16'],
    'ooooo': ['d16', 'd16', 'd16', 'd16','d16'],
  },
  'sixteen_triplets':{
    '______': ['r4'],
    '_____o': ['r8.', 'r16', 'r16','d16'],
    '____o_': ['r8.', 'r16', 'd16', 'r16'],
    '____oo': ['r8.', 'r16', 'd16', 'd16'],
    '___o__': ['r8.', 'd16', 'r16', 'r16'],
    '___o_o': ['r8.', 'd8', 'd16'],
    '___oo_': ['r8.', 'd16', 'd16', 'r16'],
    '___ooo': ['r8.', 'd16', 'd16', 'd16'],

    '__o___': ['r16', 'r16','d16', 'r8.'],
    '__o__o': ['r16', 'r16','d16', 'r16', 'r16','d16'],
    '__o_o_': ['r16', 'r16','d16', 'r16', 'd16','r16',],
    '__o_oo': ['r16', 'r16','d16', 'r16', 'd16','d16',],
    '__oo__': ['r16', 'r16','d16', 'd16', 'r16','r16'],
    '__oo_o': ['r16', 'r16','d16', 'd16', 'r16','d16'],
    '__ooo_': ['r16', 'r16','d16', 'd16', 'd16','r16'],
    '__oooo': ['r16', 'r16','d16', 'd16', 'd16','d16'],

    '_o____': ['r16', 'd16','r16', 'r8.'],
    '_o___o': ['r16', 'd16','r16', 'r16', 'r16','d16'],
    '_o__o_': ['r16', 'd16','r16', 'r16', 'd16','r16'],
    '_o__oo': ['r16', 'd16','r16', 'r16', 'd16','d16'],
    '_o_o__': ['r16', 'd16','r16', 'd16', 'r16','r16'],
    '_o_o_o': ['r16', 'd16','r16', 'd16', 'r16','d16'],
    '_o_oo_': ['r16', 'd16','r16', 'd16', 'd16','r16'],
    '_o_ooo': ['r16', 'd16','r16', 'd16', 'd16','d16'],

    '_oo___': ['r16', 'd16','d16', 'r8.'],
    '_oo__o': ['r16', 'd16','d16', 'r16', 'r16','d16'],
    '_oo_o_': ['r16', 'd16','d16', 'r16', 'd16','r16'],
    '_oo_oo': ['r16', 'd16','d16', 'r16', 'd16','d16'],
    '_ooo__': ['r16', 'd16','d16', 'd16', 'r16','r16'],
    '_ooo_o': ['r16', 'd16','d16', 'd16', 'r16','d16'],
    '_oooo_': ['r16', 'd16','d16', 'd16', 'd16','r16'],
    '_ooooo': ['r16', 'd16','d16', 'd16', 'd16','d16'],

    'o_____': ['d4'],
    'o____o': ['d16', 'r16','r16', 'r16', 'r16','d16'],
    'o___o_': ['d16', 'r16','r16', 'r16', 'd16','r16'],
    'o___oo': ['d16', 'r16','r16', 'r16', 'd16','d16'],
    'o__o__': ['d16', 'r16','r16', 'd16', 'r16','r16'],
    'o__o_o': ['d16', 'r16','r16', 'd16', 'r16','d16'],
    'o__oo_': ['d16', 'r16','r16', 'd16', 'd16','r16'],
    'o__ooo': ['d16', 'r16','r16', 'd16', 'd16','d16'],

    'o_o___': ['d16', 'r16','d16', 'r8.'],
    'o_o__o': ['d16', 'r16','d16', 'r16', 'r16','d16'],
    'o_o_o_': ['d16', 'r16','d16', 'r16', 'd16','r16'],
    'o_o_oo': ['d16', 'r16','d16', 'r16', 'd16','d16'],
    'o_oo__': ['d16', 'r16','d16', 'd16', 'r16','r16'],
    'o_oo_o': ['d16', 'r16','d16', 'd16', 'r16','d16'],
    'o_ooo_': ['d16', 'r16','d16', 'd16', 'd16','r16'],
    'o_oooo': ['d16', 'r16','d16', 'd16', 'd16','d16'],

    'oo____': ['d16', 'd16','r16', 'r8.'],
    'oo___o': ['d16', 'd16','r16', 'r16', 'r16','d16'],
    'oo__o_': ['d16', 'd16','r16', 'r16', 'd16','r16'],
    'oo__oo': ['d16', 'd16','r16', 'r16', 'd16','d16'],
    'oo_o__': ['d16', 'd16','r16', 'd16', 'r16','r16'],
    'oo_o_o': ['d16', 'd16','r16', 'd16', 'r16','d16'],
    'oo_oo_': ['d16', 'd16','r16', 'd16', 'd16','r16'],
    'oo_ooo': ['d16', 'd16','r16', 'd16', 'd16','d16'],

    'ooo___': ['d16', 'd16','d16', 'r8.'],
    'ooo__o': ['d16', 'd16','d16', 'r16', 'r16','d16'],
    'ooo_o_': ['d16', 'd16','d16', 'r16', 'd16','r16'],
    'ooo_oo': ['d16', 'd16','d16', 'r16', 'd16','d16'],
    'oooo__': ['d16', 'd16','d16', 'd16', 'r16','r16'],
    'oooo_o': ['d16', 'd16','d16', 'd16', 'r16','d16'],
    'ooooo_': ['d16', 'd16','d16', 'd16', 'd16','r16'],
    'oooooo': ['d16', 'd16','d16', 'd16', 'd16','d16'],
  },
  'septoles':{ 
    '_______': ['r4'], 
    '______o': ['r8', 'r8', 'r8','d16'],       
    '_____o_': ['r8', 'r8', 'r16', 'd16','r16'], 
    '_____oo': ['r8', 'r8', 'r16', 'd16','d16'], 
    '____o__': ['r8', 'r8', 'd8.'],       
    '____o_o': ['r8', 'r8', 'd16', 'r16','d16'], 
    '____oo_': ['r8', 'r8', 'd16', 'd16','r16'],
    '____ooo': ['r8', 'r8', 'd16', 'd16','d16'],

    '___o___': ['r8', 'r16', 'd16', 'r8.'],
    '___o__o': ['r8', 'r16', 'd16', 'r8','d16'],
    '___o_o_': ['r8', 'r16', 'd16', 'r16', 'd16','r16'],
    '___o_oo': ['r8', 'r16', 'd16', 'r16', 'd16','d16'],
    '___oo__': ['r8', 'r16', 'd16', 'd8.'],
    '___oo_o': ['r8', 'r16', 'd16', 'd16', 'r16','d16'],
    '___ooo_': ['r8', 'r16', 'd16', 'd16', 'd16','r16'],
    '___oooo': ['r8', 'r16', 'd16', 'd16', 'd16','d16'],

    '__o____': ['r8', 'd8',  'r8.'],
    '__o___o': ['r8', 'd8',  'r8','d16'],
    '__o__o_': ['r8', 'd8',  'r16', 'd16','r16'],
    '__o__oo': ['r8', 'd8',  'r16', 'd16','d16'],
    '__o_o__': ['r8', 'd8',  'd8.'],
    '__o_o_o': ['r8', 'd8',  'd16', 'r16','d16'],
    '__o_oo_': ['r8', 'd8',  'd16', 'd16','r16'],
    '__o_ooo': ['r8', 'd8',  'd16', 'd16','d16'],
    
    '__oo___': ['r8', 'd16', 'd16',  'r8.'],
    '__oo__o': ['r8', 'd16', 'd16',  'r8','d16'],
    '__oo_o_': ['r8', 'd16', 'd16',  'r16', 'd16','r16'],
    '__oo_oo': ['r8', 'd16', 'd16',  'r16', 'd16','d16'],
    '__ooo__': ['r8', 'd16', 'd16',  'd8.'],
    '__ooo_o': ['r8', 'd16', 'd16',  'd16', 'r16','d16'],
    '__oooo_': ['r8', 'd16', 'd16',  'd16', 'd16','r16'],
    '__ooooo': ['r8', 'd16', 'd16',  'd16', 'd16','d16'],
    
    '_o_____': ['r16', 'd16', 'r8', 'r8.'],
    '_o____o': ['r16', 'd16', 'r8', 'r8','d16'],
    '_o___o_': ['r16', 'd16', 'r8', 'r16', 'd16','r16'],
    '_o___oo': ['r16', 'd16', 'r8', 'r16', 'd16','d16'],
    '_o__o__': ['r16', 'd16', 'r8', 'd8.'],
    '_o__o_o': ['r16', 'd16', 'r8', 'd16', 'r16','d16'],
    '_o__oo_': ['r16', 'd16', 'r8', 'd16', 'd16','r16'],
    '_o__ooo': ['r16', 'd16', 'r8', 'd16', 'd16','d16'],
    
    '_o_o___': ['r16', 'd16', 'r16', 'd16',   'r8.'],
    '_o_o__o': ['r16', 'd16', 'r16', 'd16',   'r8','d16'],
    '_o_o_o_': ['r16', 'd16', 'r16', 'd16',   'r16', 'd16','r16'],
    '_o_o_oo': ['r16', 'd16', 'r16', 'd16',   'r16', 'd16','d16'],
    '_o_oo__': ['r16', 'd16', 'r16', 'd16',   'd8.'],
    '_o_oo_o': ['r16', 'd16', 'r16', 'd16',   'd16', 'r16','d16'],
    '_o_ooo_': ['r16', 'd16', 'r16', 'd16',   'd16', 'd16','r16'],
    '_o_oooo': ['r16', 'd16', 'r16', 'd16',   'd16', 'd16','d16'],
    
    '_oo____': ['r16', 'd16', 'd8', 'r8.'],
    '_oo___o': ['r16', 'd16', 'd8', 'r8','d16'],
    '_oo__o_': ['r16', 'd16', 'd8', 'r16', 'd16','r16'],
    '_oo__oo': ['r16', 'd16', 'd8', 'r16', 'd16','d16'],
    '_oo_o__': ['r16', 'd16', 'd8', 'd8.'],
    '_oo_o_o': ['r16', 'd16', 'd8', 'd16', 'r16','d16'],
    '_oo_oo_': ['r16', 'd16', 'd8', 'd16', 'd16','r16'],
    '_oo_ooo': ['r16', 'd16', 'd8', 'd16', 'd16','d16'],

    '_ooo___': ['r16', 'd16', 'd16', 'd16', 'r8.'],
    '_ooo__o': ['r16', 'd16', 'd16', 'd16', 'r8','d16'],
    '_ooo_o_': ['r16', 'd16', 'd16', 'd16', 'r16', 'd16','r16'],
    '_ooo_oo': ['r16', 'd16', 'd16', 'd16', 'r16', 'd16','d16'],
    '_oooo__': ['r16', 'd16', 'd16', 'd16', 'd8.'],
    '_oooo_o': ['r16', 'd16', 'd16', 'd16', 'd16', 'r16','d16'],
    '_ooooo_': ['r16', 'd16', 'd16', 'd16', 'd16', 'd16','r16'],
    '_oooooo': ['r16', 'd16', 'd16', 'd16', 'd16', 'd16','d16'],

    'o______': ['d4'],
    'o_____o': ['d8', 'r8',   'r8','d16'],
    'o____o_': ['d8', 'r8',   'r16', 'd16','r16'],
    'o____oo': ['d8', 'r8',   'r16', 'd16','d16'],
    'o___o__': ['d8', 'r8',   'd8.'],
    'o___o_o': ['d8', 'r8',   'd16', 'r16','d16'],
    'o___oo_': ['d8', 'r8',   'd16', 'd16','r16'],
    'o___ooo': ['d8', 'r8',   'd16', 'd16','d16'],

    'o__o___': ['d8', 'r16', 'd16',  'r8.'],
    'o__o__o': ['d8', 'r16', 'd16',  'r8','d16'],
    'o__o_o_': ['d8', 'r16', 'd16',  'r16', 'd16','r16'],
    'o__o_oo': ['d8', 'r16', 'd16',  'r16', 'd16','d16'],
    'o__oo__': ['d8', 'r16', 'd16',  'd8.'],
    'o__oo_o': ['d8', 'r16', 'd16',  'd16', 'r16','d16'],
    'o__ooo_': ['d8', 'r16', 'd16',  'd16', 'd16','r16'],
    'o__oooo': ['d8', 'r16', 'd16',  'd16', 'd16','d16'],

    'o_o____': ['d8', 'd8',   'r8.'],
    'o_o___o': ['d8', 'd8',   'r8','d16'],
    'o_o__o_': ['d8', 'd8',   'r16', 'd16','r16'],
    'o_o__oo': ['d8', 'd8',   'r16', 'd16','d16'],
    'o_o_o__': ['d8', 'd8',   'd8.'],
    'o_o_o_o': ['d8', 'd8',   'd16', 'r16','d16'],
    'o_o_oo_': ['d8', 'd8',   'd16', 'd16','r16'],
    'o_o_ooo': ['d8', 'd8',   'd16', 'd16','d16'],

    'o_oo___': ['d8', 'd16', 'd16',  'r8.'],
    'o_oo__o': ['d8', 'd16', 'd16',  'r8','d16'],
    'o_oo_o_': ['d8', 'd16', 'd16',  'r16', 'd16','r16'],
    'o_oo_oo': ['d8', 'd16', 'd16',  'r16', 'd16','d16'],
    'o_ooo__': ['d8', 'd16', 'd16',  'd8.'],
    'o_ooo_o': ['d8', 'd16', 'd16',  'd16', 'r16','d16'],
    'o_oooo_': ['d8', 'd16', 'd16',  'd16', 'd16','r16'], 
    'o_ooooo': ['d8', 'd16', 'd16',  'd16', 'd16','d16'],

    'oo_____': ['d16', 'd16', 'r8',   'r8.'],
    'oo____o': ['d16', 'd16', 'r8',   'r8','d16'],
    'oo___o_': ['d16', 'd16', 'r8',   'r16', 'd16','r16'],
    'oo___oo': ['d16', 'd16', 'r8',   'r16', 'd16','d16'],
    'oo__o__': ['d16', 'd16', 'r8',   'd8.'],
    'oo__o_o': ['d16', 'd16', 'r8',   'd16', 'r16','d16'],
    'oo__oo_': ['d16', 'd16', 'r8',   'd16', 'd16','r16'],
    'oo__ooo': ['d16', 'd16', 'r8',   'd16', 'd16','d16'],

    'oo_o___': ['d16', 'd16', 'r16', 'd16',   'r8.'],
    'oo_o__o': ['d16', 'd16', 'r16', 'd16',   'r8','d16'],
    'oo_o_o_': ['d16', 'd16', 'r16', 'd16',   'r16', 'd16','r16'],
    'oo_o_oo': ['d16', 'd16', 'r16', 'd16',   'r16', 'd16','d16'],
    'oo_oo__': ['d16', 'd16', 'r16', 'd16',   'd8.'],
    'oo_oo_o': ['d16', 'd16', 'r16', 'd16',   'd16', 'r16','d16'],
    'oo_ooo_': ['d16', 'd16', 'r16', 'd16',   'd16', 'd16','r16'],
    'oo_oooo': ['d16', 'd16', 'r16', 'd16',   'd16', 'd16','d16'],

    'ooo____': ['d16', 'd16', 'd8',   'r8.'],
    'ooo___o': ['d16', 'd16', 'd8',   'r8','d16'],
    'ooo__o_': ['d16', 'd16', 'd8',   'r16', 'd16','r16'],
    'ooo__oo': ['d16', 'd16', 'd8',   'r16', 'd16','d16'],
    'ooo_o__': ['d16', 'd16', 'd8',   'd8.'],
    'ooo_o_o': ['d16', 'd16', 'd8',   'd16', 'r16','d16'],
    'ooo_oo_': ['d16', 'd16', 'd8',   'd16', 'd16','r16'],
    'ooo_ooo': ['d16', 'd16', 'd8',   'd16', 'd16','d16'],

    'oooo___': ['d16', 'd16', 'd16', 'd16',     'r8.'],
    'oooo__o': ['d16', 'd16', 'd16', 'd16',     'r8','d16'],
    'oooo_o_': ['d16', 'd16', 'd16', 'd16',     'r16', 'd16','r16'],
    'oooo_oo': ['d16', 'd16', 'd16', 'd16',     'r16', 'd16','d16'],
    'ooooo__': ['d16', 'd16', 'd16', 'd16',     'd8.'],
    'ooooo_o': ['d16', 'd16', 'd16', 'd16',     'd16', 'r16','d16'],
    'oooooo_': ['d16', 'd16', 'd16', 'd16',     'd16', 'd16','r16'],
    'ooooooo': ['d16', 'd16', 'd16', 'd16',     'd16', 'd16','d16'],
  },
  'two_sixteenths_with_triplet': {
    '_____':  ['r4'],
    '____o':  ['r16', 'r16', 'r16', 'r16', 'd16'],
    '___o_':  ['r16', 'r16', 'r16', 'd16', 'r16'],
    '___oo':  ['r16', 'r16', 'r16', 'd16', 'd16'],
    '__o__':  ['r16', 'r16', 'd16', 'r16', 'r16'],
    '__o_o':  ['r16', 'r16', 'd16', 'r16', 'd16'],
    '__oo_':  ['r16', 'r16', 'd16', 'd16', 'r16'],
    '__ooo':  ['r16', 'r16', 'd16', 'd16', 'd16'],
    '_o___':  ['r16', 'd16', 'r16', 'r16', 'r16'],
    '_o__o':  ['r16', 'd16', 'r16', 'r16', 'd16'],
    '_o_o_':  ['r16', 'd16', 'r16', 'd16', 'r16'],
    '_o_oo':  ['r16', 'd16', 'r16', 'd16', 'd16'],
    '_oo__':  ['r16', 'd16', 'd16', 'r16', 'r16'],
    '_oo_o':  ['r16', 'd16', 'd16', 'r16', 'd16'],
    '_ooo_':  ['r16', 'd16', 'd16', 'd16', 'r16'],
    '_oooo':  ['r16', 'd16', 'd16', 'd16', 'd16'],
    'o____':  ['d4'],
    'o___o':  ['d16', 'r16', 'r16', 'r16', 'd16'],
    'o__o_':  ['d16', 'r16', 'r16', 'd16', 'r16'],
    'o__oo':  ['d16', 'r16', 'r16', 'd16', 'd16'],
    'o_o__':  ['d16', 'r16', 'd16', 'r16', 'r16'],
    'o_o_o':  ['d16', 'r16', 'd16', 'r16', 'd16'],
    'o_oo_':  ['d16', 'r16', 'd16', 'd16', 'r16'],
    'o_ooo':  ['d16', 'r16', 'd16', 'd16', 'd16'],
    'oo___':  ['d16', 'd16', 'r16', 'r16', 'r16'],
    'oo__o':  ['d16', 'd16', 'r16', 'r16', 'd16'],
    'oo_o_':  ['d16', 'd16', 'r16', 'd16', 'r16'],
    'oo_oo':  ['d16', 'd16', 'r16', 'd16', 'd16'],
    'ooo__':  ['d16', 'd16', 'd16', 'r16', 'r16'],
    'ooo_o':  ['d16', 'd16', 'd16', 'r16', 'd16'],
    'oooo_':  ['d16', 'd16', 'd16', 'd16', 'r16'],
    'ooooo':  ['d16', 'd16', 'd16', 'd16', 'd16'],
  },
  'triplet_with_two_sixteens': {
    '_____':  ['r4'],
    '____o':  ['r16', 'r16', 'r16', 'r16', 'd16'],
    '___o_':  ['r16', 'r16', 'r16', 'd16', 'r16'],
    '___oo':  ['r16', 'r16', 'r16', 'd16', 'd16'],
    '__o__':  ['r16', 'r16', 'd16', 'r16', 'r16'],
    '__o_o':  ['r16', 'r16', 'd16', 'r16', 'd16'],
    '__oo_':  ['r16', 'r16', 'd16', 'd16', 'r16'],
    '__ooo':  ['r16', 'r16', 'd16', 'd16', 'd16'],
    '_o___':  ['r16', 'd16', 'r16', 'r16', 'r16'],
    '_o__o':  ['r16', 'd16', 'r16', 'r16', 'd16'],
    '_o_o_':  ['r16', 'd16', 'r16', 'd16', 'r16'],
    '_o_oo':  ['r16', 'd16', 'r16', 'd16', 'd16'],
    '_oo__':  ['r16', 'd16', 'd16', 'r16', 'r16'],
    '_oo_o':  ['r16', 'd16', 'd16', 'r16', 'd16'],
    '_ooo_':  ['r16', 'd16', 'd16', 'd16', 'r16'],
    '_oooo':  ['r16', 'd16', 'd16', 'd16', 'd16'],
    'o____':  ['d4'],
    'o___o':  ['d16', 'r16', 'r16', 'r16', 'd16'],
    'o__o_':  ['d16', 'r16', 'r16', 'd16', 'r16'],
    'o__oo':  ['d16', 'r16', 'r16', 'd16', 'd16'],
    'o_o__':  ['d16', 'r16', 'd16', 'r16', 'r16'],
    'o_o_o':  ['d16', 'r16', 'd16', 'r16', 'd16'],
    'o_oo_':  ['d16', 'r16', 'd16', 'd16', 'r16'],
    'o_ooo':  ['d16', 'r16', 'd16', 'd16', 'd16'],
    'oo___':  ['d16', 'd16', 'r16', 'r16', 'r16'],
    'oo__o':  ['d16', 'd16', 'r16', 'r16', 'd16'],
    'oo_o_':  ['d16', 'd16', 'r16', 'd16', 'r16'],
    'oo_oo':  ['d16', 'd16', 'r16', 'd16', 'd16'],
    'ooo__':  ['d16', 'd16', 'd16', 'r16', 'r16'],
    'ooo_o':  ['d16', 'd16', 'd16', 'r16', 'd16'],
    'oooo_':  ['d16', 'd16', 'd16', 'd16', 'r16'],
    'ooooo':  ['d16', 'd16', 'd16', 'd16', 'd16'],
  }
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
        notes_in_beat = random.choice(['quitniplets', random.choice(['two_sixteenths_with_triplet','triplet_with_two_sixteens'])])
      elif quitniplets_are_enabled: notes_in_beat = 'quitniplets'
      else: notes_in_beat = random.choice(['two_sixteenths_with_triplet','triplet_with_two_sixteens'])
    # выяснили что за длительности в доле

    # print(notes_in_beat)

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
    # print(beat_draw_schemes[notes_in_beat][notes_in_beat_draw_scheme])
    # print(melismas_of_note)

    beat_score = ''
    
    # открываем нечетные группировки
    if notes_in_beat == 'triplet' and notes_in_beat_draw_scheme != 'o__' and notes_in_beat_draw_scheme != '___': beat_score += '\\tuplet 3/2 {'
    if notes_in_beat == 'quitniplets' and notes_in_beat_draw_scheme != 'o____' and notes_in_beat_draw_scheme != '_____': beat_score += '\\tuplet 5/4 {'
    if notes_in_beat == 'sixteen_triplets' and notes_in_beat_draw_scheme != 'o_____' and notes_in_beat_draw_scheme != '______': beat_score += '\\tuplet 6/4 {'
    if notes_in_beat == 'septoles' and notes_in_beat_draw_scheme != 'o______' and notes_in_beat_draw_scheme != '_______': beat_score += '\\tuplet 7/4 {'
    if notes_in_beat == 'triplet_with_two_sixteens' and notes_in_beat_draw_scheme != 'o____' and notes_in_beat_draw_scheme != '_____': beat_score += '\\tuplet 3/2 {'
    
    # соединяем ноты с их мелизмами и аппликатурой
    note_and_melismas_counter = 0
    two_plus_three_groups_counter = 0

    for note in beat_draw_schemes[notes_in_beat][notes_in_beat_draw_scheme]:
      
      # паузы просто переписываем
      if note.startswith('r'):
        beat_score += f'{note} '
        
      # погнали присоединять мелизмы
      else:
        # форшлаг
        if 'flam' in melismas_of_note[note_and_melismas_counter]: beat_score += '\\grace c16 '
        
        # нота
        beat_score += f'{note}'
        
        # двойка
        if 'double'in melismas_of_note[note_and_melismas_counter]: 
          if notes_in_beat == 'eight':  beat_score += f':16~'
          if notes_in_beat == 'triplet':  beat_score += f':16~'
          if notes_in_beat == 'sixteen':  beat_score += f':32~'
          if notes_in_beat == 'quitniplets':  beat_score += f':32~'
          if notes_in_beat == 'sixteen_triplets':  beat_score += f':32~'
          if notes_in_beat == 'septoles':  beat_score += f':32~'
          if notes_in_beat == 'triplet_with_two_sixteens': beat_score += f':32~'
          if notes_in_beat == 'two_sixteenths_with_triplet': beat_score += f':32~'
          


        # аппликатура
        if user_settings.show_applicature_in_score:
          if 'R' in melismas_of_note[note_and_melismas_counter] and user_settings.draw_reverse_applicature['enabled']: beat_score +='_"L"'
          elif 'L' in melismas_of_note[note_and_melismas_counter] and user_settings.draw_reverse_applicature['enabled']: beat_score +='_"Rr"'
          elif 'R' in melismas_of_note[note_and_melismas_counter]: beat_score +='_"R"'
          else: beat_score +='_"L"'

        # акцент
        if 'accent'in melismas_of_note[note_and_melismas_counter]: beat_score += '^>'
        
        
        beat_score += ' '
        note_and_melismas_counter += 1

      if notes_in_beat == 'triplet_with_two_sixteens' and two_plus_three_groups_counter == 2:
        beat_score +='} '
      elif notes_in_beat == 'two_sixteenths_with_triplet' and two_plus_three_groups_counter == 1:
        beat_score +='\\tuplet 3/2 {'
      two_plus_three_groups_counter += 1
      

    # закрываем нечетные группировки
    if notes_in_beat == 'triplet' and notes_in_beat_draw_scheme != 'o__' and notes_in_beat_draw_scheme != '___': beat_score += '} '
    if notes_in_beat == 'quitniplets' and notes_in_beat_draw_scheme != 'o____' and notes_in_beat_draw_scheme != '_____': beat_score += '}'
    if notes_in_beat == 'sixteen_triplets' and notes_in_beat_draw_scheme != 'o_____' and notes_in_beat_draw_scheme != '______': beat_score += '}'
    if notes_in_beat == 'septoles' and notes_in_beat_draw_scheme != 'o______' and notes_in_beat_draw_scheme != '_______': beat_score += '}'
    if notes_in_beat == 'two_sixteenths_with_triplet' and notes_in_beat_draw_scheme != 'o____' and notes_in_beat_draw_scheme != '_____': beat_score += '} '

    # print(beat_score)
    score += beat_score





######################## SCORE end ###########################
score += r'''\bar "|."
}'''
##############################################################

f.write(score)
print('COMPLETED: python_to_ly.py')