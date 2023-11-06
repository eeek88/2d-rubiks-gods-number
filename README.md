# 2d-rubiks-cube-gods-number

<b>Introduction</b>
The Rubik's cube is an extensively studied game -- lesser known, however, are its two dimensional counterparts. In this project, we investigate the combinatorics of, and compute the God's Number to a Rubik's like game in its 3x3 and 4x4 variants.

<b>How to play</b>
<!-- Picture and explanation of game -- mention metroid prime 2 but in the least attentive way possible, perhaps as a footnote -->
<!--Couldnt find a better picture for the time being-->
![puzzle example](https://static.wikia.nocookie.net/metroid/images/f/f0/Rubiks_Puzzle.png/revision/latest?cb=20150816034434)

We drew inspiration from a puzzle in the video game Metroid Prime 2: Echoes (2004) where the player encounters a 3x3 grid which contains tiles with 3 separate colors in randomized positons across the grid. The goal is to rearrange the the tiles so that each row contains only the specific color assigned to it. This is achieved by rotating any 2x2 segment of the 3x3 grid by 90 degrees enough times to match the solution. In the example above, the goal would be to arrange the red tiles on the 1st (top) row, green tiles on the 2nd row and blue tiles on the 3rd row. 



<b>Combinatorics</b>
In the 3x3 variant, there are three possible colors to pick from, and three of each color. Therefore, the number of possible positions in the 3x3 variant equals:
$$\binom{9}{3} \binom{6}{3} \binom{3}{3} = 1680$$
Which we confirm with Monte Carlo simulation.

The number of unique positions in the 4x4 variant follows similarly:
$$\binom{16}{4} \binom{12}{4} \binom{8}{4} \binom{4}{4} = 63063000$$

(The number of games in each variant follows the sequence A034841 in the OEIS.) We note that the number of unique positions in the 6x6 variant exceeds the number of unique positions in the traditional Rubik's cube, despite having the same number of colors.

<b>Methodology and results</b>
Using Dijkstra's algorithm on the state space graph of our game, we compute god's number in the 3x3 variant to be 9, and ? in the 4x4 variant. 


