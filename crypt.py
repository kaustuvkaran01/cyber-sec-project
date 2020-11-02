class payload:
    def __init__(self, text= str(), key = str(), encrypted = str()):
        self.text = text
        self.key = key
        self.encrypted = encrypted
    
    def cipherText(self):
        special_char = list('[@_!#$%^&*()<>?/\|}{~:+-]')
        result = ""
        s = 0 
        for i in range(len(self.key)):
            s += ord(self.key[i])
        s = s % 26  

        for i in range(len(self.text)):
            char = self.text[i] 
            if char not in special_char: 
                if (char.isupper()): 
                    result += chr((ord(char) + s-65) % 26 + 65) 
                elif(ord(char)==32): 
                    result += ' '
                else: 
                    result += chr((ord(char) + s - 97) % 26 + 97)
            else: 
                result += special_char[(special_char.index(char)+1)%len(special_char)]
        self.text = result

    def originalText(self): 
        special_char = list('[@_!#$%^&*()<>?/\|}{~:+-]') 
        result = ""
        s = 0 
        for i in range(len(self.key)):
            s += ord(self.key[i])
        s = 26 - (s % 26)  

        for i in range(len(self.encrypted)):
            char = self.encrypted[i]
            if char not in special_char: 
                if (char.isupper()): 
                    result += chr((ord(char) + s-65) % 26 + 65) 
                elif(ord(char)==32): 
                    result += ' '
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
            else: 
                result += special_char[(special_char.index(char)-1)%len(special_char)]
        self.text = result

    def encrypt(self):
        self.disp()
        self.cipherText()
        self.disp()
        for i, char in enumerate(self.text):
            c = chr(ord(char) ^ i ^ ord(self.key[ i % len(self.key)]))
            self.encrypted += c
        self.disp()

    def decrypt(self):
        deciper_str = self.encrypted
        self.encrypted = ''
        for i, char in enumerate(deciper_str):
            c = chr(ord(char) ^ ord(self.key[ i % len(self.key)]) ^ i )
            self.encrypted += c
        self.disp()
        self.originalText()
        self.disp()

    def disp(self):
        print(f"Text = {self.text}")
        print(f"Key = {self.key}")
        print(f"Encrypted = {self.encrypted}")


if __name__ == "__main__":
    p = payload(text = "Hello my name is Pulkit+-+-", key="group of keys")
    p.encrypt()   
    q = payload(encrypted=p.encrypted, key="group of keys")
    q.decrypt()
