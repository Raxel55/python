def convert_temperature(temperature, unit):
    """convert_temperature(temperature, unit)\n\nConvert a temperature to Fahrenheit from Celsius or conversely.\nKeyword arguments:\ntemperature:\tvalue of temperature.\nunit:\t\t\twhat to convert value to. Can be 'f' or 'c'."""
    if unit.lower() == 'f': return temperature * 1.8 + 32
    if unit.lower() == 'c': return (temperature - 32) / 1.8
    raise Exception("Can't resolve unit")


if __name__ == '__main__':
    print(convert_temperature(32, 'C'))
    print(convert_temperature(0, 'f'))
    print(convert_temperature.__doc__)
