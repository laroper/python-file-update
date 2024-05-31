# Algorithm for file update in Python
**Description:** An algorithm that updates a file that identifies employees who can access restricted content. The restrictions are based on their IP address. There is an allow list for IP addresses permitted to sign into a restricted subnetwork. There is also a remove list that identifies which employees must be removed from the allow list.

## Open the file that contains the allow list
In the code block below I needed to open a file called `allow_list.txt`. To do this I first assign a string containing this file name to a variable called `import_file`. Then using the `with` statement along with the `open` function containing the parameter keyword of `“r”` which tells the function that the file should be read. While working in the `with` statement the text is stored in a variable called `file`. 

> https://github.com/laroper/python-file-update/blob/41c274fa795714f77699c94f780dfc95d256c916/file_update_algorithm.py#L1-L11

## Read the file contents
To read the content of the file I had to use the `.read()` method to convert the contents of the `“allow_list”` file to a string, then store this string in a variable called `ip_addresses`.  

> https://github.com/laroper/python-file-update/blob/41c274fa795714f77699c94f780dfc95d256c916/file_update_algorithm.py#L13-L15

## Convert the string into a list
In order to remove individual IP addresses from the `allow list`, the IP addresses need to be in a list format. To do this I use the `.split()` method to convert the `ip_addresses` string into a list. Code below displays this.

> https://github.com/laroper/python-file-update/blob/41c274fa795714f77699c94f780dfc95d256c916/file_update_algorithm.py#L17-L19

## Iterate through the remove list
A second list called `remove_list` contains all of the IP addresses that should be removed from the `ip_addresses` list. The code below shows the header of a for loop that will iterate through the `remove_list` and use `element` as the loop variable.

> https://github.com/laroper/python-file-update/blob/41c274fa795714f77699c94f780dfc95d256c916/file_update_algorithm.py#L21-L26

## Remove IP addresses that are on the remove list
The code below will remove all the IP addresses from the allow list that are also on the remove list. This is done by first creating a conditional statement that evaluates if the loop variable `element` is part of the `ip_addresses` list. Then, within that conditional, apply the `.remove()` method to the `ip_addresses` list and remove the IP addresses identified in the loop variable `element`. 

> https://github.com/laroper/python-file-update/blob/41c274fa795714f77699c94f780dfc95d256c916/file_update_algorithm.py#L28-L35

## Update the file with the revised list of IP addresses 
Next, updating the file with this revised list. To do this, I first convert the `ip_addresses` list back into a string using the `.join()` method. Apply `.join()` to the string `"\n"` in order to separate the elements in the file by placing them on a new line. Using another with statement with `“w”` argument that tells the `open()` function that you are writing to the file. Then utilizing the `.write()` method to write over the file assigned to the `import_file` variable.

> https://github.com/laroper/python-file-update/blob/41c274fa795714f77699c94f780dfc95d256c916/file_update_algorithm.py#L36-L46

## Summary of Algorithm

> [!IMPORTANT]
> I created an algorithm that uses Python code to check whether a file of authorized IP addresses stored in a file called “allowed_list.txt” contained any unautorized IP addresses. These unauthorized IP addresses were stored in a `remove_list` variable and checked against the allowed list. If found in the allowed list those unauthorized IP addresses were removed from the file containing the allowed IP addresses.
> - This was done by opening the file,
> - converting it to a string to be read,
> - then converting this string to a list stored in a variable called `ip_addresses`.
> - The program iterated through the `ip_addresses` list, checking if the element of `remove_list` was a part of the list.
> - If it was, it applied the `.remove()` method to remove the element from the ip_addresses list.
> - Once completed the `.join()` method was used to convert the list back to a string so it could write over the content of the `allow_list.txt` file.


