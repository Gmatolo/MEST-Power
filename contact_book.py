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
