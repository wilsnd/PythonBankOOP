class Money:
    """Class to demonstrate magic methods"""

    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        """String representation"""
        return f"{self.currency} {self.amount:.2f}"

    def __repr__(self):
        """Official representation"""
        return f"Money({self.amount}, '{self.currency}')"

    def __add__(self, other):
        """Addition operator"""
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency)
        raise TypeError(f"Cannot add Money and {type(other)}")

    def __sub__(self, other):
        """Subtraction operator"""
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount - other, self.currency)
        raise TypeError(f"Cannot subtract {type(other)} from Money")

    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Money):
            return self.currency == other.currency and self.amount == other.amount
        return False