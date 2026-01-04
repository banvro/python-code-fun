from faker import Faker
fake = Faker("en-in")

# 👤 Person
# print("Name:", fake.name())
print("First Name:", fake.first_name())
print("Last Name:", fake.last_name())
print("Date of Birth:", fake.date_of_birth())

# 📞 Contact
print("Email:", fake.email())
print("Phone:", fake.phone_number())

# 🏠 Address
print("Address:", fake.address())
print("City:", fake.city())
print("State:", fake.state())
print("Country:", fake.country())
print("Pincode:", fake.postcode())

# 🌐 Internet
print("Username:", fake.user_name())
print("Password:", fake.password())
print("Website:", fake.url())
print("IP Address:", fake.ipv4())

# 🏢 Work
print("Company:", fake.company())
print("Job:", fake.job())

# 🎨 Files & Colors
print("Color Name:", fake.color_name())
print("Hex Color:", fake.hex_color())
print("File Name:", fake.file_name())
print("File Extension:", fake.file_extension())
print("Image URL:", fake.image_url())

# 🔢 Misc
print("Boolean:", fake.boolean())
print("UUID:", fake.uuid4())
