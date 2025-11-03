given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

full_name = given_name + " " + middle_names + " " + family_name
name_length = len(full_name) # find the length of the name.

driving_license_character_limit = 28
print(name_length if name_length <= driving_license_character_limit else "Name is too long.")