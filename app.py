import csv
from contact import PhoneBook, Contact

if __name__ == "__main__":
    with open("phonebook_raw.csv", mode='r', encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        header = contacts_list[0]

    ph = PhoneBook()
    for data in contacts_list[1:]:
        contact = Contact(*data[:7])
        ph.add(contact)

    with open("phonebook.csv", mode="w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerow(header)
        datawriter.writerows(ph.get_contacts_list())
