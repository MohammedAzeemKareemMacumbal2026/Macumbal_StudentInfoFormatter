first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
favorite_subject = input("Enter favorite subject: ").strip()

full_name = f"{first_name} {last_name}"

formatted_name = full_name.title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_subject = favorite_subject.title()
char_count = len(formatted_name)

print("\nFormatted Output:")
print(f"Name: {formatted_name}")
print(f"Name Code: {name_code}")
print(f"Section: {formatted_section}")
print(f"Favorite Subject: {formatted_subject}")
print(f"Character Count: {char_count}")