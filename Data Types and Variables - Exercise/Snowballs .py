num_of_snowballs = int(input())
max_value = 0
snow_max = 0
time_max = 0
quality_max = 0
for ball in range(num_of_snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int(snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > max_value:
        max_value = snowball_value
        snow_max = snowball_snow
        time_max = snowball_time
        quality_max = snowball_quality
print(f"{snow_max} : {time_max} = {max_value} ({quality_max})")

