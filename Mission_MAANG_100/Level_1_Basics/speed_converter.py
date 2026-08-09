car_speed_kmh = float(input("Enter the speed of the card in km/h: "))

car_speed_mps = car_speed_kmh * 1000 / 3600

print(f"The speed of the car in m/s is: {car_speed_mps:.2f}")