def make payment(self, amount):
    """Process customer payment that reduces balance."""
    if ammount < 0:
        raise ValueError('amount should not be negative.')

    self.balance −= amount
