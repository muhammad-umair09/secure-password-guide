"""
Module: analyzer.py
Description: Audits passwords against policies, dictionary pools, and predictive patterns.
Author: Senior Cybersecurity Engineer
"""
import logging
from config import (
    LOWERCASE, UPPERCASE, DIGITS, SPECIAL_CHARS, 
    COMMON_PASSWORDS_DICTIONARY, PREDICTABLE_SEQUENCES, ENTROPY_THRESHOLDS
)
from entropy import calculate_shannon_entropy

# Configure standard error logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - [%(filename)s]: %(message)s')

class PasswordAnalyzer:
    def __init__(self, password: str):
        self.password = password
        self.length = len(password)
        self.findings = []
        self.recommendations = []
        self.risk_rating = "Critical"
        self.strength_tier = "Very Weak"
        self.entropy = 0.0

    def analyze(self) -> dict:
        """Runs the fully consolidated test matrix against the password."""
        try:
            if not self.password or self.length == 0:
                return self._generate_empty_report()

            # 1. Structural Metric & Pattern Auditing
            self.entropy = calculate_shannon_entropy(self.password)
            self._check_dictionary_and_exact_matches()
            self._check_length_constraints()
            self._check_character_diversity()
            self._check_consecutive_and_repeated_patterns()
            self._check_predictable_sequences()

            # 2. Risk Rating & Tier Determination
            self._determine_security_tier()

            return {
                "password_length": self.length,
                "entropy_bits": self.entropy,
                "strength_tier": self.strength_tier,
                "risk_rating": self.risk_rating,
                "findings": self.findings,
                "recommendations": self.recommendations
            }
        except Exception as e:
            logging.error(f"Execution failure during analysis sequence: {str(e)}")
            return self._generate_empty_report()

    def _check_dictionary_and_exact_matches(self):
        normalized = self.password.lower()
        if normalized in COMMON_PASSWORDS_DICTIONARY:
            self.findings.append("CRITICAL_VULNERABILITY: Password is in the global Top 20 compromised list.")
            self.recommendations.append("Immediately discard this password. It is actively actively targeted by threat actors.")

    def _check_length_constraints(self):
        if self.length < 8:
            self.findings.append("FAIL: Character length is below standard threshold (< 8 characters).")
            self.recommendations.append("Increase password length to a minimum of 12-16 characters to prevent brute-forcing.")
        elif self.length < 12:
            self.findings.append("WARNING: Weak length baseline (between 8 and 11 characters).")
            self.recommendations.append("Add characters to breach the 12+ standard for enhanced protection.")

    def _check_character_diversity(self):
        has_lower = any(c in LOWERCASE for c in self.password)
        has_upper = any(c in UPPERCASE for c in self.password)
        has_digit = any(c in DIGITS for c in self.password)
        has_special = any(c in SPECIAL_CHARS for c in self.password)

        missing = []
        if not has_lower: missing.append("Lowercase Letters")
        if not has_upper: missing.append("Uppercase Letters")
        if not has_digit: missing.append("Numeric Characters")
        if not has_special: missing.append("Special Characters")

        if missing:
            self.findings.append(f"FAIL: Missing character pools: {', '.join(missing)}.")
            for item in missing:
                self.recommendations.append(f"Inject at least one random {item.lower()} into your password layout.")

    def _check_consecutive_and_repeated_patterns(self):
        # Repeated characters (e.g., aaa, 1111)
        for i in range(len(self.password) - 2):
            if self.password[i] == self.password[i+1] == self.password[i+2]:
                self.findings.append("WARNING: Detected 3 or more repeating characters sequentially.")
                self.recommendations.append("Break up repetitive character clusters (e.g., 'aaa' to 'a1a').")
                break

    def _check_predictable_sequences(self):
        normalized = self.password.lower()
        for seq in PREDICTABLE_SEQUENCES:
            for i in range(len(seq) - 3):
                sub_seq = seq[i:i+4]
                if sub_seq in normalized:
                    self.findings.append(f"WARNING: Found predictable alphanumeric sequence keyboard layout zone: '{sub_seq}'.")
                    self.recommendations.append("Avoid standard sequential layouts (alphabetic order or sequential rows).")
                    return

    def _determine_security_tier(self):
        # Base classification on Entropy
        if self.entropy < ENTROPY_THRESHOLDS["Very Weak"]:
            self.strength_tier = "Very Weak"
            self.risk_rating = "Critical"
        elif self.entropy < ENTROPY_THRESHOLDS["Weak"]:
            self.strength_tier = "Weak"
            self.risk_rating = "High"
        elif self.entropy < ENTROPY_THRESHOLDS["Moderate"]:
            self.strength_tier = "Moderate"
            self.risk_rating = "Medium"
        elif self.entropy < ENTROPY_THRESHOLDS["Strong"]:
            self.strength_tier = "Strong"
            self.risk_rating = "Low"
        else:
            self.strength_tier = "Very Strong"
            self.risk_rating = "Minimal"

        # Downgrade penalty overrides for high risk discoveries
        if any("CRITICAL_VULNERABILITY" in f or "FAIL" in f for f in self.findings):
            if self.strength_tier in ["Strong", "Very Strong", "Moderate"]:
                self.strength_tier = "Weak"
                self.risk_rating = "High"

    def _generate_empty_report(self) -> dict:
        return {
            "password_length": 0, "entropy_bits": 0.0, "strength_tier": "Very Weak",
            "risk_rating": "Critical", "findings": ["No input provided or calculation error."],
            "recommendations": ["Ensure you supply a valid alphanumeric target string."]
        }