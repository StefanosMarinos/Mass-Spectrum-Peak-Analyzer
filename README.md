MS CODE USE INSTRUCTIONS
--------------------
•	To use the code you need a python compiler.  Various Python compilers are available in the internet such as this one (I use this one) : https://www.programiz.com/python-programming/online-compiler/
•	Copy and paste the entire code from the txt file that I give you with the name “ms code” to the compiler. Make sure the first line of code is the number 1 line, so you have to delete the initial lines that say : 
--------------------
1 # Online Python compiler (interpreter) to run Python online.
2# Write Python 3 code in this online editor and run it.
3 print("Try programiz.pro")
•	Press run to run the code in the compiler
•	6 choices show up. To make a choice type its number next to Choice and press enter 
•	1st choice (find C H O ) this one gives you the possible numbers of carbon, hydrogen and oxygen that can make up the given m/z. After choosing option 1 give the m/z and press enter. It will tell you the possible combinations that give that peak or it will tell you no possible combinations. (* more about this later)
•	2nd choice (find number of C atoms) this calculates the number of carbon atoms from the M and M+1 peaks intensities. You type in the intensities of each peak and press enter each time. Then it tells you the result
•	3rd choice , 4th choice and 5th choice do the same with more atoms. 

If you want to have another combination of atoms you can ask me to adjust the code to make another combination
---------------
**** IF THE AWNSER IN OPTIONS 1 3 4 AND 5 IS : NO COMBINATIONS FOUND
If the code cant find any combinations it is due to the set range for each atom. For example the section of the code for option 1 is currently set to search for a range of 10-16 atoms of carbon , 1-21 for hydrogen atoms and 0 to 4 for oxygen atoms. RANGE : range of 0-N includes 0 atoms to N-1 atoms, a range of 3-12 calculates options for 3 to 11 atoms. To keep searching for the same atoms but with another range of atoms you need to manually change the range inside the code. I will give you an example here :
Choice: 1
Give m/z: 341
No combinations found.

So you go to the section of the code for answer 1 ( it is this one that says elif answer =1

elif answer == 1:
        varos = float(input("Give m/z: "))
        r = 0

        for c in range(10, 16):
            for h in range(1, 21):
                for O in range(1, 4):
                    if varos == 12 * c + h + 16 * O:
                        print(f"c = {c}, h = {h}, O = {O}")
                        r += 1

this is before the change. You just need to adjust the numbers inside the range parentheses :
elif answer == 1:
        varos = float(input("Give m/z: "))
        r = 0

        for c in range(10, 22):
            for h in range(1, 21):
                for O in range(1, 6):
                    if varos == 12 * c + h + 16 * O:
                        print(f"c = {c}, h = {h}, O = {O}")
                        r += 1

this is the code now . It now calculates that m/z=341 is C21H9O5.
Choice: 1
Give m/z: 341
c = 21, h = 9, O = 5
Another example is when in option 3 I want to search only for bromine atoms and not chlorine atoms. Then I set the range for CL to (0,1) in elif answer=3 section. I also set the range for bromine to be (2,5) here :
Choice: 3
Give m/z: 328
c = 10, h = 2, O = 3, Br = 2, cl = 0
c = 10, h = 18, O = 2, Br = 2, cl = 0
c = 11, h = 6, O = 2, Br = 2, cl = 0
c = 12, h = 10, O = 1, Br = 2, cl = 0
so its clearly C11H6O2Br2.

One last thing to point out is that all bromine atoms are counted as 79 and all chlorine atoms are counted as 35 so you if we see 3 peaks that correspond to a dibromo product at 328 330 and 332 you need to use the number 328. For a tetrabromo product peak that shows up as m/z 490 you need to use the number 486
Choice: 3
Give m/z: 486
c = 10, h = 2, O = 3, Br = 4, cl = 0
c = 10, h = 18, O = 2, Br = 4, cl = 0
c = 11, h = 6, O = 2, Br = 4, cl = 0
this is what I used to calculate the tetrabromo product peak (range for carbon was set to 9-12)
