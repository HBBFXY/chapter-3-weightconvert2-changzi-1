initial_weight_earth=60
moon_weight_ratio=0.165
print("年份\t地球重量(kg)\t月球重量(kg)")
for year in range(1,11):
  weight_earth=initial_weight_earth+year*0.5
  weight_moon=weight_earth*moon_weight_ratio
  print(f"{year}\t{weight_earth:.2f}\t\t{weight_moon:.2f}")
