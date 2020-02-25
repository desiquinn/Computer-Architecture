# Day 1 MVP

    # inside def __init__(self): of the CPU class
        # add ram property with empty list
        # add reg property with a list of 8 zeros (reg = [0] * 8)
        # add properties for internal registers
        # pc - program counter, address of the current executing instruction

    # inside the CPU class itself

        # add ram_read() method - takes in address to read from mar
            # create a variable called value and assign it to the value located in the RAM at specific address passed in
            # return value from RAM

        # add ram_write() method - takes in value to write from mdr, and address to write too from mar
            # writes the value to the ram at the specific address passed in

    # inside the run() method
        # add HLT variable with value of 1
        # add LDI variable with value of 2
        # add PRN variable with value of 3

        # read memory address stored in pc & store result in variable ir
        # use ram_read() method and pass in pc+1 and store in variable operand_a
        # use ram_read() method and pass in pc+2 and store in variable operand_b
        
        # set halted to False

        # while not halted
            # set instruction to the program at the current pc count

            # if instruction == HLT 
                # to exit the loop by changing halted to True
                # increment pc by 1 bite
            # else if instruction == LDI
                # store the 8 value in a given register
                # increment pc by 3 bites
            # else if instruction == PRN
                # print the value in a register
                # increment pc by 2 bites
            # otherwise
                # print error message