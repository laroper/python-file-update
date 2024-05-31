# Assign `import_file` to the name of the file

import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# First line of 'with' statement

with open(import_file, "r") as file:

    # Use '.read()' function to read the imported file and store it in a variable named 'ip_addresses'

    ip_addresses = file.read()

    # Use 'split()' function to convert 'ip_addresses' from a string to a list

    ip_addresses = ip_addresses.split()

# Build interative statement
# NAme loop variable 'element'
# Loop through 'ip_addresses'

for element in ip_addresses:

    # Build conditional statement 
    # If current element is in 'remove_list',

        if element in remove_list:
              
              # then current element should be removed from 'ip_address'

              ip_addresses.remove(element)

# Convert 'ip_addresses' back to string so that so that it can written into the text file

ip_addresses = "\n".join(ip_addresses)

#Build 'with' statement to rewrite the original file

with open(import_file, "w") as file:

    #Rewrite the file, replacing its content with 'ip_addresses'

    file.write(ip_addresses)


