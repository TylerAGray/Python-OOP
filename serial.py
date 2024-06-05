"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
class SerialGenerator:
    """Class to create a serial number generator.
    
    Attributes:
        start (int): The initial start number.
        next (int): The next number to be generated.
    """

    def __init__(self, start=0):
        """Initialize the generator with a start number."""
        self.start = start
        self.next = start

    def generate(self):
        """Generate the next serial number."""
        current = self.next
        self.next += 1
        return current

    def reset(self):
        """Reset the serial number to the initial start number."""
        self.next = self.start

    def __repr__(self):
        """Provide a nice representation of the instance."""
        return f"<SerialGenerator start={self.start} next={self.next}>"

# Example usage:
if __name__ == "__main__":
    serial = SerialGenerator(start=100)
    print(serial.generate())  # 100
    print(serial.generate())  # 101
    print(serial.generate())  # 102
    serial.reset()
    print(serial.generate())  # 100
    print(serial)  # <SerialGenerator start=100 next=101>

