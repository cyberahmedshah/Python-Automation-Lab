
import json
import os

FILE = "contacts.json"

def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def add_contacts(contact_name, contact_number):
    contacts = load_contacts()
    if contact_name in contacts:
        return "Contact already exists."
    else:
        contacts[contact_name] = contact_number
        with open(FILE, "w") as f:
            json.dump(contacts, f)
        return "Contact added successfully."