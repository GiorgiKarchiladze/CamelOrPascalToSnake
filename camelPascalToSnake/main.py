import re


def convert_to_pascal_camel_or_snake(string_input, pascal_camel_or_snake):
    # Split the string by camelCase, PascalCase, snake_case, and spaces
    words = re.findall(r'[A-Za-z][^A-Z\s_]*|[A-Za-z]+', string_input)

    if pascal_camel_or_snake.lower() == 'pascal':
        char_list = [word.capitalize() for word in words]
        return ''.join(char_list)

    elif pascal_camel_or_snake.lower() == 'camel':
        char_list = [
            words[0].lower() if i == 0 else word.capitalize()
            for i, word in enumerate(words)
        ]
        return ''.join(char_list)

    elif pascal_camel_or_snake.lower() == 'snake':
        char_list = [word.lower() for word in words]
        return '_'.join(char_list)

    else:
        return "Invalid conversion type specified."


def main():
    print('Type \'exit\' to close the program')
    while True:
        custom_input = input("Would you like to convert to pascal, camel, or snake case?")
        if custom_input.lower() == 'exit':
            break
        elif custom_input.lower() == 'pascal':
            print(convert_to_pascal_camel_or_snake(input("Please input text to convert to pascal: "), 'pascal'))
        elif custom_input.lower() == 'camel':
            print(convert_to_pascal_camel_or_snake(input("Please input text to convert to camel: "), 'camel'))
        elif custom_input.lower() == 'snake':
            print(convert_to_pascal_camel_or_snake(input("Please input text to convert to snake: "), 'snake'))
        else:
            pass


main()