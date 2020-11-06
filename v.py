from string import punctuation


def generateVigenereKey(string, key):
    count = 0
    key = list(key)
    print(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            print("String - Key ", count)
            count += 1
            key.append(key[i % len(key)])
    return("" . join(key))


def vcipherText(string, key):
    vigenere_cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        vigenere_cipher_text.append(chr(x))
    return("" . join(vigenere_cipher_text))


if __name__ == "__main__":
    string = input("PlainText : ")
    string = string.upper()
    keyword = input("Key: ")
    keyword = keyword.upper()
    # Prepare.py
    processedTextList = []
    processedText = ""
    print(punctuation + " ")

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
    print(processedTextList)
    result = ""
    for i in processedTextList:
        if i not in (punctuation+" "):
            key = generateVigenereKey(i, keyword)
            result += vcipherText(i, key)
        else:
            result += i


# Back to main
    vigenere_cipher_text = result
    print("Ciphertext :", vigenere_cipher_text)
    # print("Original/Decrypted Text :",vplainText(vigenere_cipher_text, key))
