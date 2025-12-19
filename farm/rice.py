from farm.crop import Crop #Crop fonksiyonunu import edip burda çalışmasını sağladık
#sulayınca ve transplant edince artacak şekilde ayarladık
class Rice(Crop):
    def water(self):
        self.grains += 5
    
    def transplant(self):
        self.grains += 10