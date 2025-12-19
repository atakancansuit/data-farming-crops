
class Corn:
    def __init__(self):
        # Mısır doğduğu an (init), taneleri 0 olsun.
        self.grains = 0

    def water(self):
        # Sulandığında 10 tane ekle
        self.grains += 10

    def ripe(self):
        # Eğer taneler 15 veya daha fazlaysa True, değilse False döner
        return self.grains >= 15
