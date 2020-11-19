\version "2.20.0" 

\header{
  title = "Roman Z"
  composer = "www.drumsologenerator.com"
  subsubtitle = \markup { \fontsize #-5 "generation_details: 8, [2, 3], 10, 10, 0, 1, 0, 1, ['R'], False, ['eight', 'sixteen']" }
  
}

 \relative g'{
    \set fontSize = -3
    \stemUp
    \time 2/4
      c16_"R" c16_"L" c16_"R" c16_"L" c16_"R" c16_"L" c8_"R" 
      c16_"L" c8_"R" c16_"R" c8_"L" c8_"R" 
    \time 3/4
      c16_"L" c16_"R" c16_"L"^> c16_"R" c16_"L" c16_"R" c16_"L" c16_"R" c16_"L" c16_"R" c16_"L" c16_"R" 
    \time 2/4
      r8 c8_"R" c8_"L" c8_"R" 
      c8_"L" c8_"R" c16_"L" c16_"R" c16_"L" c16_"R" 
    \time 3/4
      c16_"L" c16_"R" c16_"L" c16_"R" c8_"L" c8_"R"^> c8_"L" c16_"R" c16_"L" 
      c8_"R" c16_"L" c16_"R" r8 c8_"L" c8_"R" c8_"L"^> 
    \time 2/4
      c16_"R"^> c16_"L"^> c8_"R"^> c16_"L" c8_"R" c16_"R" \bar "|."
  }
}