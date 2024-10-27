alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):#h
    cipher=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position+shift_key
            cipher+=alphabet[new_position]
        else:
            cipher+=char
    print(f"here is the text after encryption:{cipher}")
def decryption(cipher,shift_key):#h
    plain_text=""
    for char in cipher:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position-shift_key
            plain_text+=alphabet[new_position]
        else:
            cipher+=char
    print(f"here is the text after decryption:{plain_text}")
wanna_play=False
while not wanna_play:
    what_to_do=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:")
    text=input("Enter the text to encrypt:").lower()
    shift=int(input("Enter shift key:"))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(cipher=text,shift_key=shift)
    play_again=input("type 'yes' to continue, type 'no' to exit:\n ")
    if play_again=='no':
        wanna_play=True
        print("Bye")
