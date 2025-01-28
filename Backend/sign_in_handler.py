import json
from argon2 import PasswordHasher
import os

# Initialize the password hasher
ph = PasswordHasher()

def handle_signin(data):
    """
    Handles the sign-in process.
    - Verifies the username and password using Argon2.
    """
    try:
        # Check if users.json exists, or create a new file if it doesn't
        if not os.path.exists('users.json'):
            return {'status': 'error', 'message': 'No users found, please sign up first.'}

        # Load users from users.json
        with open('users.json', 'r') as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                return {'status': 'error', 'message': 'Users data is corrupted.'}

        # Extract the login details
        username = data['username']
        password = data['password']

        # Find the user by username
        user = next((user for user in users if user['username'] == username), None)

        # If the user is not found, return an error
        if user is None:
            return {'status': 'error', 'message': 'Invalid username or password'}

        # Verify the password using Argon2
        try:
            ph.verify(user['password'], password)  # This will raise an exception if passwords don't match
            return {'status': 'success', 'message': 'Login successful'}
        except Exception:
            return {'status': 'error', 'message': 'Invalid username or password'}

    except Exception as e:
        return {'status': 'error', 'message': str(e)}

# For testing purposes, to simulate a sign-in request
if __name__ == "__main__":
    data = {
        'username': 'testuser',
        'password': 'password123'
    }
    response = handle_signin(data)
    print(response)
