def encrypt(text,s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            result+=chr((ord(char)+s-89)%67+90)
        else:
            result+=chr((ord(char)+s-89)%67+90)
    return result
text="attackaction"
s=4
print("text:"+text)
print("shift:"+str(s))
print("cipher:"+encrypt(text,s))
            
