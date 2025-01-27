import json
from argon2 import PasswordHasher

# Initialize the password hasher
ph = PasswordHasher()

# Handle the incoming POST request
def handle_signin(data):
    # Load the users from the JSON file
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        return {'status': 'error', 'message': 'No users found'}

    # Check if the email exists in the users
    for user in users:
        if user['email'] == data['email']:
            try:
                # Verify the password using Argon2
                ph.verify(user['password'], data['password'])
                return {'status': 'success', 'message': 'Sign in successful'}
            except Exception:
                return {'status': 'error', 'message': 'Invalid password'}

    return {'status': 'error', 'message': 'Email not found'}

if __name__ == "__main__":
    import sys
    import json

    # Read the data from stdin (which will be sent from the form)
    data = json.loads(sys.stdin.read())

    response = handle_signin(data)

    # Output the response as JSON
    print(f"Content-Type: application/json\n")
    print(json.dumps(response))
