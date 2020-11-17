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
  subtitle = ""
  subsubtitle = "generation details: {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}" 
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
      user_settings.draw_reverse_applicature['enabled']) # {10}

f.write(header)

appendix = '''
\drums {
  \\repeat unfold 2 {
    sn16^"L" sn^"R" sn^"L" sn^"L" sn^"R" sn^"L" sn^"R" sn^"R"
    \stemUp
    sn16_"L" sn_"R" sn_"L" sn_"L" sn_"R" sn_"L" sn_"R" sn_"R"
  }
}
'''
f.write(appendix)

print('COMPLETED: python_to_ly.py')