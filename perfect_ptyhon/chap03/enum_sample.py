from enum import Enum

class UserType(Enum):
  GUEST = 1
  MEMBER = 2
  ADMIN = 3

print(UserType.GUEST)
print(UserType.GUEST.name)
print(UserType.GUEST.value)