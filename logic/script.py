alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'


def cryp(string, key):

    output = ''

    for i in string: # for letter in string
        if i in alphabet: # if letter exist
            letter_pos = alphabet.index(i) # get letter position

            module = int(letter_pos + key) % len(alphabet) # displacement 
            output += alphabet[module] # new position
        else: # if letter don't exist
            output += i # add original letter

    return output


if __name__ == '__main__':
    s = str(input('Text to cryp: ')).upper()
    k = int(input('Key: '))
    print(cryp(s, k))
