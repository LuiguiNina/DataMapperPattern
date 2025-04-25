from domain.customer import Customer

def test_customer_repr():
    customer = Customer(id=1, name="Bob", email="bob@example.com")
    assert repr(customer) == "<Customer id=1, name='Bob', email='bob@example.com'>"
