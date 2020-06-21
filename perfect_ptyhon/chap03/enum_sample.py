from enum import Enum

class UserType(Enum):
  GUEST = 1
  MEMBER = 2
  ADMIN = 3

print(UserType.GUEST)
print(UserType.GUEST.name)
print(UserType.GUEST.value)

class Color(Enum):
  RED = (255, 0, 0)
  GREEN = (0, 255, 0)
  BLUE = (0, 0, 255)

print(Color['RED'])