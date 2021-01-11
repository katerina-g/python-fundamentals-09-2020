count_rooms = int(input())

free_chairs = 0
enough_chairs = True

for i in range(1, count_rooms + 1):
    rooms = input().split()
    chairs_count = len(rooms[0])
    num_of_people = int(rooms[1])

    if chairs_count >= num_of_people:
        free_chairs += chairs_count - num_of_people
    else:
        enough_chairs = False
        print(f"{num_of_people - chairs_count} more chairs needed in room {i}")

if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")

