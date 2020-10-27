
class payload:
    def __init__(self, text= None, key = None, encrypted = None):
        self.text = text
        self.key = key
        self.encrypted = encrypted
    
    def encrypt(self):
        self.encrypted = str()
        for i, char in enumerate(self.text):
            c = chr(ord(char) ^ i ^ ord(self.key[ i % len(self.key)]))
            self.encrypted += c

    def decrypt(self):
        self.text = str()
        for i, char in enumerate(self.encrypted):
            c = chr(ord(char) ^ ord(self.key[ i % len(self.key)]) ^ i )
            self.text += c

    def disp(self):
        print(f"Text = {self.text}")
        print(f"Key = {self.key}")
        print(f"Encrypted = {self.encrypted}")


if __name__ == "__main__":
    p = payload(text = "Hello my name is Pulkit", key="key")
    p.encrypt()
    p.disp()

    q = payload(encrypted=p.encrypted, key="key")
    q.decrypt()
    q.disp()