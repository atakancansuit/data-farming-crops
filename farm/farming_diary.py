"""
Module: farming_diary
This script simulates a farming diary where different crops (corn and rice) are grown, watered,
and checked for ripeness.
"""

from farm.corn import Corn


from farm.corn import Corn  # Corn sınıfını içeri aldık

print("\n📝 Day One: Corn")

# 1. Bir Mısır ekin (Instance oluşturun)
crop = Corn()

# 2. Mısırı sulayın (water metodunu çağırın)
crop.water()

# 3. Durumu yazdırın
print(f"The corn crop produced {crop.grains} grains")

# 4. Olgunlaştı mı kontrol edin
if crop.ripe():
    print("The corn crop is ripe")
else:
    print("The corn crop is not ripe")

print("\n\n📝 Day Two: Rice")
from farm.rice import Rice  # Rice sınıfını içeri aldık
crop = Rice()

# 2. Mısırı sulayın (water metodunu çağırın)
crop.water()

crop.transplant()
# 3. Durumu yazdırın
print(f"The rice crop produced {crop.grains} grains")

# 4. Olgunlaştı mı kontrol edin
if crop.ripe():
    print("The rice crop is ripe")
else:
    print("The rice crop is not ripe")