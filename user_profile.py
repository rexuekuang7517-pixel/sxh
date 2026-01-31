"""
User Profile Settings Module

A simple module for managing user profile settings.
"""


class UserProfile:
    """Represents a user profile with customizable settings."""
    
    def __init__(self, username):
        """
        Initialize a user profile.
        
        Args:
            username (str): The username for this profile
        """
        self.username = username
        self.settings = {
            'email': '',
            'notifications': True,
            'theme': 'light',
            'language': 'en'
        }
    
    def update_setting(self, key, value):
        """
        Update a specific setting.
        
        Args:
            key (str): The setting key to update
            value: The new value for the setting
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        if key in self.settings:
            self.settings[key] = value
            return True
        return False
    
    def get_setting(self, key):
        """
        Get a specific setting value.
        
        Args:
            key (str): The setting key to retrieve
            
        Returns:
            The setting value, or None if key doesn't exist
        """
        return self.settings.get(key)
    
    def get_all_settings(self):
        """
        Get all settings.
        
        Returns:
            dict: A dictionary of all settings
        """
        return self.settings.copy()
    
    def __str__(self):
        """String representation of the user profile."""
        return f"UserProfile(username='{self.username}', settings={self.settings})"
