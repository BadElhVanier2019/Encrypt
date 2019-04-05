def stringtobin(message):
    # creates a variable called bits total where the bits will be stored
    bitstotal = ""
    # this loop runs the for the length of the message that needs to be converted
    for i in range(len(message)):
        # when using the bin function, a '0b' is added to the start of it,the [2:0] removes it
        char = bin(ord(message[i]))[2:]
        # adds enough leading zeros to create a byte
        while len(char) < 8:
            char = "0" + char
        # adds the byte value of the character to the variable bitstotal
        bitstotal += char
    return (bitstotal)


def bintostring(binarymessage):
    # total is where the string will be stored
    total = ""
    # for each byte, it is converted to base 10 and then converted to an ascii value
    for i in range(len(binarymessage) // 8):
        byte = binarymessage[8 * i: 8 * (i + 1)]
        byte = int(byte, 2)
        char = chr(byte)
        # after its converted into the character, it is stored in total
        total += char
    return total


def inttobin(integertoconvert):
    # converts the number into binary and removes the '0b'
    binarynumber = bin(integertoconvert)[2:]
    # if the length of the integer is not a multiple of 8 (a byte), it adds leading 0's
    while len(binarynumber) % 8 != 0:
        binarynumber = "0" + binarynumber

    return binarynumber


def bintoint(string):
    # takes the input in bits, and converts it to base 2
    decimal = int(string, 2)
    return decimal


def hextobin(hexval):
    # takes the hexvalue converts it into base 10
    decimal = int(hexval, 16)
    # ueses intobin function to convert to binary
    result = inttobin(decimal)
    return result


def bintohex(binval):
    # takes the binary number and converts it into base 10
    decimal = int(binval, 2)
    # takes converts the base 10 number to a hex
    result = hex(decimal)[2:]
    # if the hex value is less than 8, it adds leading zeros
    while len(result) < 8:
        result = "0" + result
    return result


# ---------Bitwise Operators---------
def bitxor(input1, input2):
    # Convert to base 10
    bit1 = bintoint(input1)
    bit2 = bintoint(input2)

    # XOR the numbers
    result = bit1 ^ bit2

    # Convert to base 2
    result = inttobin(result)
    return result


def bitadd(input1, input2):
    # Convert to base 10
    bit1 = bintoint(input1)
    bit2 = bintoint(input2)

    # Add the numbers
    result = bit1 + bit2
    # Convert to base 2
    result = inttobin(result)
    return result


def bitnot(bitinput):
    result = ""
    # checks each bit and gets the compliment of it
    for i in range(len(bitinput)):
        # if the bitinput is a 0, the result will be a 1
        if bitinput[i] == "1":
            result += "0"
        else:
            # if the bitinput is a 1, the result will be 0
            result += "1"

    return result


def bitand(input1, input2):
    # Convert to base 10
    bit1 = bintoint(input1)
    bit2 = bintoint(input2)

    # "AND" the numbers
    result = bit1 & bit2
    # Convert to base 2
    result = inttobin(result)
    return result


# -----Bit Manipulation Functions---------
def rightrotate(strinput, amount):
    # Get the full string
    stringfull = strinput
    string = strinput
    for i in range(amount):
        # Set the first value to the last character
        string = stringfull[len(stringfull) - 1]
        # The for loop adds in the other characters to the right
        for g in range(0, len(strinput) - 1):
            string += stringfull[g]

        stringfull = string

    return string


# Leftrotate is not used in the hash function. I realized this after I made it
def leftrotate(strinput, amount):
    stringfull = strinput
    string = strinput
    for i in range(amount):
        # Set the last character of string to the first value of stringfull
        string = stringfull[0]
        for g in range(1, len(strinput)):
            # Add in the other characters to the left
            string = stringfull[len(strinput) - g] + string

        stringfull = string

    return string


def rightshift(strinput, amount):
    # Convert to base 10
    bit = bintoint(strinput)

    # Perform the Operation
    result = bit >> amount

    # Convert to base 2
    result = inttobin(result)

    return result


