def convert_to_snake_case(pascal_or_camel_cased_string):
    """
    create a list comprehension to iterate through each character in the input string
    if the character is uppercase, add an underscore before it and convert it to lowercase
    otherwise, keep the character as it is
    """
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
    # join the characters in the list to form the snake-cased string and remove leading underscores
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))

if __name__ == '__main__':
    main()