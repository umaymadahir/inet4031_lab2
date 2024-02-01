import sys

print("Printing out User Data:")

for line in sys.stdin:
    line = line.strip()

    if line.startswith('#'):
        continue

    userData = line.split(':')
    username, password, userid, groupid = userData
    
    print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

print("\nEnd of User Data")

