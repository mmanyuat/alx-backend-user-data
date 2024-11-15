#!/usr/bin/env python3
""""Auth module for managing api authenication"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Template for API authenication management"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """return if path is none"""
        if path is None:
            return True

        if not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.
        Currently returns None as a placeholder.
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request.
        Currently returns None as a placeholder.
        """
        return None
