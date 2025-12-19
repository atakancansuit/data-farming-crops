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

# 1. Instantiate a rice crop
pass  # YOUR CODE HERE

# 2. Water the rice crop
pass  # YOUR CODE HERE

# 3. Transplant the rice crop
pass  # YOUR CODE HERE

# 4. Print "The rice crop produced ## grains"
pass  # YOUR CODE HERE

# 5. Print "The rice crop is ripe" or "The rice crop is not ripe"
pass  # YOUR CODE HERE
