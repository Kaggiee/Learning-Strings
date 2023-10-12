def main():
    """
    This function will initiate the variables at zero, then open the text file. It will read it
    and split it to make the data easier to parse, and then count how many lines (sentences)
    there are. The number of words are calculated by the length of the split file as an array.
    Using a for loop, the program will determine which characters are uppercase, lowercase,
    and how many digits there are before adding that amount to the corresponding counter. Then,
    the average is calculated and the results are displayed.
    """
    words = 0
    sentences = 0
    upper = 0
    lower = 0
    digits = 0

    infile = open('8-data.txt', 'r', encoding='UTF-8')
    file = infile.read()
    lines = file.split()
    sentences = file.count('\n')
    sentences += 1
    infile.close()
    words += len(lines)
    for character in file:
        if character.isupper():
            upper += 1
        if character.islower():
            lower += 1
        if character.isdigit():
            digits += 1
        average = (words/sentences)

    print(f'Total words: {words}')
    print(f'Total sentences: {sentences}')
    print(f'Average number of words per line: {average}')
    print(f'Uppercase letters: {upper}')
    print(f'Lowercase letters: {lower}')
    print(f'Digits: {digits}')

# Call the main function.
if __name__ == '__main__':
    main()
