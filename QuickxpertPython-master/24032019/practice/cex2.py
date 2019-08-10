def vowels_consonants(parm_string):
    """
    This function will returns vowels count and consonants count.

    :param param_string: contains the string value
    :type param_string: string
    :returns: Count of vowel and consonant in the given string
    :rtype: tuple
    :author: Cmoolya

    """
    vowel_count, conso_count = 0, 0
    valid_vowels = ["a", "A", "E", "e", "I", "i", "O", "o", "U", "u"]
    for each_char in parm_string:
        if each_char in valid_vowels:
            vowel_count = vowel_count + 1
        else:
            if each_char not in [" ", "."]:
                conso_count = conso_count + 1
    return vowel_count, conso_count

if __name__ == "__main__":
    str_inpt = "Hi this is an Orange fruit."
    results = vowels_consonants(str_inpt)
    print("%d Vowels and %d Consonant in %s." % (results[0], results[1], \
                                                              str_inpt))
