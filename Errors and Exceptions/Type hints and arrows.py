
# Type hints shows the datatype of a variable
can_drive: bool
can_drink: bool


def police_check(age: int) -> bool: # -> Type arrows are used to show expected data types of return
    if age >= 18:
        can_drive = True
        can_drink = True
    else:
        can_drive = False
        can_drink = False
    return "True"


if police_check(15):
    print("Allow to pass")
else:
    print("Charge fine")

if police_check("twenty"):
    print("You can go")
