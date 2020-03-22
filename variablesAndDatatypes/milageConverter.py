print("How many Kilometers Did You Run Today")

kilometers = float(input())
km_to_miles = kilometers / 1.60934

conversion = round(km_to_miles , 2)

print(f"Okay, you ran {conversion} miles")