import random
import Operators as op


class SHA256:
    def __init__(self,message):
        self.saltval = op.bintohex(op.inttobin(random.getrandbits(128)))
        self.originalmessage = message

        for index in range (2):
            if index == 1:
                self.message = self.originalmessage + self.saltval
            else:
                self.message = self.originalmessage

            # ---------Initial Hash Values-------
            # these hash values change for each 512 bit chunk
            h0 = op.hextobin("0x6a09e667")
            h1 = op.hextobin("0xbb67ae85")
            h2 = op.hextobin("0x3c6ef372")
            h3 = op.hextobin("0xa54ff53a")
            h4 = op.hextobin("0x510e527f")
            h5 = op.hextobin("0x9b05688c")
            h6 = op.hextobin("0x1f83d9ab")
            h7 = op.hextobin("0x5be0cd19")

            # --------Initial Constants-------
            # these are constants used in the calculations
            constants = [op.hextobin("0x428a2f98"), op.hextobin("0x71374491"), op.hextobin("0xb5c0fbcf"), op.hextobin("0xe9b5dba5"),
                         op.hextobin("0x3956c25b"), op.hextobin("0x59f111f1"), op.hextobin("0x923f82a4"), op.hextobin("0xab1c5ed5"),
                         op.hextobin("0xd807aa98"), op.hextobin("0x12835b01"), op.hextobin("0x243185be"), op.hextobin("0x550c7dc3"),
                         op.hextobin("0x72be5d74"), op.hextobin("0x80deb1fe"), op.hextobin("0x9bdc06a7"), op.hextobin("0xc19bf174"),
                         op.hextobin("0xe49b69c1"), op.hextobin("0xefbe4786"), op.hextobin("0x0fc19dc6"), op.hextobin("0x240ca1cc"),
                         op.hextobin("0x2de92c6f"), op.hextobin("0x4a7484aa"), op.hextobin("0x5cb0a9dc"), op.hextobin("0x76f988da"),
                         op.hextobin("0x983e5152"), op.hextobin("0xa831c66d"), op.hextobin("0xb00327c8"), op.hextobin("0xbf597fc7"),
                         op.hextobin("0xc6e00bf3"), op.hextobin("0xd5a79147"), op.hextobin("0x06ca6351"), op.hextobin("0x14292967"),
                         op.hextobin("0x27b70a85"), op.hextobin("0x2e1b2138"), op.hextobin("0x4d2c6dfc"), op.hextobin("0x53380d13"),
                         op.hextobin("0x650a7354"), op.hextobin("0x766a0abb"), op.hextobin("0x81c2c92e"), op.hextobin("0x92722c85"),
                         op.hextobin("0xa2bfe8a1"), op.hextobin("0xa81a664b"), op.hextobin("0xc24b8b70"), op.hextobin("0xc76c51a3"),
                         op.hextobin("0xd192e819"), op.hextobin("0xd6990624"), op.hextobin("0xf40e3585"), op.hextobin("0x106aa070"),
                         op.hextobin("0x19a4c116"), op.hextobin("0x1e376c08"), op.hextobin("0x2748774c"), op.hextobin("0x34b0bcb5"),
                         op.hextobin("0x391c0cb3"), op.hextobin("0x4ed8aa4a"), op.hextobin("0x5b9cca4f"), op.hextobin("0x682e6ff3"),
                         op.hextobin("0x748f82ee"), op.hextobin("0x78a5636f"), op.hextobin("0x84c87814"), op.hextobin("0x8cc70208"),
                         op.hextobin("0x90befffa"), op.hextobin("0xa4506ceb"), op.hextobin("0xbef9a3f7"), op.hextobin("0xc67178f2")]

            # -----------------Padding-----------------
            # This sections initializes the first 16 "words". Each "word" is 32 bits.

            # words is a list that stores the 32 bit 'words'
            words = []

            # gets the message input and turns it into binary
            paddedmessage = op.stringtobin(self.message)

            # takes the length of the padded message, converts it into bits, and stores it in bitsinmessage
            bitsinmessage = op.inttobin(len(paddedmessage))
            # adds a one to the end of the padded message
            paddedmessage += "1"

            # adds 0's to make the length of  (paddedmessage - the length of bitsinmessage) a multiple of 512
            while (len(paddedmessage) + len(bitsinmessage)) % 512 != 0:
                paddedmessage += "0"

            # adds bits in messsage to the end of padded message
            paddedmessage += bitsinmessage

            # creates a variable called fullmessage which is the padded message and is not affected
            fullmessage = paddedmessage

            # for each 512-bit chunk of full message (represented my paddedmessage)the following happens
            for z in range(len(paddedmessage) // 512):
                words = []
                # takes the chunk and seperates it into 16, 32 bit words
                paddedmessage = fullmessage[512 * z: 512 * (z + 1)]
                for i in range(int(16)):
                    words.append(paddedmessage[32 * i: 32 * (i + 1)])

                # ----------Creating the 64 words from the first 16-------

                # creates the other 48 words using the first 16
                for i in range(16, 64):

                    s0 = op.bitxor(op.bitxor(op.rightrotate(words[i - 15], 7), op.rightrotate(words[i - 15], 18)),
                                op.rightshift(words[i - 15], 3))
                    s1 = op.bitxor(op.bitxor(op.rightrotate(words[i - 2], 17), op.rightrotate(words[i - 2], 19)),
                                op.rightshift(words[i - 2], 10))

                    sum1 = op.bitadd(words[i - 16], s0)
                    sum2 = op.bitadd(words[i - 7], s1)
                    total = op.bitadd(sum1, sum2)
                    while len(total) < 32:
                        total = "0" + total

                    # Only take the first 32 bits, starting from the right by chopping of the first 8 bytes
                    # if its bigger
                    if len(total) > 32:
                        total = total[8:]

                    # adds the new word into the list of words
                    words.append(total)

                #     for i in range(len(words)):
                #        print(str((i+1)) + ") " + str(words[i]))

                # -----Initialize variables to initial hash values, as they will change-----
                a = h0
                b = h1
                c = h2
                d = h3
                e = h4
                f = h5
                g = h6
                h = h7

                # Checks to make sure the bit length of any variable doesn't exceed 32
                for i in range(0, 64):
                    if len(a) > 32:
                        a = a[8:]
                    if len(b) > 32:
                        b = b[8:]
                    if len(c) > 32:
                        c = c[8:]
                    if len(d) > 32:
                        d = d[8:]
                    if len(e) > 32:
                        e = e[8:]
                    if len(f) > 32:
                        f = f[8:]
                    if len(g) > 32:
                        g = g[8:]
                    if len(h) > 32:
                        h = h[8:]

                    # The Main Algorithm
                    S1 = op.bitxor(op.bitxor(op.rightrotate(e, 6), op.rightrotate(e, 11)), op.rightrotate(e, 25))
                    ch = op.bitxor(op.bitand(e, f), op.bitand(op.bitnot(e), g))
                    temp1 = op.bitadd(op.bitadd(op.bitadd(op.bitadd(h, S1), ch), constants[i]), words[i])
                    S0 = op.bitxor(op.bitxor(op.rightrotate(a, 2), op.rightrotate(a, 13)), op.rightrotate(a, 22))
                    maj = op.bitxor(op.bitxor(op.bitand(a, b), op.bitand(a, c)), op.bitand(b, c))
                    temp2 = op.bitadd(S0, maj)

                    # Variable Swaps
                    h = g
                    g = f
                    f = e
                    e = op.bitadd(d, temp1)
                    d = c
                    c = b
                    b = a
                    a = op.bitadd(temp1, temp2)

                # Add each letter to its corresponding hash value
                h0 = op.bitadd(h0, a)
                h1 = op.bitadd(h1, b)
                h2 = op.bitadd(h2, c)
                h3 = op.bitadd(h3, d)
                h4 = op.bitadd(h4, e)
                h5 = op.bitadd(h5, f)
                h6 = op.bitadd(h6, g)
                h7 = op.bitadd(h7, h)

            # Convert to Hex, then to a string.
            h0 = str(op.bintohex(h0))
            h1 = str(op.bintohex(h1))
            h2 = str(op.bintohex(h2))
            h3 = str(op.bintohex(h3))
            h4 = str(op.bintohex(h4))
            h5 = str(op.bintohex(h5))
            h6 = str(op.bintohex(h6))
            h7 = str(op.bintohex(h7))

            # Cut off if the length of the hex string is greater than 8
            if len(h0) > 8:
                h0 = h0[len(h0) - 8:]
            if len(h1) > 8:
                h1 = h1[len(h1) - 8:]
            if len(h2) > 8:
                h2 = h2[len(h2) - 8:]
            if len(h3) > 8:
                h3 = h3[len(h3) - 8:]
            if len(h4) > 8:
                h4 = h4[len(h4) - 8:]
            if len(h5) > 8:
                h5 = h5[len(h5) - 8:]
            if len(h6) > 8:
                h6 = h6[len(h6) - 8:]
            if len(h7) > 8:
                h7 = h7[len(h7) - 8:]

            # Concatenate the strings
            if index == 0:
                self.finalhash = h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7
            else:
                self.finalsalt = h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7

    def hash(self):
        return self.finalhash

    def salt (self):
        return self.finalsalt

message = SHA256('abc')


print(message.hash())
print(message.saltval)
print(message.salt())

check = SHA256(message.originalmessage + message.saltval)
print(check.hash())




