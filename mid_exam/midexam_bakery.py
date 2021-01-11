from math import floor
biscuits_per_worker_per_day = int(input())
count_workers = int(input())
factory_2_biscuits_per_30_days = int(input())

biscuits = 0
for day in range(1, 30 + 1):
    if day % 3 == 0:
        biscuits_per_day = biscuits_per_worker_per_day * count_workers * 0.75
    else:
        biscuits_per_day = biscuits_per_worker_per_day * count_workers

    biscuits += floor(biscuits_per_day)

print(f"You have produced {biscuits} biscuits for the past month.")

if biscuits > factory_2_biscuits_per_30_days:
    percent = (biscuits - factory_2_biscuits_per_30_days) / factory_2_biscuits_per_30_days * 100
    print(f"You produce {percent:.2f} percent more biscuits.")
else:
    percent = (factory_2_biscuits_per_30_days - biscuits) / factory_2_biscuits_per_30_days * 100
    print(f"You produce {percent:.2f} percent less biscuits.")
