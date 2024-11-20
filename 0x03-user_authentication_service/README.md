Project Overview: 0x03. User Authentication Service  

This project focuses on creating a user authentication system using Python, 
Flask, SQLAlchemy, and bcrypt, providing hands-on learning of authentication mechanisms. 
While the industry standard recommends using pre-built modules or frameworks for such tasks, 
the project requires building the system from scratch to deepen understanding.  

---

Key Features and Learning Objectives:  
1. API Route Declaration: Learn how to define endpoints in a Flask app.  
2. Cookie Handling: Understand how to set and retrieve cookies.  
3. Data Retrieval: Master techniques for extracting form data from HTTP requests.  
4. HTTP Status Codes: Learn how to return various status codes appropriately.  
5. Password Hashing: Use `bcrypt` to hash passwords securely.  
6. User Management: Implement CRUD operations for managing user data with SQLAlchemy.  

---

Project Details:  
- Timeline:  
  - Start Date: Nov 18, 2024, 5:00 AM  
  - End Date: Nov 22, 2024, 5:00 AM  
  - Checker Release: Nov 19, 2024, 5:00 AM  
  - Auto Review: Triggered at the deadline.  

- Technologies:  
  - Python 3.7  
  - Flask  
  - SQLAlchemy (1.3.x)  
  - bcrypt for password hashing  
  - SQLite for database management  

- Setup Requirements:  
  - Files must comply with `pycodestyle` standards.  
  - Include detailed documentation for modules, classes, and functions.  
  - Use type annotations for all functions.  
  - The Flask app should interact only with the `Auth` class, not directly with the database.  

---

Tasks Breakdown:  
1. User Model:  
   - Create a `User` SQLAlchemy model with attributes: `id`, `email`, `hashed_password`, `session_id`, and `reset_token`.  

2. Database Operations:  
   - Add User: Implement a method to save users in the database.  
   - Find User: Search for users using various filters; raise errors for invalid inputs or missing records.  
   - Update User: Modify user attributes; raise `ValueError` for invalid fields.  

3. Password Management:  
   - Use `bcrypt.hashpw` to hash passwords securely.  

4. Authentication Service:  
   - Build a class to handle user registration:  
     - Prevent duplicate email registration.  
     - Store hashed passwords securely.  

5. Flask Application:  
   - Set up a basic Flask app with a root route returning `{"message": "Bienvenue"}` in JSON format.  

---

Key Deliverables:  
- Modularized Python files adhering to the specified standards:  
  - `user.py`: Contains the `User` model.  
  - `db.py`: Manages database interactions (add, find, and update users).  
  - `auth.py`: Implements authentication logic.  
  - `app.py`: Runs the Flask application.  
- A `README.md` file explaining project objectives and usage.  

Outcome:  
By completing this project, you’ll gain a deep understanding of authentication systems, 
secure password handling, and API development, laying a strong foundation for real-world backend development.
