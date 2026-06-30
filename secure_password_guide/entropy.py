"""
Module: entropy.py
Description: Calculates mathematical Shannon Entropy based on unique character pools.
Author: Senior Cybersecurity Engineer
"""
import math
from config import LOWERCASE, UPPERCASE, DIGITS, SPECIAL_CHARS

def calculate_shannon_entropy(password: str) -> float:
    """
    Calculates the Shannon Entropy of a password string.
    Formula: E = L * log2(R)
    Where L is password length, and R is the size of the pool of unique characters.
    """
    if not password:
        return 0.0

    length = len(password)
    pool_size = 0

    # Determine character pool size based on types present
    has_lower = any(c in LOWERCASE for c in password)
    has_upper = any(c in UPPERCASE for c in password)
    has_digit = any(c in DIGITS for c in password)
    has_special = any(c in SPECIAL_CHARS for c in password)

    if has_lower:
        pool_size += len(LOWERCASE)   # 26
    if has_upper:
        pool_size += len(UPPERCASE)   # 26
    if has_digit:
        pool_size += len(DIGITS)      # 10
    if has_special:
        pool_size += len(SPECIAL_CHARS) # 29 (standard)

    # Fallback for characters outside standard ASCII configs
    if pool_size == 0:
        pool_size = len(set(password))

    # Calculate bits of entropy
    entropy = length * math.log2(pool_size)
    return round(entropy, 2)