class ClassicCiphers:
    @classmethod
    def encrypt(self, plaintext, key):
        if (key >= 25 or key <= 0):
            print "Key should be less than 25 and larger than 0"
        else:
            encrypted_string = ""
            for i in (plaintext):
                letter = ord(i)
                if (64 < letter < 91):
                    char = ((letter - 65 + key) % 26)
                    encrypted_string += str(chr(char+65))
                elif (96 < letter < 123):
                    char = ((letter - 97 + key) % 26)
                    encrypted_string += str(chr(char+97))
                else:
                    encrypted_string += i
            return encrypted_string

    @classmethod
    def decrypt(self, ciphertext, key):
        if (key >= 25 or key <= 0):
            print "Key should be less than 25 and larger than 0"
        else:
            decrypted_string = ""
            for i in (ciphertext):
                letter = ord(i)
                if (64 < letter < 91):
                    char = ((letter - 65 - key) % 26)
                    decrypted_string += str(chr(char+65))
                elif (96 < letter < 123):
                    char = ((letter - 97 - key) % 26)
                    decrypted_string += str(chr(char+97))
                else:
                    decrypted_string += i
            return decrypted_string

    @classmethod
    def mapStringWithKeyword(self, ciphertext, keyword):
        text = ciphertext.split()
        for word in text:
            if len(word) == len(keyword):
                attempt = self.bruteDecrypt(word)
                for string in attempt:
                    if string == keyword:
                        return self.calculateKey(word[0], keyword[0])

    @classmethod
    def calculateKey(self, cipherLetter, keyLetter):
        i = 0
        decryptedLetters = self.bruteDecrypt(cipherLetter)
        for letter in decryptedLetters:
            i += 1
            if letter == keyLetter:
                return i

    @classmethod
    def bruteDecrypt(self, ciphertext, keyword=""):
        if keyword:
            key = self.mapStringWithKeyword(ciphertext, keyword)
            return self.decrypt(ciphertext, key)
        else:
            deciphered = []
            for i in range(1, 25):
                deciphered.append(self.decrypt(ciphertext, i))
            return deciphered

ciphers = ClassicCiphers()
print ciphers.encrypt("Get me a vanilla ice cream, make it double", 6)
print ciphers.encrypt("I don't much care for Leonard Cohen", 15)
print ciphers.encrypt("I like root beer floats", 16)

print ciphers.decrypt("nduzs ftq buzq oazqe", 12)
print ciphers.decrypt("fdhvdu qhhgv wr orvh zhljkw", 3)
print ciphers.decrypt("ufgihxm uly numnys", 20)

print ciphers.bruteDecrypt("gryy gurz gb tb gb nzoebfr puncry", "chapel")
print ciphers.bruteDecrypt("wziv kyv jyfk nyve kyv tpdsrcj tirjy", "cymbals")
print ciphers.bruteDecrypt("baeeq klwosjl osk s esf ozg cfwo lgg emuz")

