How to run the test program:
python ls8.py examples/sctest.ls8



* implementing CMP and equal flag

Flag register (FL) - holds current flag status
 - can be changed based on the operands given to the CMP opcode

00000LGE
L - less-than (during cmp if set to 1 -  reg A is less than reg B)
G - greater-than (during cmp if set to 1 - reg A is greater than reg B)
E - equal (during cmp if set to 1 - reg A and reg B are equal)

    ### probably have to use FL like pc and ir, as local variables ###???

CMP is handled by the ALU!
- It compares the values in two registers

# pseudo code
    # if they are equal, set the E flag to 1, otherwise 0 (00000001)
    # if regA is less that regB, set the L flag to 1, otherwise 0 (00000100)
    # if regA is greater than regB, set the G flag to 1, otherwise 0 (00000010)

* implementing JMP

JMP instruction - jumps to the address stored in the given register

# pseudo code
    # set the pc to the address stored at the given register

* implementing JEQ and JNE