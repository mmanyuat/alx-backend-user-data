#!/usr/bin/env python3
"""
Importing from the auth class
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    """A class that inherits from auth"""
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """Extracts the header for authorization"""
        if authorization_header is None or not isinstance(
            authorization_header, str
        ):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Decodes the header"""
        if base64_authorization_header is None or not isinstance(
            base64_authorization_header, str
        ):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode("utf-8")
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """extract the credentials of the user"""
        if (
            decoded_base64_authorization_header is None
            or not isinstance(decoded_base64_authorization_header, str)
        ):
            return None, None

        if ":" not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):
        """Gets the user object credentials"""
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None

        users = User.search({"email": user_email})
        if not users or len(users) == 0:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Retrieve the User instance associated with the request.

        Args:
            request: The HTTP request object.

        Returns:
            User instance or None if authentication fails.
        """
        authorization_header = self.authorization_header(request)
        if authorization_header is None:
            return None

        base64_header = self.extract_base64_authorization_header(
            authorization_header
        )
        if base64_header is None:
            return None

        decoded_header = self.decode_base64_authorization_header(base64_header)
        if decoded_header is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        if user_email is None or user_pwd is None:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
