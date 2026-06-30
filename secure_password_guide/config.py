"""
Module: config.py
Description: Configuration variables, character sets, and dictionary blocks for security auditing.
Author: Senior Cybersecurity Engineer
"""
import string

# Character sets for evaluation and generation
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SPECIAL_CHARS = "!@#$%^&*()-_=+[{]};:',.<>?/|~"

# Industry Standard Strength Thresholds (Entropy in Bits)
ENTROPY_THRESHOLDS = {
    "Very Weak": 28,   # Vulnerable to instant/near-instant cracking
    "Weak": 36,        # Vulnerable to standard dictionary/brute-force
    "Moderate": 60,    # Resistant to basic online attacks, weak against offline GPU arrays
    "Strong": 80,      # Compliant with standard enterprise policies
    "Very Strong": 128 # High-security/Enterprise-grade, brute-force proof with current tech
}

# High-Risk Common Passwords (Top 20 compromised dictionary items)
COMMON_PASSWORDS_DICTIONARY = [
    "123456", "password", "123456789", "qwerty", "12345", 
    "12345678", "football", "qwertyuiop", "admin", "letmein1",
    "welcome", "password123", "iloveyou", "monkey", "charlie",
    "shadow", "dragon", "mustang", "trustnoone", "matrix"
]

# Predictable Sequences for Pattern Recognition
PREDICTABLE_SEQUENCES = [
    "abcdefghijklmnopqrstuvwxyz",
    "01234567890",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]