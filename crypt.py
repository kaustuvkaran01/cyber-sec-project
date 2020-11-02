class payload:
    def __init__(self, text= str(), key = str(), encrypted = str()):
        self.text = text
        self.key = key
        self.encrypted = encrypted
    
    def encrypt(self):
        special_char = list('[@_!#$%^&*()<>?/\\|}{~:+-]')
        result = ""
        s = 0 
        for char in self.key:
            s += ord(char)
        s = s % 26

        for char in self.text: 
            if char not in special_char: 
                if char.isupper(): 
                    result += chr((ord(char) + s-65) % 26 + 65) 
                elif ord(char)==32: 
                    result += ' '
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
            else: 
                result += special_char[(special_char.index(char)+1)%len(special_char)]
        
        for i, char in enumerate(result):
            c = chr(ord(char) ^ i ^ ord(self.key[ i % len(self.key)]))
            self.encrypted += c
        

    def decrypt(self):
        for i, char in enumerate(self.encrypted):
            c = chr(ord(char) ^ ord(self.key[ i % len(self.key)]) ^ i )
            self.text += c

        special_char = list('[@_!#$%^&*()<>?/\\|}{~:+-]') 
        result = ""
        s = 0 
        for char in self.key:
            s += ord(char)
        s = 26 - (s % 26)  
        
        for char in self.text:
            if char not in special_char: 
                if char.isupper(): 
                    result += chr((ord(char) + s-65) % 26 + 65) 
                elif ord(char)==32: 
                    result += ' '
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
            else: 
                result += special_char[(special_char.index(char)-1)%len(special_char)]
        self.text = result


    def disp(self):
        print(f"Text = {self.text}")
        print(f"Key = {self.key}")
        print(f"Encrypted = {self.encrypted}")
        print("#############################\n")


if __name__ == "__main__":
    p = payload(text = "Hello my name is Pulkit\\+-+-", key="Nanny")
    p.disp()
    p.encrypt()
    p.disp()

    q = payload(encrypted=p.encrypted, key="Nanny")
    q.disp()
    q.decrypt()
    q.disp()
