from pydantic import BaseModel, EmailStr, validator, field_validator
from typing import Optional
import re

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    age: int
    phone: Optional[str] = None

    # CUSTOM VALIDATOR 1: Username rules
    @field_validator('username')
    @classmethod
    def username_valid(cls, v):
        """
        Username must be:
        - 3-20 characters
        - Only letters, numbers, underscore
        - No spaces
        """
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters')
        if len(v) > 20:
            raise ValueError('Username must be less than 20 characters')
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError('Username can only contain letters, numbers, and underscore')
        return v.lower()  # Always lowercase

    # CUSTOM VALIDATOR 2: Password strength
    @field_validator('password')
    @classmethod
    def password_strong(cls, v):
        """
        Password must be:
        - At least 8 characters
        - Contains uppercase
        - Contains lowercase
        - Contains number
        """
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain number')
        return v

    # CUSTOM VALIDATOR 3: Age range
    @field_validator('age')
    @classmethod
    def age_valid(cls, v):
        """Age must be 13-120"""
        if v < 13:
            raise ValueError('Must be at least 13 years old')
        if v > 120:
            raise ValueError('Invalid age')
        return v

    # CUSTOM VALIDATOR 4: Phone format
    @field_validator('phone')
    @classmethod
    def phone_valid(cls, v):
        """Phone must be 10 digits"""
        if v is None:
            return v
        # Remove spaces, dashes, parentheses
        cleaned = re.sub(r'[\s\-\(\)]', '', v)
        if not cleaned.isdigit():
            raise ValueError('Phone must contain only digits')
        if len(cleaned) != 10:
            raise ValueError('Phone must be 10 digits')
        return cleaned

# TEST IT:
print("\n=== VALID USER ===")
valid_user = UserCreate(
    username="Alice_123",
    email="alice@example.com",
    password="Secret123",
    age=25,
    phone="(555) 123-4567"
)
print(valid_user)

print("\n=== INVALID USERS ===")

# Test 1: Bad username
try:
    bad = UserCreate(username="ab", email="test@test.com", password="Secret123", age=25)
except Exception as e:
    print(f"❌ Username error: {e}")

# Test 2: Weak password
try:
    bad = UserCreate(username="alice", email="test@test.com", password="weak", age=25)
except Exception as e:
    print(f"❌ Password error: {e}")

# Test 3: Bad age
try:
    bad = UserCreate(username="alice", email="test@test.com", password="Secret123", age=10)
except Exception as e:
    print(f"❌ Age error: {e}")

# Test 4: Bad phone
try:
    bad = UserCreate(username="alice", email="test@test.com", password="Secret123", age=25, phone="123")
except Exception as e:
    print(f"❌ Phone error: {e}")