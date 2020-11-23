\version "2.20.0" 

\header{
  title = "Brother's wedding"
  composer = "www.drumsologenerator.com"
  subtitle = "generation details: 4, [2], 10, 10, 10, 1, 10, 1, ['R', 'L'], False" 
  subsubtitle = \markup { \fontsize #-10"generation details:... "}}

\score {
  \new RhythmicStaff {
    \tempo "Zalupante" 4 = 666
    % \time 2/4
    %   \grace c16 c2:32~_"R"^>
    %   c8. c16 \tuplet 5/4 { c8 c8 c16 }
    % \time 3/4
    %   \tuplet 3/2 {c4 r c} r16 c:32 \grace c 16 c c:32
    % \time 2/4
    %   c8 c
    %   \tuplet 3/2 {c8 c c} 
    %   \tuplet 5/4 {c16_"R"^> c_"L"^> c_"R"^> c_"L"^> c_"R"^>} 
    %   \tuplet 6/4 {c16 c c c c c}
    % \time 4/4
    %   c4 c c c
    \time 1/4
    %   c8 c8 
    %   \tuplet 3/2 {c8 c8 c8}
    %   c16 c16 c16 c16
    %   \tuplet 5/4 {c16 c16 c16 c16 c16}
    %   \tuplet 6/4 {c16 c16 c16 c16 c16 c16}
    %   \tuplet 7/4 {c16 c16 c16 c16 c16 c16 c16}
    % \time 1/4
    %   \grace c16 c2:32~_"R"^>
    %   \grace c16 c2:32~_"R"^> 
    % \time 1/4
    %   c8.
      \tuplet 5/4 {c16 c16 c16 c16 c16}
      \tuplet 3/2 {c16 c16 c16} c16 c16
      c16 c16 \tuplet 3/2 {c16 c16 c16}
      d4
    }
}

'r8.'],
'r8','d16'],
'r16', 'd16','r16'],
'r16', 'd16','d16'],
'd8.'],
'd16', 'r16','d16'],
'd16', 'd16','r16'],
'd16', 'd16','d16'],