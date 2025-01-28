import json
from argon2 import PasswordHasher
import os

# Initialize the password hasher
ph = PasswordHasher()

def handle_signup(data):
    """
    Handles the sign-up process.
    - Hashes the user's password using Argon2.
    - Saves the username, email, and hashed password in a JSON file.
    """
    try:
        # Check if users.json exists, or create a new file if it doesn't
        if os.path.exists('users.json'):
            print("Found users.json. Loading existing users.")
            with open('users.json', 'r') as file:
                users = json.load(file)  # Load existing users
        else:
            print("No users.json found. Creating a new user list.")
            users = []

        # Extract the user's details from the input data
        username = data['username']
        email = data['email']
        password = data['password']

        # Check for duplicate username or email
        duplicate_username = any(user['username'] == username for user in users)
        duplicate_email = any(user['email'] == email for user in users)

        if duplicate_username:
            print(f"Username '{username}' is already taken.")
            return {'status': 'error', 'message': 'The username is already taken. Please choose a different username.'}
        if duplicate_email:
            print(f"Email '{email}' is already registered.")
            return {'status': 'error', 'message': 'The email is already registered. Please use a different email address.'}

        # Hash the user's password
        hashed_password = ph.hash(password)

        # Create a new user object
        new_user = {'username': username, 'email': email, 'password': hashed_password}

        # Add the new user to the list
        users.append(new_user)

        # Save the updated list of users back into users.json
        with open('users.json', 'w') as file:
            json.dump(users, file, indent=4)

        print(f"New user '{username}' created successfully.")
        return {'status': 'success', 'message': 'User created successfully'}

    except Exception as e:
        print(f"Error during sign-up: {str(e)}")
        return {'status': 'error', 'message': str(e)}

# For testing purposes, to simulate a sign-up request
if __name__ == "__main__":
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    }
    response = handle_signup(data)
    print(response)