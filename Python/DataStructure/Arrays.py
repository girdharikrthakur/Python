

# Syntax: array(typecode, [elements])

# typecode :

# | Type Code | C Type             | Python Type  | Size (in bytes) | Description                    |
# | --------- | ------------------ | ------------ | --------------- | ------------------------------ |
# | `'b'`     | signed char        | int          | 1 byte          | Integer between - 128 to 127   |
# | `'B'`     | unsigned char      | int          | 1 byte          | Integer between 0 to 255       |
# | `'u'`     | Py\_UNICODE        | Unicode char | 2 or 4 bytes    | Unicode character (deprecated) |
# | `'h'`     | signed short       | int          | 2 bytes         | Short integer                  |
# | `'H'`     | unsigned short     | int          | 2 bytes         | Unsigned short integer         |
# | `'i'`     | signed int         | int          | 2 or 4 bytes    | Integer                        |
# | `'I'`     | unsigned int       | int          | 2 or 4 bytes    | Unsigned integer               |
# | `'l'`     | signed long        | int          | 4 bytes         | Long integer                   |
# | `'L'`     | unsigned long      | int          | 4 bytes         | Unsigned long integer          |
# | `'q'`     | signed long long   | int          | 8 bytes         | Long long integer              |
# | `'Q'`     | unsigned long long | int          | 8 bytes         | Unsigned long long integer     |
# | `'f'`     | float              | float        | 4 bytes         | Floating-point number          |
# | `'d'`     | double             | float        | 8 bytes         | Double precision float         |


from array import array


numbers = array("i", [1, 2, 3, 4])
print(numbers)
numbers.append(1)
print(numbers)
numbers.insert(1, 10)
print(numbers)
numbers.pop()
print(numbers)

