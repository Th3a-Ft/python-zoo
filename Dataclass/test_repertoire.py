from Dataclass.Address import Address
from Dataclass.Contact import Contact
from Repertoire import Repertoire

def test_constructor():
    contact = Contact(46874,"yuretye")
    address = Address("yudy", 28, "ur")
    repertoire = Repertoire("dupont", "john", (1999, 0o4, 27), contact, address)
    assert "dupont" == repertoire.last_name
    assert "john" == repertoire.first_name
    assert (1999, 4, 27) == repertoire.birthday
    assert 46874 == contact.telephone
    assert "yuretye" == contact.mail
    assert "yudy" == address.address
    assert 28 == address.postcode
    assert "ur" == address.city

def test_contact():
    contact = Contact(46874,"yuretye")
    assert 46874 == contact.telephone
    assert "yuretye" == contact.mail

def test_address():
    address = Address("yudy",28,"ur")
    assert "yudy" == address.address
    assert 28 == address.postcode
    assert "ur" == address.city
