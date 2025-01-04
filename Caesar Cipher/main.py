from art import logo

print(logo)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(original_text,key,encode_or_decode):
    output_text = ''


    if encode_or_decode == 'decode':
        key *= -1
        
    for char in original_text:
        if char in alphabet:
            shifted_position = alphabet.index(char)
            new_position = shifted_position+key
            output_text += alphabet[new_position]
        else:
            output_text += char
    print(f"The {direction}d text is {output_text}")
    
should_contiue = True
while should_contiue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("type your message:\n").lower()
    shift = int(input("type the shift number:\n"))

    shift = shift%26
    caesar(text,shift,direction)

    result = input("Type 'yes' if you want to go again.Otherwise type 'no'.\n").lower()
    if result == 'no':
        should_contiue=False





