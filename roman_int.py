import re


def validate(roman):
    return bool(
        re.search(
            r"^(M{0,3})(D?[C]{0,3}|C[DM])(L?[X]{0,3}| X[LC])(V?[I]{0,3}|I[VX])$", roman
        )
    )


def roman_to_int(roman):
    int_val = 0
    for i in range(len(roman)):
        if i > 0 and rom_val[roman[i]] < rom_val[roman[i - 1]]:
            intval += rom_val[roman[i]] - 2 * rom_val[roman[i - 1]]
        else:
            int_val = rom_val[roman[i]]
    return int_val


rom_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
roman = input("enter a number in roman")
res = validate(roman)
if res:
    print("can be done")
    result = roman_to_int(roman)
    print(result)
else:
    print("not")
