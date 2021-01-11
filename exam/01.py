skill = input()
new_skill = ""
line = input()
while not line == "For Azeroth":
    line = line.split()
    if "GladiatorStance" in line:
        skill = skill.upper()
        print(skill)
    elif "DefensiveStance" in line:
        skill = skill.lower()
        print(skill)
    elif "Dispel" in line:
        index = int(line[1])
        letter = line[2]
        if index < len(skill):
            new_skill = skill[:index] + letter + skill[index + 1:]
            print("Success!")
        else:
            print("Dispel too weak.")
        skill = new_skill
    elif ("Target" and "Change") in line:
        substring = line[2]
        second_substring = line[3]
        skill = skill.replace(substring, second_substring)
        print(skill)
    elif ("Target" and "Remove") in line:
        substring = line[2]
        skill = skill.replace(substring, "")
        print(skill)
    else:
        print("Command doesn't exist!")
    line = input()
