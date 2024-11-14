import logging

logging.basicConfig(filename="contacts.log", level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

contacts = {
    "Pedro": {"phone": "555-555-5555", "email": "email@gmail.com"}
}


def add_contact(name, phone, email):
    if name not in contacts:
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact {name} added.")
        logging.info(f"Contact {name} | Phone : {phone} | Email : {email}")
        return contacts[name]
    else:
        logging.info(f"Contact {name} already exists.")
        return None


def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
        logging.info(f"Deleted contact: {name}")
    else:
        logging.warning(f"Attempted to delete non-existent contact: {name}")
        raise ValueError(f"Contact {name} not found.")


def show_contacts():
    if not contacts:
        print("Not contacts available.")
        return None
    else:
        print("\nContacts List:")
        for name, info in contacts.items():
            print(f"{name}: Phone : {info['phone']} | Email : {info['email']}")
            logging.info(f"Displayed contacts: {len(contacts)} contacts")
        return contacts


def edit(name, new_name=None, phone=None, email=None):
    if name in contacts:
        if new_name:
            contacts[name] = contacts.pop(name)
            name = new_name
            logging.info(f"Contact {name} updated.")
            return contacts[name]
        if phone:
            contacts[name]["phone"] = phone
            return contacts[name]
        if email:
            contacts[name]["email"] = email
            return contacts[name]

        print(f"Contact {name} undated")
    else:
        print(f"Contact {name} not found.")
        logging.warning(f"Contact {name} not found")
        return None

