from farm.crop import Crop # ana klasmanı import ettik
#sulayınca artacak şekilde ayarladık
class Corn(Crop):  # Parantez içine Baba sınıfın adını yazdık
    def water(self):
        self.grains += 10
