\version "2.20.0" 

\header{
  title = "5 x 5 = 5"
  composer = "www.drumsologenerator.com"
  subsubtitle = \markup { \fontsize #-5 "generation_details: 5, [5], 15, 32, 0, 2, 0, 1, ['R'], False, ['quitniplets']" }
  
}

 \relative g'{
    \set fontSize = -3
    \stemUp
    \time 5/4
      \tuplet 5/4 {c16^> c16 r16 c16 c16 }\tuplet 5/4 {c8 c16 c16 c16 }\tuplet 5/4 {r16 c16 c16^> c16^> c16 }\tuplet 5/4 {r16 c16 c8 c16 }\tuplet 5/4 {c16^> c16 c16 c16^> c16 }
      \tuplet 5/4 {c16 c16 c16 c16 r16 }\tuplet 5/4 {r16 c16^> c8 c16^> }\tuplet 5/4 {c16^> c16 c16 c16 c16 }\tuplet 5/4 {c16 c16^> c16^> c16 c16 }\tuplet 5/4 {c16 c16 c16 c16 c16^> }
      \tuplet 5/4 {c16^> c16 c16^> c16 c16^> }\tuplet 5/4 {c16 c16 c16 c16 c16 }\tuplet 5/4 {c16 c16^> c8 c16 }\tuplet 5/4 {c8.^> c16^> c16^> }\tuplet 5/4 {c16 c16^> c16 c16^> c16 }
      \tuplet 5/4 {c16 c16 c8 c16 }\tuplet 5/4 {c16 c16 c16 c16 c16 }\tuplet 5/4 {c8 c16^> c16^> c16 }\tuplet 5/4 {c16 c16 c16 c16 r16 }\tuplet 5/4 {c16 c16^> c16^> c16 c16 }
      \tuplet 5/4 {c16 c16 r8 c16 }\tuplet 5/4 {c16 c16^> c16 c16 c16 }\tuplet 5/4 {r8 c16 c16 r16 }\tuplet 5/4 {c16 c16^> c16 c16 c16^> }\tuplet 5/4 {c16^> c16 c16^> c16 c16 }\bar "|."
  }
}