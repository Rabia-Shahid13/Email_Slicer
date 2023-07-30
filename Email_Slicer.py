user_input = input("Please enter your email: ")

(username, domain) = user_input.split("@")
(domain, extension) = domain.split(".")

print("Username: ", username)
print("Domain: ", domain)
print("Extension: ", extension)