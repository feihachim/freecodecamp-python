"""
For this lab, you will use conditional statements to determine whether commuting is possible based on the weather,
the distance to travel, and the availability of a vehicle.
"""

distance_mi = 0
is_raining = False
has_bike = False
has_car = False
has_ride_share_app = False

# for numbers, 0 is considered a falsy value
if distance_mi == 0:
    print(False)
elif distance_mi > 0 and distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi > 1 and distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
else:
    print(False)
