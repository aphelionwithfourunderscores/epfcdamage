def damage_calc(raw_damage, vt, wp, pierce, armor, is_headshot):
  if armor == "Frontline":
    if pierce == 'H':
      reduction = 0.2
    elif pierce == 'A':
      reduction = 0.35
    elif pierce == 'L':
      reduction = 0.6
  elif armor == "Scout":
    if pierce == 'H':
      reduction = 0.1
    elif pierce == 'A':
      reduction = 0.2
    elif pierce == 'L':
      reduction = 0.5
  final_red = reduction * (1.0 - (0.06 * wp))
  if is_headshot:
    damage = raw_damage * head * (1.0 + 0.04 * vt) * (1.0 - final_red)
  else:
    damage = raw_damage * (1.0 + 0.04 * vt) * (1.0 - final_red)
  return damage

UP9 = [25.0, 'A', 'L', 'L']
K45 = [30.0, 'A', 'A', 'L']
S97 = [25.0, 'A', 'A', 'L']
MCS = [21.0*8.0, 'A', 'L', 'L']
CBRC = [37.0, 'H', 'A', 'A']
F57 = [29.0, 'H', 'A', 'A']

gun_choice = int(input("Select gun by number:\n1) UP9\n2) K45\n3) S97\n 4) 480 MCS\n 5) CBR-C\n 6) F57\n"))

match gun_choice:
  case 1:
    chosen_gun = UP9
  case 2:
    is_chambered = True if input("Rechambered to 9mm? Y/N ").lower() == 'y' else False
    chosen_gun = K45
    if is_chambered:
      chosen_gun[0] -= 5.0
  case 3:
    chosen_gun = S97
  case 4:
    chosen_gun = MCS
    is_slugs = True if (input("Slugs? Y/N ").lower() == "y") else False
    if is_slugs:
      chosen_gun = [96.0, 'H', 'A', 'A']
  case 5:
    chosen_gun = CBRC
    is_chambered = True if input("Rechambered to 5.56? Y/N ").lower() == 'y' else False
    if is_chambered:
      chosen_gun[0] -= 8.0
    is_ext = True if (input("Extended Barrel? ").lower() == "y") else False
    if is_ext:
      chosen_gun[0] *= 1.1
  case 6:
    chosen_gun = F57
  case _:
    print("buddy you gotta choose a gun")
    exit()

head = 3.0 if input("Executioner? Y/N ").lower() == "y" else 2.5
vt = int(input("Enter how many Vital Targets perks you have: "))
wp = int(input("Enter how many Weak Points perks you have: "))

print("Standard Swat units have 75 HP and either Scout or Frontline armor.")

print("\nFrontline Armor:\n")
print("Close Range (0-15 studs)")
close_damage_head = round(damage_calc(chosen_gun[0], vt, wp, chosen_gun[1], "Frontline", True),2)
close_damage_body = round(damage_calc(chosen_gun[0], vt, wp, chosen_gun[1], "Frontline", False),2)
print("Headshot damage: " + str(close_damage_head))
print("Bodyshot damage: " + str(close_damage_body))
print("\nMedium Range (15-50 studs)")
med_damage_head = round(damage_calc(chosen_gun[0], vt, wp, chosen_gun[2], "Frontline", True),2)
med_damage_body = round(damage_calc(chosen_gun[0], vt, wp, chosen_gun[2], "Frontline", False),2)
print("Headshot damage: " + str(med_damage_head))
print("Bodyshot damage: " + str(med_damage_body))
print("\nLong Range (50+ studs)")
long_damage_head = round(damage_calc(chosen_gun[0], vt, wp, chosen_gun[3], "Frontline", True),2)
long_damage_body = round(damage_calc(chosen_gun[0], vt, wp, chosen_gun[3], "Frontline", False),2)
print("Headshot damage: " + str(long_damage_head))
print("Bodyshot damage: " + str(long_damage_body))

print("\nScout Armor:\n")
print("Close Range (0-15 studs)")
close_damage_head = round(damage_calc(chosen_gun[0], vt, wp, chosen_gun[1], "Scout", True),2)
close_damage_body = round(damage_calc(chosen_gun[0], vt, wp, chosen_gun[1], "Scout", False),2)
print("Headshot damage: " + str(close_damage_head))
print("Bodyshot damage: " + str(close_damage_body))
print("\nMedium Range (15-50 studs)")
med_damage_head = round(damage_calc(chosen_gun[0], vt, wp, chosen_gun[2], "Frontline", True),2)
med_damage_body = round(damage_calc(chosen_gun[0], vt, wp, chosen_gun[2], "Frontline", False),2)
print("Headshot damage: " + str(med_damage_head))
print("Bodyshot damage: " + str(med_damage_body))
print("\nLong Range (50+ studs)")
long_damage_head = round(damage_calc(chosen_gun[0], vt, wp, chosen_gun[3], "Scout", True),2)
long_damage_body = round(damage_calc(chosen_gun[0], vt, wp, chosen_gun[3], "Scout", False),2)
print("Headshot damage: " + str(long_damage_head))
print("Bodyshot damage: " + str(long_damage_body))
