def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result


def convert(val):
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    if dollars == 0 and cents == 0:
        return "Oh, man..."
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string


print convert(11.26)
print convert(0.97)
print convert(0)
print convert(0.01)
print convert(1)
