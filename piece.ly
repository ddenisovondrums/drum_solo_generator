\version "2.20.0" 

\header{
  title = "Brother's wedding"
  composer = "www.drumsologenerator.com"
  subsubtitle = \markup { \fontsize #-5 "generation_details: 8, [3], 10, 10, 10, 1, 10, 1, ['R'], False, ['sixteen']" }
  
}

 \relative g'{
    \set fontSize = -3
    \stemUp
    \time 3/4
      c16_"R" c16_"L"^> c16_"R" c16_"L" c8_"R"^> c16_"L" c16_"R" c16_"L" c16_"R" c16_"L" c16_"R" 
      c16_"L" c16_"R"^> c16_"L" c16_"R" r16 c16_"R" \grace c16 c16_"L" c16_"R" c16_"L"^> c16_"R" c16_"L" \grace c16 c16_"R" 
      c16_"L" c8_"R" c16_"R" \grace c16 c16_"L" c16_"R" c16_"L" c16_"R" c16_"L" c8_"R" c16_"R" 
      r16 c16:32~_"R" c16_"L" c16_"R" c8_"L" \grace c16 c16_"R" c16_"L" c16_"R" c16_"L" c16_"R" c16_"L" 
      c16_"R" c16_"L" c16_"R" c16_"L" c16_"R" c16_"L" c16_"R"^> c16_"L" c16_"R" c16_"L" c8_"R" 
      c16_"L" c16_"R" c16_"L" c16_"R" c16_"L" c16_"R"^> c8_"L" c16_"L"^> c16_"R" c16_"L" c16_"R" 
      c8_"L" c16_"L" c16_"R"^> c16_"L"^> \grace c16 c16_"R" c8_"L" c16_"R" c8_"L" c16_"L" 
      c16_"R" c16_"L" c16_"R" c16_"L"^> c16_"R" c16_"L" c16_"R" c16_"L" r16 c16_"L" c16_"R" c16_"L" \bar "|."
  }
}