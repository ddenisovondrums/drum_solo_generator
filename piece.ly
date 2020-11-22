\version "2.20.0" 

\header{
  title = "Find a bug"
  composer = "www.drumsologenerator.com"
  subsubtitle = \markup { \fontsize #-6 "generation_details: 32, [1], 30, 40, 0, 2, 100, 1, ['R'], False, ['sixteen_triplets'], False" }
  
}

 \relative c'{
    \set fontSize = -3
    \clef percussion
    \stemUp
    \time 1/4
      \tuplet 6/4 {d16 r16 r16 r16 r16 d16:32~ }
      \tuplet 6/4 {d16^> d16^> d16^> r16 r16 d16 }
      \tuplet 6/4 {r16 d16^> r16 r16 r16 d16:32~ }
      \tuplet 6/4 {d16:32~ d16:32~ d16^> r16 d16:32~ d16 }
      \tuplet 6/4 {r16 d16:32~ d16:32~ d16 r16 d16^> }
      \tuplet 6/4 {d16:32~ d16 r16 d16 r16 d16^> }
      \tuplet 6/4 {d16:32~ d16^> d16 r8. }
      \tuplet 6/4 {d16:32~ d16:32~ d16^> d16:32~ d16:32~ d16:32~ }
      \tuplet 6/4 {d16:32~ d16^> d16^> d16:32~ d16:32~ d16^> }
      \tuplet 6/4 {d16:32~ d16^> r16 r16 d16:32~ d16:32~ }
      \tuplet 6/4 {d16:32~ d16:32~ d16:32~ d16 r16 r16 }
      \tuplet 6/4 {d16^> r16 d16^> d16:32~ d16:32~ d16:32~ }
      \tuplet 6/4 {d16^> d16 r16 r16 d16^> d16 }
      \tuplet 6/4 {r16 d16 r16 d16:32~ d16^> r16 }
      \tuplet 6/4 {r16 d16^> d16:32~ d16:32~ d16^> d16^> }
      \tuplet 6/4 {d16:32~ d16 r16 d16^> d16^> r16 }
      \tuplet 6/4 {r16 r16 d16^> d16:32~ d16 r16 }
      \tuplet 6/4 {d16 r16 d16 r16 d16:32~ d16 }
      \tuplet 6/4 {r16 d16:32~ d16:32~ d16:32~ d16:32~ d16 }
      \tuplet 6/4 {r16 d16:32~ d16:32~ d16 r16 d16:32~ }
      \tuplet 6/4 {d16^> r16 d16:32~ d16^> d16:32~ d16:32~ }
      \tuplet 6/4 {d16^> d16:32~ d16:32~ d16^> d16:32~ d16:32~ }
      \tuplet 6/4 {d16 r16 r16 r16 d16 r16 }
      \tuplet 6/4 {r16 d16:32~ d16^> d16:32~ d16^> d16:32~ }
      \tuplet 6/4 {d16:32~ d16^> d16^> d16^> r16 d16^> }
      \tuplet 6/4 {d16^> r16 d16 r16 r16 d16:32~ }
      \tuplet 6/4 {d16 r16 d16^> r8. }
      \tuplet 6/4 {r16 d16^> d16^> r8. }
      \tuplet 6/4 {d16^> d16:32~ d16^> d16:32~ d16:32~ d16^> }
      \tuplet 6/4 {r16 d16 r16 d16^> d16 r16 }
      \tuplet 6/4 {r16 d16^> r16 r16 d16^> r16 }
      \tuplet 6/4 {d16^> d16 r16 r16 d16:32~ d16 }\bar "|."
}