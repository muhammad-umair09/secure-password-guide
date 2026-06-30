# Secure Password Creation Guide & Audit Suite

An enterprise-grade, modular Identity & Access Management (IAM) educational tool and assessment engine written in Python. This framework calculates Shannon Entropy, evaluates character diversity, flags keyboard patterns, and generates cryptographically secure, high-entropy password keys.



## Project Overview

Weak credentials remain a primary vector for initial access in corporate cyber attacks. This project bridges the gap between end-user behavior and rigorous Identity Management standards. It acts as both a **vulnerability testing tool** and an **educational asset** designed for SOC analysts, security awareness trainers, and Blue Team members.

### Core Objectives
* **Quantify Key Strengths:** Implement true mathematical Shannon Entropy checking.
* **Identify Structural Anti-Patterns:** Catch sequence layouts, repeated sets, and Top 20 standard dictionary strings.
* **Zero Predictability Generation:** Build an execution component tracking logic tied exclusively to CSPRNG architectures.
* **Provide Actionable Remediation:** Convert diagnostic failures into structured mitigation reports.

---

## Features
- **Shannon Entropy Engine:** Accurate mathematical calculation of password strength based on unpredictable character pool footprints.
- **Pattern Recognition & Security Checks:** Detects repeated characters, keyboard sequences (e.g., `qwerty`), and common credentials.
- **CSPRNG-Powered Generator:** Uses Python's `secrets` module to generate high-entropy passwords that are safe from seed-state manipulation.
- **Comprehensive Audit Reporting:** Displays live diagnostic data in the console and exports standard compliance Markdown reports.
- **Educational Knowledge Base:** Built-in threat profiles for credential-stuffing, spraying, dictionary attacks, and brute-force vectors.

---

## Technical Architecture & Methodology

### 1. Entropy Calculation Formula
Password strength is quantified using standard cryptographic Shannon Entropy:

$$E = L \times \log_2(R)$$

Where:
* $E$ = Calculated entropy in bits.
* $L$ = Total character count length of target string.
* $R$ = The calculated size of the pool of unique character classes present.

### 2. Tier Classification Boundaries
* **Very Weak (< 28 bits):** Instantly breakable via online dictionary lookup tables.
* **Weak (28–35 bits):** Vulnerable to automated multi-threaded online brute force scripts.
* **Moderate (36–59 bits):** Safe from casual online guessing; vulnerable to fast offline GPU clusters.
* **Strong (60–79 bits):** Standard enterprise baseline compliance; multi-day compute threshold requirements.
* **Very Strong (≥ 80 bits):** Globally sound infrastructure grade defense metrics. Immune to current brute-force techniques when properly mixed.

---

## Installation & Deployment Guide

### Prerequisites
* Python 3.8 or higher installed on target host system framework.

### Setup Steps
1. Clone this repository to your local directory:
   ```bash
   git clone [https://github.com/muhammad-umair09/secure-password-guide.git](https://github.com/muhammad-umair09/secure-password-guide.git)
   cd secure-password-guide