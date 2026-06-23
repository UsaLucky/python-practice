# def find_contact(contacts, name):
#     for contact in contacts:
#         if contact['name'] == name:
#             return contact['phone']
#     return 'Not found'

def find_contact(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            return contact['phone']
    return 'Not found'

# 1. Create a list of contact dictionaries
my_contacts = [
    {"name": "Victor", "phone": "080-111-2222"},
    {"name": "Joel", "phone": "081-333-4444"},
    {"name": "Selima", "phone": "090-555-6666"}
]

# 2. Call the function and print the result
search_name = str(input("Enter the contact name: "))
phone_number = find_contact(my_contacts, search_name)

print(f"Searching for {search_name}...")
print(f"Phone Number: {phone_number}")



