class MyClass:
    """This is a sample class."""
    def __init__(self, name):
        """Initialize MyClass with a name.
        Args:
            name (str): The name of the MyClass instance.
        """
        self.name = name

    def say_hello(self):
        """Print a greeting message.
        Returns:
            str: A greeting message.
        """
        return f"Hello, {self.name}!"

    def calculate_xor(self, num1, num2):
        """Calculate the sum of two numbers.
        Args:
            num1 (int): The first number.
            num2 (int): The second number.
        Returns:
            int: The sum of num1 and num2.
        """
        return num1 ^ num2


if __name__ == '__main__':
    help(MyClass.calculate_xor)
