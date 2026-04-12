** start of main.py **

distance_mi = 3
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True

if not distance_mi:
    print(False)

elif distance_mi <= 1:
    print(not is_raining)
elif 1 < distance_mi <= 6 and has_bike and not is_raining:
    print(True)
elif distance_mi > 6 and has_ride_share_app:
    print(True)
elif distance_mi > 6 and has_car:
    print(True)
else:
    print(False)









** end of main.py **

