import datetime
# import contact
from dataclasses import dataclass

from Dataclass.Address import Address
from Dataclass.Contact import Contact


@dataclass
class Repertoire:
    last_name:str
    first_name:str
    birthday:datetime.date
    contact:Contact
    address:Address

contact = Contact(46874,"yuretye")
address = Address("yudy", 28, "ur")
repertoire = Repertoire("dupont", "john", (1999, 0o4, 27), contact, address)

print(repertoire)



