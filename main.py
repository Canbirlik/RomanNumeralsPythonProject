
def convert_one_roman_digit(rom_str):
    if rom_str == "I":
        return 1
    elif rom_str == "V":
        return 5
    elif rom_str == "X":
        return 10
    elif rom_str == "L":
        return 50
    elif rom_str == "C":
        return 100
    elif rom_str == "D":
        return 500
    elif rom_str == "M":
        return 1000


def roman_to_arabic(roman_string):
    total_number = 0
    prev_number = 0
    number_list = []

    for item in roman_string:
        number_list.append(convert_one_roman_digit(item))

    for nums in reversed(number_list):
        if nums < prev_number:
            total_number -= nums
        else:
            total_number += nums
        prev_number = nums
    return total_number


while True:
    roman_string = input("Please, enter the Roman Numerals: ")
    try:
        arabic_number = roman_to_arabic(roman_string)
        print("Arabic Number:", arabic_number)
    except:
        print("Error, you entered an invalid Roman numeral.")



