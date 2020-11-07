from string import punctuation


class payload:
    def __init__(self, text=str(), key=str(), encrypted=str()):
        self.text = text
        self.key = key
        self.encrypted = encrypted
        self.intermediate_encrypted = ""

    def vigenereGenerateKeyDecryption(self, vigenere_string, vigenere_key):
        vigenere_key = list(vigenere_key)
        if len(vigenere_string) == len(vigenere_key):
            return(vigenere_key)
        else:
            for i in range(len(vigenere_string) - len(vigenere_key)):
                vigenere_key.append(vigenere_key[i % len(vigenere_key)])
        return("" . join(vigenere_key))

    def vigenereOriginalTextDecryption(self, vigenere_decrypt_cipher_text, vigenere_key):
        vigenere_orig_text = []
        for i in range(len(vigenere_decrypt_cipher_text)):
            x = (
                ord(vigenere_decrypt_cipher_text[i]) - ord(vigenere_key[i]) + 26) % 26
            x += ord('A')
            vigenere_orig_text.append(chr(x))
        return("" . join(vigenere_orig_text))

    def generateVigenereKeyEncryption(self, string, key):
        count = 0
        key = list(key)
        if len(string) == len(key):
            return(key)
        else:
            for i in range(len(string) - len(key)):
                count += 1
                key.append(key[i % len(key)])
        return("" . join(key))

    def vcipherTextEncryption(self, string, key):
        vigenere_cipher_text = []
        for i in range(len(string)):
            x = (ord(string[i]) + ord(key[i])) % 26
            x += ord('A')
            vigenere_cipher_text.append(chr(x))
        return("" . join(vigenere_cipher_text))

    def encrypt(self):
        # Kaustuv and Parth's encryption starts
        string = self.text.upper()
        keyword = self.key.upper()
        processedTextList = []
        processedText = ""

        for i in string:
            if i not in (punctuation + " " + "0123456789"):
                processedText += i
            else:
                processedTextList.append(processedText)
                processedTextList.append(i)
                processedText = ""
        if processedText != "":
            processedTextList.append(processedText)
        while '' in processedTextList:
            processedTextList.remove('')
        for i in processedTextList:
            if i not in (punctuation+" "+"0123456789"):
                key = self.generateVigenereKeyEncryption(i, keyword)
                self.intermediate_encrypted += self.vcipherTextEncryption(
                    i, key)
            else:
                self.intermediate_encrypted += i

        # dipesh encryption starts
        special_char = list('[@_!#$%^&*()<>?/\\|}{~:+-]')
        result = ""
        s = 0
        for char in self.key:
            s += ord(char)
        s = s % 26

        for char in self.intermediate_encrypted:
            if char not in special_char:
                if char.isnumeric():
                    result += chr(ord(char) + s % 10)
                elif char.isupper():
                    result += chr((ord(char) + s-65) % 26 + 65)
                elif ord(char) == 32:
                    result += ' '
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
            else:
                result += special_char[(special_char.index(char)+1) % len(special_char)]
        self.intermediate_encrypted = result

        # dipesh encryption ends

        # pulkit encryption starts
        for i, char in enumerate(self.intermediate_encrypted):
            c = chr(ord(char) ^ i ^ ord(self.key[i % len(self.key)]))
            self.encrypted += c

        # pulkit encryption ends

    def decrypt(self):
        # pulkit decryption starts
        for i, char in enumerate(self.encrypted):
            c = chr(ord(char) ^ ord(self.key[i % len(self.key)]) ^ i)
            self.text += c

        # pulkit decryption ends

        # dipesh decryption starts
        special_char = list('[@_!#$%^&*()<>?/\\|}{~:+-]')
        result = ""
        s = 0
        for char in self.key:
            s += ord(char)
        s = 26 - (s % 26)

        for char in self.text:
            if char not in special_char:
                if char.isnumeric():
                    result += chr(ord(char) - (26-s) % 10)
                elif char.isupper():
                    result += chr((ord(char) + s-65) % 26 + 65)
                elif ord(char) == 32:
                    result += ' '
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
            else:
                result += special_char[(special_char.index(char)-1) % len(special_char)]
        self.text = result

        # dipesh decryption ends

        # Kaustuv and Parth's decryption starts
        vigenere_decrypt_cipher_text = self.text.upper()
        keyword = self.key.upper()
        processedTextList = []
        processedText = ""

        for i in vigenere_decrypt_cipher_text:
            if i not in (punctuation + " " + "0123456789"):
                processedText += i
            else:
                processedTextList.append(processedText)
                processedTextList.append(i)
                processedText = ""
        if processedText != "":
            processedTextList.append(processedText)
        while '' in processedTextList:
            processedTextList.remove('')
        result = ""
        for i in processedTextList:
            if i not in (punctuation+" "+"0123456789"):
                vigenere_key = self.vigenereGenerateKeyDecryption(i, keyword)
                result += self.vigenereOriginalTextDecryption(i, vigenere_key)
            else:
                result += i
        self.text = result
        # Kaustuv and Parth's decryption ends

    def disp(self):
        print(f"Text = {self.text}")
        print(f"Key = {self.key}")
        print(f"Encrypted = {self.encrypted}")
        print("#############################\n")


if __name__ == "__main__":
    option = input("Enter the option e for encryption and d for decryption: ")

    if option == "e":
        inp_text = input("Enter the string to be encrypted: ")
        inp_key = input("Enter the key: ")
        p = payload(text=inp_text, key=inp_key)
        p.encrypt()
        print(f"Encrypted string: {p.encrypted}")

    if option == "d":
        inp_encrypted = input("Enter the encrypted string: ")
        inp_key = input("Enter the key: ")
        q = payload(encrypted=inp_encrypted, key=inp_key)
        q.decrypt()
        print(f"Decrypted string: {q.text}")
