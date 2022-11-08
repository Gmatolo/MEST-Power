from abc import ABC, abstractmethod


# create a contact details class
class ContactDetails:
    first_name = ""
    second_name = ""
    email_address = ""
    phone_number = ""


# create a contactBookAddress to work as a blueprint
class ContactBookAbstract(ABC):
    @abstractmethod
    def create_contact(self, contact: ContactDetails):
        pass


class ContactManager(ContactDetails, ContactBookAbstract):
    def create_contact(self):
        self.first_name = "Gerald"
        self.second_name = "Gerald"
        self.phone_number = "+254719749633"
        self.email_address = "gerald.matolo@meltwater.org"
        contact_details = {
            "Name: ": f"{self.first_name} {self.second_name}",
            "Email: ": self.email_address,
            "Phone Number: ": self.phone_number,
        }
        # print(f"Your contact details are as: {contact_details.items()}")
        for k, v in contact_details.items():
            print(k, v)


