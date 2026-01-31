#!/usr/bin/env python
"""
Example usage of the User Profile Settings module.
"""

from user_profile import UserProfile


def main():
    """Demonstrate user profile settings functionality."""
    
    # Create a new user profile
    print("Creating user profile...")
    profile = UserProfile("alice")
    print(profile)
    print()
    
    # Display current settings
    print("Current settings:")
    for key, value in profile.get_all_settings().items():
        print(f"  {key}: {value}")
    print()
    
    # Update some settings
    print("Updating settings...")
    profile.update_setting('theme', 'dark')
    profile.update_setting('email', 'alice@example.com')
    profile.update_setting('notifications', False)
    print()
    
    # Display updated settings
    print("Updated settings:")
    for key, value in profile.get_all_settings().items():
        print(f"  {key}: {value}")
    print()
    
    # Try to update a non-existent setting
    print("Trying to update non-existent setting...")
    result = profile.update_setting('invalid_setting', 'value')
    print(f"  Result: {result}")
    print()
    
    # Get a specific setting
    print("Getting theme setting:")
    theme = profile.get_setting('theme')
    print(f"  Theme: {theme}")


if __name__ == "__main__":
    main()
