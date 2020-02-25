"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
     # inside def __init__(self): of the CPU class
        # add ram property with empty list
        self.ram = [0] * 8
        # add reg property with a list of 8 zeros (reg = [0] * 8)
        self.reg = [0] * 8
        # add properties for internal registers
        # pc - program counter, address of the current executing instruction
        self.pc = 0

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    # add ram_read() method - takes in address to read from mar
    def ram_read(self, mar):
        # create a variable called value and assign it to the value located in the RAM at specific address passed in
        value = self.ram[mar]
        # return value from RAM
        return value

    # add ram_write() method - takes in value to write from mdr, and address to write too from mar
    def ram_write(self, mdr, mar):
        # writes the value to the ram at the specific address passed in
        self.ram[mar] = mdr

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
    # inside the run() method
        # add HLT variable with value of 1
        HLT = 1
        # add LDI variable with value of 2
        LDI = 2
        # add PRN variable with value of 3
        PRN = 3

        # read memory address stored in pc & store result in variable ir
        ir = self.ram_read(self.pc)
        # use ram_read() method and pass in pc+1 and store in variable operand_a
        operand_a = self.ram_read(self.pc+1)
        # use ram_read() method and pass in pc+2 and store in variable operand_b
        operand_b = self.ram_read(self.pc+2)
        
        # set halted to False
        halted = False

        # while not halted
        while not halted:
            # set instruction to the program at the current pc count
            instruction = self.ram_read(self.pc)

            # if instruction == HLT 
            if instruction == HLT:
                # to exit the loop by changing halted to True
                halted = True
                # increment pc by 1 bite
                self.pc += 1
            # else if instruction == LDI
            elif instruction == LDI:
                # store the 8 value in a given register
                self.reg[self.pc+1] = self.pc+2
                # increment pc by 3 bites
                self.pc += 3
            # else if instruction == PRN
            elif instruction == PRN:
                # print the value in a register
                reg_num = self.pc+1
                print(self.reg[reg_num])
                # increment pc by 2 bites
                self.pc += 2
            # otherwise
            else:
                # print error message
                print(f"No instructrion found at index {self.pc}")