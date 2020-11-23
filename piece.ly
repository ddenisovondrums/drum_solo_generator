\version "2.20.0" 

\header{
  title = "Hate five!"
  composer = "www.drumsologenerator.com"
  subsubtitle = \markup { \fontsize #-6 "generation_details: 16, [2], 3, 35, 0, 1, 0, 1, ['R'], False, ['quitniplets'], False" }
  
}

 \relative c'{
    \set fontSize = -3
    \clef percussion
    \stemUp
    \time 2/4
      \tuplet 5/4 {d16^> d16 d16 d16 d16 }\tuplet 5/4 {r16 d16 d16 d16 d16 }
      \tuplet 5/4 {d16 d16^> d16^> d16 d16 }\tuplet 5/4 {d16 d16^> d16^> d16^> d16 }
      \tuplet 5/4 {d16 d16^> d16 d16^> d16 }\tuplet 5/4 {d16^> d16 d16 d16^> d16^> }
      \tuplet 5/4 {d16 d16^> d16 d16 d16 }\tuplet 5/4 {d16 d16 d16 d16 d16 }
      \tuplet 5/4 {d16 d16 d16 d16 d16 }\tuplet 5/4 {d16 d16 d16^> d16^> d16 }
      \tuplet 5/4 {d16 d16^> d16 d16^> d16 }\tuplet 5/4 {d16^> d16 d16 d16 d16 }
      \tuplet 5/4 {d16 d16 d16^> d16 d16 }\tuplet 5/4 {d16^> d16 d16^> d16^> d16^> }
      \tuplet 5/4 {d16 d16^> d16 d16^> d16 }\tuplet 5/4 {d16^> d16^> d16^> d16 d16 }
      \tuplet 5/4 {r16 d16^> d16 d16 d16 }\tuplet 5/4 {d16 d16^> d16 d16^> d16 }
      \tuplet 5/4 {d16 d16 d16 d16 r16 }\tuplet 5/4 {d16 d16 d16^> d16^> d16^> }
      \tuplet 5/4 {d16 d16^> d16^> d16 d16^> }\tuplet 5/4 {d16 d16^> d16 d16^> d16 }
      \tuplet 5/4 {d16^> d16 d16 d16 d16 }\tuplet 5/4 {d16 d16 r16 d16 d16 }
      \tuplet 5/4 {d16^> d16^> d16 d16 r16 }\tuplet 5/4 {d16^> d16 d16 d16 d16 }
      \tuplet 5/4 {d16^> d16^> d16^> r16 d16^> }\tuplet 5/4 {d16^> d16 d16^> d16 d16 }
      \tuplet 5/4 {d16 d16^> d16 d16^> d16 }\tuplet 5/4 {d16^> d16^> d16 d16^> d16 }
      \tuplet 5/4 {d16 d16^> d16^> d16 d16 }\tuplet 5/4 {r16 d16^> d16 d16 d16^> }\bar "|."
}