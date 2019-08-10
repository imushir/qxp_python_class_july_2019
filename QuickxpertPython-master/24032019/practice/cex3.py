def vowels_consonant(string_param):
    """
    This function will returns vowels count and consonants count.

    :param string_param: contains string value
    :param type: String
    :returns: Count of vowel and consonant in the given string
    :rtype: tuple
    :author: Cmoolya

    """

    vowel_count, consonant_count = 0, 0
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    for each_char in string_param:
        if each_char in vowels:
            vowel_count = vowel_count + 1
        else:
            if each_char.isalpha():
                consonant_count = consonant_count + 1
    return vowel_count, consonant_count

if __name__ == "__main__":
    user_input = "apple orange are fruits OoOoO."
    results = vowels_consonant(user_input)
    print("%d Vowels and %d Consonants in %s." % (results[0], results[1], \
                                                              user_input))

