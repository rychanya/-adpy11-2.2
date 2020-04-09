import re


class Contact:

    @staticmethod
    def normalize_full_name(lastname: str, firstname: str, surname: str):
        full_name = ' '.join((lastname, firstname, surname))
        result = re.findall(r'\w+', full_name)
        if len(result) == 1:
            return (result[0], '', '')
        elif len(result) == 2:
            return (result[0], result[1], '')
        elif len(result) == 3:
            return (result[0], result[1], result[2])
        else:
            raise ValueError

    @staticmethod
    def normalize_phone_number(number: str):
        res = re.sub(
            r'^\s*(8|\+7)\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})',
            r'+7(\2)\3-\4-\5',
            number
        )
        res = re.sub(
            r'\s*\(?(доб\.)\s(\d+)\)?',
            r' доб.\2',
            res
        )
        return res

    def __init__(self, lastname, firstname, surname, organization, position, phone, email):
        self.lastname, self.firstname, self.surname = self.normalize_full_name(lastname, firstname, surname)
        self.organization = organization
        self.position = position
        self.phone = self.normalize_phone_number(phone)
        self.email = email

    def __eq__(self, other):
        if not isinstance(other, Contact):
            raise NotImplementedError
        if (self.lastname == other.lastname and self.firstname == other.firstname):
            return True
        elif self.phone and self.phone == other.phone:
            return True
        elif self.email and self.email == other.email:
            return True
        return False

    def update(self, data):
        self.lastname = self.lastname or data.lastname
        self.firstname = self.firstname or data.firstname
        self.surname = self.surname or data.surname
        self.organization = self.organization or data.organization
        self.position = self.position or data.position
        self.phone = self.phone or data.phone
        self.email = self.email or data.email

    def to_list(self):
        return [
            self.lastname,
            self.firstname,
            self.surname,
            self.organization,
            self.position,
            self.phone,
            self.email
        ]


class PhoneBook:

    def __init__(self):
        self._contacts = []

    def add(self, contact_to_add):
        for contact in self._contacts:
            if contact == contact_to_add:
                contact.update(contact_to_add)
                return
        self._contacts.append(contact_to_add)

    def get_contacts_list(self):
        return [contact.to_list() for contact in self._contacts]
