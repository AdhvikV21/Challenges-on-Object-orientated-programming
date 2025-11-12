class RomanConverter:
    def int_to_roman(self, num):
        roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        result = ""
        for value, symbol in roman_map:
            result += symbol * (num // value)
            num %= value
        return result

converter = RomanConverter()
while True:
    try:
        number = input("Enter a number: ")
        print(f"Roman equivalent: {converter.int_to_roman(int(number))}")
    except ValueError:
        print("Invalid input.")