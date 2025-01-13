"""Learn classes in Python."""


# We use the "class" statement to create a class
class Human:
    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"  # Người khôn ngoan

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by Python but that live in user-controlled namespaces.
    # Methods(or objects or attributes) like: __init__, __str__, __len__repr__ etc...abs
    # are called special methods (or sometimes called under methods).
    # You should not invent such names on your own.
    def __init__(self, name):
        # Assign the argument to the instance's "name" attribute
        self.name = name
        # Initialize property
        self._age = 0
        # the leading underscore indicates the "age" property is intended to be used internally
        # do not rely on this to be enforced: it's a hint to other developers

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))
        print(f"{self.name}: {msg}")

    # Another instance method
    def sing(self):
        return "yo... yo... microphone check... one two... one two..."

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into a read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    # @age.deleter
    # def age(self):
    #     del self._age


if __name__ == "__main__":
    print(Human.grunt())  # => "*grunt*"
    print(Human.get_species())  # => "H. sapiens"

    # Create an instance of the class
    bob = Human("Bob")
    print(bob.name)  # => "Bob"

    # Call an instance method
    bob.say("Hi there!")
    bob.say("What's up?")
    # del bob.age // if you want to delete the property, you need to use the deleter decorator
    # print(bob.age)

    # Call a static method
    print(Human.grunt())
