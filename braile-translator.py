def translate_to_braille(space_station_sign):

    # base for braille alphabet
    a_through_j = [
    '100000', #a
    '110000', #b
    '100100', #c
    '100110', #d
    '100010', #e
    '110100', #f
    '110110', #g
    '110010', #h
    '010100', #i
    '010110'  #j
    ]

    k_through_t = []
        
    for letter in a_through_j:
        new_character = letter[:2] +'1'+letter[3:]
        k_through_t.append(new_character)

    u_through_z = []

    for i in range(5):
        letter = k_through_t[i]
        new_character = letter[:5]+'1'
        u_through_z.append(new_character)

    add_w = '010111'
    u_through_z.insert(2, add_w)

    white_space = '000000'
    u_through_z.append(white_space)

    # braille alphabet completed
    braille_alphabet = a_through_j + k_through_t + u_through_z

    translation = ''

    for c in space_station_sign:

        if(c.isupper()) == True:
            unicode_value = ord(c.lower())
            position = unicode_value - 97
            cap_sign = '000001'
            translation += cap_sign
            translation += braille_alphabet[position]
        else:
            unicode_value = ord(c)
            if unicode_value == 32:
                white_space = '000000'
                translation += braille_alphabet[-1]
            else:
                position = unicode_value - 97
                translation += braille_alphabet[position]

    return translation
                
print (translate_to_braille('Braille'))
