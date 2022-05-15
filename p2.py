#caeser cipher
def cipher(string, offset):
    BASE = 26
    #offset = offset % BASE
    first_letter = ord('a')
    last_letter = ord('z')
    code = ""
    for letter in string:
        new_char = chr(int(ord(letter))-int(offset))
        #print('1', new_char, ord(new_char))
        if(ord(new_char)<first_letter):
            #print('2', new_char, ord(new_char))
            new_char = chr(ord(new_char)+BASE)
        code += new_char
    return code
    
while(True):
    string = input("Enter a word: ")
    if string.isalpha():
        break

string = string.split(" ")[0]

while(True):
    offset = input("Enter offset: ")
    if offset.isdigit():
        break

print(cipher(string, offset))
        