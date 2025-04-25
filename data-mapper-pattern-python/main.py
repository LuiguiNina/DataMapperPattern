from domain.customer import Customer
from data_mapper.customer_mapper import CustomerMapper

mapper = CustomerMapper()

# Create and persist a customer
new_customer = Customer(name="Alice", email="alice@example.com")
mapper.insert(new_customer)
print("Inserted:", new_customer)

# Retrieve it later
fetched = mapper.find_by_id(new_customer.id)
print("Fetched:", fetched)