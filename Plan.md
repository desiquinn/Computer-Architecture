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

# Day 2 MVP
   
    # Inside the load() method
        # if there is no sys.argv[1]
            # print an error message
        # else Open a file dynamically from examples directory (using sys.argv[1])
            # for every line in this file
                # slice out everything that is after a ', #'
                # if it is a blank line 
                    # ignore it (continue)
                # else 
                    # convert the binary number to an interger
                    # save it to the ram at the current address
                    # increment address

    # Inside the alu() method
        # else if op == "MUL"
            # get value from reg A and get value from reg B, mulitply and assign to reg A
    
    # Inside run() method
        # add MUL to the instructions list with machine code 0b10100010

        # add to the while loop
            # if the ir is equal to the MUL
                # invoke alu(op,reg_a, reg_b)
                # increment pc by 3