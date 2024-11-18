## Multiple Inheritance
from inheritance import Superhero


# Another class definition
# bat.py
class Bat:
    species = "Baty"

    def __init__(self, can_fly=True):
        self.fly = can_fly

    # This class also has a say method
    def say(self, msg):
        msg = "... ... ..."
        return msg

    # And its own method as well
    def sonar(self):
        return "))) ... ((("


# if __name__ == "__main__":
# b = Bat()
# print(b.say("hello"))
# print(b.fly)


class Batman(Superhero, Bat):
    def __init__(self, *args, **kwargs):
        Superhero.__init__(
            self, "anonymous", movie=True, superpowers=["Wealthy"], *args, **kwargs
        )
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # override the value for the name attribute
        self.name = "Sad Affleck"

    # This class has a say method
    def say(self, msg):
        msg = "%s %s" % (self.name, msg)
        return msg

    def sing(self):
        return "nan nan nan nan nan batman!"


if __name__ == "__main__":
    sup = Batman()

    # The Method Resolution Order
    print(Batman.__mro__)  # => (<class '__main__.Batman'>,
    # => <class 'superhero.Superhero'>,
    # => <class 'human.Human'>,
    # => <class 'bat.Bat'>, <class 'object'>)

    # Calls parent method but uses its own class attribute
    print(sup.get_species())  # => Superhuman

    # Calls overridden method
    print(sup.sing())  # => nan nan nan nan nan batman!

    # Calls method from Human, because inheritance order matters
    sup.say("I agree")  # => Sad Affleck: I agree

    # Call method that exists only in 2nd ancestor
    print(sup.sonar())  # => ))) ... (((

    # Inherited class attribute
    sup.age = 100
    print(sup.age)  # => 100

    # Inherited attribute from 2nd ancestor whose default value was overridden.
    print("Can I fly? " + str(sup.fly))  # => Can I fly? False
