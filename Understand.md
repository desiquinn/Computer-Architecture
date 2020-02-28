My Understand Notes:

Day 1 To Do *************

Day 1: Get print8.ls8 running
 Inventory what is here
 Implement the CPU constructor
 Add RAM functions ram_read() and ram_write()
 Implement the core of run()
 Implement the HLT instruction handler
 Add the LDI instruction
 Add the PRN instruction

 1st Comment should be "Get print8.ls8 running"

 Inventory of what is here:
 asm folder - don't need to touch this unless we are doing stretch.
 ls8 folder - Using this folder to emplement the MVP of this project
    * Readme - explaining how to implement the ls8 step by step
    * cpu.py - This is our source file according to the readme, run it via the ls8.py file
    * ls8.py - This is how we will run the CPU (python ls8.py), this initiates and instance of CPU, invokes load() CPU, and invokes run() CPU.
    * examples - a folder of ls8 files which will eventually be loaded dynamically into the CPU (right now what we need is hard coded)

 FAQ.md- A large list of answers to common questions.  This should have all/most of the information needed to implement the project

 Ls8 Cheetsheet - list of instruction codes and the number or registers or values they take and the size of them
 ls8 Spec - these are in the instructions for building out the ls8 and what is expected.
 Readme.md - outlines what is considered mvp and stretch and gives us a lists of tasks.

 * LS-8 Stands for Lambda School 8 computer
 8-bit computer
 8-bit memory addressing - ?
 8-bit CPU - only has 8 wires available for addresses, computations, and instructions
 8-bits = 256 bytes of memory - can only computer files up to 255 bytes

 execute code that stores the value of 8 in registers and prints it

 """
 # print8.ls8: Print the number 8 on the screen

10000010 # LDI R0,8 ---> Machine code value of the instruction for LDI
00000000 ---> Operand
00001000 ---> Operand with value of 8
01000111 # PRN R0  ---> Machine code value of the instruction for PRN
00000000 ---> Operand
00000001 # HLT  ---> Machine code value of the instruction for HLT
"""

we have to implement the following instructions:

* LDI - load "immediate", store this value in a register(which is what we need it to do), or "set this register to this value"
* PRN - psuedo-instruction that prints the numerica value stored in a register
* HLT - halt and exit

THE PROGRAM IS ALREADY HARD CODED INTO SOURCE FILE (cpu.py)

# Already Done For Us

    * sys already imported
    * progam is hard coded into the load function (no need to load anything today???)
    * saving instruction that comes from the program (hard coded right now) into a specific address of the RAM
    * incrementing the address by 1
    * ls8.py is completed in order to run the CPU
    * already done in load() - add an address properties that serves as a counter of the current place we are accessing in the ram

# What we need To Do - Most/ALL work done in cpu.py for MVP (must do steps 1-6 for day 1 mvp)
    
    * Complete configuring the __init__ for the CPU class
        - add a "ram" properties that is a list that holds 256 bytes of memory 
        - add a register properties with 8 spaces to represent registers R0-R7 
            reg = [0] * 8
        - add properties for internal registers
            * pc - program counter, address of the current executing instuction
            ### don't need to add these some may come later ###
            * fl - flags, holds the current flag's status
            * ir - instruction register, contains a copy of the currently executing instruction, can be local variable in run?
            * mar - Memory Address Register, holds the memory address we're reading or writing
            * mdr - Memory Data Register, holds the value to write or the value just read
    * add ram_read() and ram_write() methods - They access the RAM
        - read = accepts address to read (from mar) and returns the value stored in RAM
        - write = accepts value to write (mdr), and an address (mar) to write it too, and does it
    * add HLT, LDI, and PRN instruction definitions so we can refer to them by name
        - should this be a propety? or should it be a local variable in run?
    * Complete configuring the run function - which will run the CPU
        - read memory address stored in pc
        - store result in ir
        - use read to store pc +1 and pc+2 in variables operand_a and operand_b
        - I believe this is where we impliment the instructions for mvp (use if-elif cascade)
            - use HLT to exit the loop
            - use LDI to store the 8 value in a register
            - use PRN to print the value in a register
        - update pc after each operand (determine how mand bites are used)
    
    # don't need these for Day 1 MVP
    * Complete configuring the alu function
        - how?
    * Complete configuring the trace function (I think this is just for debugging)
        - how?


Day 2 To Do ************

Day 2: Add the ability to load files dynamically, get mult.ls8 running
 Un-hardcode the machine code
 Implement the load() function to load an .ls8 file given the filename passed in as an argument
 Implement a Multiply instruction (run mult8.ls8)

 Use the command line like "python3 ls8.py examples/mult.ls8" in order to run specific files from examples using our ls8

Use the following to see how you are running these files:

import sys

print(sys.argv)

You can also use this to run the specific file dynamically in your code:

sys.argv[0] == "ls8.py"
sys.argv[1] == "examples/mult.ls8"

Also use error handling to ensure you are only getting back what you expect

This will all be done in load() and using with open ()
We need to ignore blank lines 
slice out everything after #
convert the binary string to an interger using int(ob#, base 2)



