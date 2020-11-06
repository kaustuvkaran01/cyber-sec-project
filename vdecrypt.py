from string import punctuation
def vigenereGenerateKey(vigenere_string, vigenere_key):
    vigenere_key = list(vigenere_key)
    if len(vigenere_string) == len(vigenere_key):
        return(vigenere_key)
    else:
        for i in range(len(vigenere_string) - len(vigenere_key)):
            vigenere_key.append(vigenere_key[i % len(vigenere_key)])
    return("" . join(vigenere_key))


def vigenereOriginalText(vigenere_decrypt_cipher_text, vigenere_key):
    vigenere_orig_text = []
    for i in range(len(vigenere_decrypt_cipher_text)):
        x = (ord(vigenere_decrypt_cipher_text[i]) - ord(vigenere_key[i]) + 26) % 26
        x += ord('A')
        vigenere_orig_text.append(chr(x))
    return("" . join(vigenere_orig_text))


if __name__ == "__main__":

    vigenere_decrypt_cipher_text = input("Cipher text: ")
    vigenere_decrypt_cipher_text = vigenere_decrypt_cipher_text.upper()
    keyword = input("Key: ")
    keyword = keyword.upper()

#prepare.py
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
        if i not in (punctuation+" "):
            vigenere_key = vigenereGenerateKey(i,keyword)
            result += vigenereOriginalText(i, vigenere_key)
        else:
            result += i
    print(result)

