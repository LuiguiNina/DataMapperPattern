from domain.customer import Customer
from data_mapper.customer_mapper import CustomerMapper

def test_insert_and_find():
    mapper = CustomerMapper()
    customer = Customer(name="Jane", email="jane@example.com")
    mapper.insert(customer)

    found = mapper.find_by_id(customer.id)
    assert found.name == "Jane"
    assert found.email == "jane@example.com"