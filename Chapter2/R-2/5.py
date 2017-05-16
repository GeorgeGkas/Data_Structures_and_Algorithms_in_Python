def make payment(self, amount):
    """Process customer payment that reduces balance."""
    if not isinstance(amount, (int, float)):
        raise TypeError('amount is not a number')

    self.balance −= amount
