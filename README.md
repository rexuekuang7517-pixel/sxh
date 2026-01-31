# sxh
A demo repository showcasing user profile settings management.

## Features

- User profile creation with customizable settings
- Update individual profile settings
- Retrieve specific or all settings
- Input validation for setting updates

## Usage

```python
from user_profile import UserProfile

# Create a user profile
profile = UserProfile("username")

# Update settings
profile.update_setting('theme', 'dark')
profile.update_setting('email', 'user@example.com')

# Get a specific setting
theme = profile.get_setting('theme')

# Get all settings
all_settings = profile.get_all_settings()
```

## Available Settings

- `email`: User's email address (default: empty string)
- `notifications`: Enable/disable notifications (default: True)
- `theme`: UI theme preference (default: 'light')
- `language`: Language preference (default: 'en')

## Running Tests

```bash
python -m unittest test_user_profile.py
```

## Example

Run the example script to see the module in action:

```bash
python example.py
``` 
