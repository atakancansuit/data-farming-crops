
class Rice:
    def __init__(self):
        # Pirinç doğduğu an (init), taneleri 0 olsun.
        self.grains = 0

    def water(self):
        # Sulandığında 5 tane ekle
        self.grains += 5

    def ripe(self):
        # Eğer taneler 15 veya daha fazlaysa True, değilse False döner
        return self.grains >= 15
    def transplant(self):
        # Pirince özel metod: Fideleme yapınca 10 artar
        self.grains += 10
