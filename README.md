# Terminal Tetris

A simplified version of Tetris displayed in the terminal using ANSI escape codes.

https://github.com/user-attachments/assets/b51a019d-0116-43aa-bcea-67f38eb360cf

## Design

the program structure is the following (or at least that's what it tries to be)
<img width="2256" height="596" alt="diagram" src="https://github.com/user-attachments/assets/24bb85e2-4487-403d-ab8c-b0fcf81d15e7" />

Since I can't read from the terminal screen, I needed to add a pre-rendering stage: the board matrix.
Having a matrix also simplifies on-screen drawing, as I don't have to worry about the individual position of each Piece.
I only need to apply the logic to the matrix and then draw the entire board each frame.

Furthermore, the logical part of removing entire rows and checking for collisions is easier, at least for the methods I chose.
