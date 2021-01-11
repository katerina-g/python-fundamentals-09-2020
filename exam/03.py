heroes = {}

line = input()
while not line == "End":
    line = line.split()
    command = line[0]
    if command == "Enroll":
        hero_name = line[1]
        if hero_name not in heroes:
            heroes[hero_name] = {'spell_name': []}
        else:
            print(f"{hero_name} is already enrolled.")
    elif command == "Learn":
        hero_name = line[1]
        spell_name = line[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name not in heroes[hero_name]['spell_name']:
                heroes[hero_name]['spell_name'].append(spell_name)
            else:
                print(f"{hero_name} has already learnt {spell_name}.")
    elif command == "Unlearn":
        hero_name = line[1]
        spell_name = line[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name not in heroes[hero_name]['spell_name']:
                print(f"{hero_name} doesn't know {spell_name}.")
            else:
                heroes[hero_name]['spell_name'].remove(spell_name)
    line = input()
print("Heroes:")
if len(heroes) > 0:
    sorted_heroes = sorted(heroes.items(), key=lambda x: (-len(x[1]['spell_name']), x[0]))
    for name, value in sorted_heroes:
        print(f"== {name}: {', '.join(map(str,value['spell_name']))}")