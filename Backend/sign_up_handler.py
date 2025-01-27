import json
from argon2 import PasswordHasher

# Initialize the password hasher
ph = PasswordHasher()

# Handle the incoming POST request
def handle_signup(data):
    # Load existing users (if any)
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
        print("users.json not found, creating new list.")

    # Get the new user's details
    username = data['username']
    email = data['email']
    password = data['password']

    # Hash the password
    hashed_password = ph.hash(password)

    # Create a new user object
    new_user = {'username': username, 'email': email, 'password': hashed_password}

    # Add the new user to the list
    users.append(new_user)

    # Save users back to the JSON file
    try:
        with open('users.json', 'w') as file:
            json.dump(users, file)
        print("User data saved to users.json.")
    except Exception as e:
        return {'status': 'error', 'message': f'Error saving user data: {str(e)}'}

    return {'status': 'success', 'message': 'User created successfully'}

if __name__ == "__main__":
    import sys
    import json

    # Read the data from stdin (which will be sent from the form)
    data = json.loads(sys.stdin.read())

    response = handle_signup(data)

    # Output the response as JSON
    print(f"Content-Type: application/json\n")
    print(json.dumps(response))
