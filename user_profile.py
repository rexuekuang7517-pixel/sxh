"""
User Profile Settings Module

A simple module for managing user profile settings.
"""


class UserProfile:
    """Represents a user profile with customizable settings."""
    
    # Default settings for new user profiles
    _DEFAULT_SETTINGS = {
        'email': '',
        'notifications': True,
        'theme': 'light',
        'language': 'en'
    }
    
    # Expected types for each setting
    _EXPECTED_TYPES = {
        'email': str,
        'notifications': bool,
        'theme': str,
        'language': str
    }
    
    def __init__(self, username):
        """
        Initialize a user profile.
        
        Args:
            username (str): The username for this profile
            
        Raises:
            ValueError: If username is empty or not a string
        """
        if not isinstance(username, str) or not username.strip():
            raise ValueError("Username must be a non-empty string")
        self.username = username
        self.settings = self._DEFAULT_SETTINGS.copy()
    
    def update_setting(self, key, value):
        """
        Update a specific setting.
        
        Args:
            key (str): The setting key to update
            value: The new value for the setting
            
        Returns:
            bool: True if update was successful, False otherwise
            
        Raises:
            TypeError: If value type doesn't match expected type for the setting
        """
        if key not in self.settings:
            return False
        
        # Validate value type based on setting key
        expected_type = self._EXPECTED_TYPES.get(key)
        if expected_type and not isinstance(value, expected_type):
            raise TypeError(f"Setting '{key}' expects {expected_type.__name__}, got {type(value).__name__}")
        
        self.settings[key] = value
        return True
    
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
            dict: A copy of the settings dictionary. Modifications to the
                  returned dictionary will not affect the profile's internal state.
        """
        return self.settings.copy()
    
    def __str__(self):
        """
        String representation of the user profile.
        
        Note: This representation may include sensitive information
        such as email addresses. Use with caution in production environments.
        """
        return f"UserProfile(username='{self.username}', settings={self.settings})"
