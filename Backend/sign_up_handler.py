import json
from argon2 import PasswordHasher

# Initialize the password hasher
ph = PasswordHasher()

# Handle the incoming POST request
def handle_signup(data):
    try:
        # Attempt to load the existing users from users.json
        try:
            with open('users.json', 'r') as file:
                users = json.load(file)
            print("Loaded existing users.")
        except FileNotFoundError:
            # If the file doesn't exist, create an empty list
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
        print(f"New user: {new_user}")

        # Save the updated user list back to users.json
        try:
            with open('users.json', 'w') as file:
                json.dump(users, file, indent=4)
            print("User data saved to users.json.")
        except Exception as e:
            print(f"Error saving user data: {e}")
            return {'status': 'error', 'message': f'Error saving user data: {str(e)}'}

        return {'status': 'success', 'message': 'User created successfully'}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'status': 'error', 'message': f"An error occurred: {str(e)}"}

if __name__ == "__main__":
    import sys
    # Read the data from stdin (which will be sent from the form)
    try:
        data = json.loads(sys.stdin.read())
        response = handle_signup(data)
        print(f"Content-Type: application/json\n")
        print(json.dumps(response))
    except Exception as e:
        print(f"Error processing request: {e}")
        print(f"Content-Type: application/json\n")
        print(json.dumps({'status': 'error', 'message': 'Error processing request'}))
