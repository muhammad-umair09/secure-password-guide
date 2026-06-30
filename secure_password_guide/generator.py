"""
Module: generator.py
Description: Generates high-entropy passwords using cryptographically secure random primitives.
Author: Senior Cybersecurity Engineer
"""
import secrets
import logging
from config import LOWERCASE, UPPERCASE, DIGITS, SPECIAL_CHARS

class SecurePasswordGenerator:
    @staticmethod
    def generate(length: int = 16, include_upper: bool = True, include_digits: bool = True, include_special: bool = True) -> str:
        """
        Generates a customized high-entropy password using the secrets library.
        Guarantees that at least one character from each selected category is injected.
        """
        try:
            if length < 4:
                length = 4 # Absolute floor limit to guarantee diversity distribution

            character_pool = LOWERCASE
            mandatory_chars = [secrets.choice(LOWERCASE)]

            if include_upper:
                character_pool += UPPERCASE
                mandatory_chars.append(secrets.choice(UPPERCASE))
            if include_digits:
                character_pool += DIGITS
                mandatory_chars.append(secrets.choice(DIGITS))
            if include_special:
                character_pool += SPECIAL_CHARS
                mandatory_chars.append(secrets.choice(SPECIAL_CHARS))

            # Pad remainder of configuration
            remaining_length = length - len(mandatory_chars)
            generated_pool = [secrets.choice(character_pool) for _ in range(remaining_length)]
            
            # Combine pools and securely shuffle components
            full_password_list = mandatory_chars + generated_pool
            secrets.SystemRandom().shuffle(full_password_list)

            return "".join(full_password_list)
        except Exception as e:
            logging.error(f"Error during cryptographic password creation: {str(e)}")
            return ""