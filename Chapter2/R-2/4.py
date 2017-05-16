class Flower:
    """A flower."""

    def __init__(self, name, petals, price):
        """Create a new flower instance.

        name    the name of the flower (e.g. 'Spanish Oyster')
        petals  the number of petals exists (e.g. 50)
        price   price of each flower (measured in euros)
        """
        self._name = str(name)
        self.set_petals(petals)
        self.set_price(price)

    def set_name(self, name):
        self._name = str(name)

    def get_name(self):
        return self._name

    def set_petals(self, petals):
        try:
            self._petals = int(petals)
        except (TypeError, ValueError):
            print('set_petals(): could not parse "%s" to int().' % petals)

    def get_petals(self):
        return self._petals

    def set_price(self, price):
        try:
            self._price = float(price)
        except (TypeError, ValueError):
            print('set_price(): You should parse "%s" to float().' % price)

    def get_price(self):
        return self._price


if __name__ == '__main__':
    rose = Flower('Rose', 60, 1.3)
    
    print('%s contains %d petals costs %.2f euros.' % \
            (rose.get_name(), rose.get_petals(), rose.get_price()))

    """Example with error."""
    rose.set_petals('error')
