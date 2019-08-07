#!/usr/bin/env python
import random

# number of user data to generate
users = int(input())
for user in range(users):
    participant_id = random.randint(1000097, 1269551)
    weeks = 8

    for week in range(weeks):
        mon = random.randint(1000, 14000)
        tues = random.randint(1000, 14000)
        wed = random.randint(1000, 14000)
        thurs = random.randint(1000, 14000)
        fri = random.randint(1000, 14000)
        sat = random.randint(1000, 14000)
        sun = random.randint(1000, 14000)
        print(f'("{participant_id}", {week + 1}, {mon}, {tues}, {wed}, {thurs}, {fri}, {sat}, {sun}),')
