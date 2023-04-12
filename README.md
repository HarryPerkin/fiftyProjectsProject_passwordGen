# Password Generator
## Escaping Tutorial Hell with Question Driven Development.

1. Password Generator takes an integer as a single argument and checks for validity.
2. The program loops over the size of the passed integer.
3. With each loop a random char is generated from unicode codes 32-126 and concatenated onto previous chars.
4. The subseqent string of random chars is written to *passwords.txt*.

## Known Bugs/Potential Issues:
. If passwords.txt does not exist in the directory, the program will not create one.
