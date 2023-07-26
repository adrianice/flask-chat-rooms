# Flask Chat Rooms

Flask Chat Rooms is a simple chat application made with Flask.

## How to Run the Application

Follow the steps below to run the application on your PC:

1. **Clone the repository:**
```
git clone https://github.com/adrianice/flask-chat-rooms.git
cd flask-chat-rooms
```

2. **Import the database:**
- Before proceeding, ensure you have MySQL installed on your system. I used XAMPP, but you can use any other database server of your choice.
- Import the database from the `flaskchat.sql` file provided in the repository.

3. **Create a Python virtual environment:**
- It's recommended to use a virtual environment to avoid dependency conflicts.
- Execute the following commands to create and activate a virtual environment (using `venv`):
  ```
  python -m venv venv
  source venv/bin/activate      # For Windows, use: venv\Scripts\activate
  ```

4. **Install the dependencies:**
- Install the required dependencies listed in the `requirements.txt` file:
  ```
  pip install -r requirements.txt
  ```

5. **Run the application:**
- To start the Flask development server, execute the following command:
  ```
  python app.py
  ```
- By default, the application will be available at `http://127.0.0.1:5000/`.

6. **Create a new user or use the default user:**
- Upon running the application, you have the option to create a new user.
- Alternatively, you can use the default user with the following credentials:
  - Username: `test`
  - Password: `1234`