def letters_range(start, stop, step=1):
    return [chr(x) for x in range(ord(start), ord(stop), step)]


print(letters_range('b', 'w', 2))
print(letters_range('a', 'g'))
print(letters_range('g', 'p'))
print(letters_range('p', 'g', -2))
print(letters_range('a', 'a'))
