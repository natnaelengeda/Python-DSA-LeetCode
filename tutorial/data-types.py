# Nummeric Types
# int -> Immutable
x = 10
y = 20
z = -100

# float -> Immutable
x = 3.14
z = -0.001

# complex -> Immutable
c = 3 + 4j

#Boolean Type
#bool -> Immutable
is_valid = True
is_invalid = False

# Sequence Types
# str -> Immutable
name = "Natty"

#list -> Mutable
numbers = [1,2,3]
numbers.append(4)

#tuple -> Immutable
coordinated = (10,20)

#range -> Immutable
r = range(0,10)

#dict -> Mutable
user = {
  "name": "Natty",
  "age": 24
}

#Set Types
#set -> Mutable
unique_numbers = {1,2,3}

#frozenset -> Immutable
frozen = frozenset([1,2,3])

#Binary Types
#bytes -> Imutable
b = b"hello"

#bytearray -> Mutable
ba = bytearray(b"hello")
ba[0] = 72

#memoryview -> Depends on the Object
data = bytearray(b"hello")
mv = memoryview(data)

#None Type -> Immutable
x = None
