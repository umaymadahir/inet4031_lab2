filename = "fileprocessor.input"

try:
	with open(filename, 'r') as file:
		lines = file.readlines()
	print("Printing out User Data:\n")

	for line in lines:
		if line.startswith('#'):
			continue

		userData = line.strip().split(':')
		username, password, userid, groupid = userData

		print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

	print("\nEnd of User Data")


except FileNotFoundError:

	print(f"Error: {filename} not found.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
