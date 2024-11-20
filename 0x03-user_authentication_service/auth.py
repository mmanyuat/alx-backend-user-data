#!/usr/bin/env python3
"""Authentication Module"""
from db import DB
from user import User
from typing import Type
import bcrypt  # Fix the import issue


class Auth:
    """Authentication class to interact with the authentication database."""

    def __init__(self):
        """A constructor"""
        self.db = DB()

    @staticmethod
    def _hash_password(password: str) -> bytes:
        """Hashes a password using bcrypt"""
        if not isinstance(password, str):
            raise TypeError('Password must be a string')
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user with the given email and password.
        Args:
            email (str): The user's email.
            password (str): The user's password.
        Returns:
            User: The newly created User object.
        Raises:
            ValueError: If a user with the given email already exists.
        """
        try:
            existing_user = self.db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except Exception:  # Ideally, catch NoResultFound specifically
            pass

        hashed_password = self._hash_password(password)
        new_user = self.db.add_user(
                email=email,
                hashed_password=hashed_password.decode('utf-8')
                )

        return new_user
