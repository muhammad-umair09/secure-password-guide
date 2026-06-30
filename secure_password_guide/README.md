# Secure Password Creation Guide & Audit Suite

A modular Identity & Access Management (IAM) educational platform, defensive security analyzer, and cryptographically secure password generation system designed to evaluate key space complexity using mathematical Shannon Entropy.

---

## Badges

---

## Overview

In modern cloud and enterprise architectures, compromised credentials remain the primary initial access vector for malicious threat actors. The **Secure Password Creation Guide & Audit Suite** is an enterprise-grade command-line interface (CLI) tool built to bridge the gap between human behavioral patterns and computational security baselines.

Unlike basic length-based password validators, this suite applies true **Shannon Entropy Calculations**, checks against known leaked dictionary matrices, detects sequential keyboard walk patterns, and enforces custom security policies. It serves as an essential tool for cybersecurity students, SOC Analysts, Blue Team learners, and security awareness training programs.

---

## Features

* 🧠 **Shannon Entropy Engine:** Computes exact mathematical key space predictability in bits.
* 🛑 **Pattern & Sequential Walk Recognition:** Flags repetitive character loops and horizontal/vertical keyboard sequences (e.g., `qwerty`, `asdfgh`).
* 📖 **Dictionary Blacklist Filter:** Screens candidate strings against the top high-risk compromised passwords.
* 🔑 **CSPRNG Secure Generator:** Utilizes Python's `secrets` module (`os.urandom`) instead of pseudo-random utilities to guarantee zero seed predictability.
* 📊 **Compliance Report Exporter:** Automatically generates professional, standalone Markdown (`.md`) audit reports complete with explicit risk designations and actionable remediation steps.
* 🎓 **Cybersecurity Knowledge Base:** Includes native educational briefings on advanced authentication attacks such as Password Spraying and Credential Stuffing.

---

## Screenshots

```text
+------------------------------------------------------------+
|        SECURE PASSWORD CREATION GUIDE & AUDIT SUITE        |
|           Enterprise-Grade IAM Assessment System           |
+------------------------------------------------------------+
|                                                            |
|  1. Run Passive Audit on a Password String                 |
|  2. Run Cryptographically Secure Password Generation Engine |
|  3. Review Educational Threat Vector Briefing              |
|  4. Exit Application Platform                              |
|                                                            |
+------------------------------------------------------------+

```

*(Place actual UI terminal execution screenshot assets inside an `/assets/` directory and update this reference link).*

---

## Demo

To view a terminal record of this tool running live via an interactive mock session, view our Asciinema log:
`[Link to Live Demo Session Placeholder]`

---

## Architecture

This application adheres to clean, decoupled, and modular object-oriented design principles. Business logic, cryptographic generation, and representation layers are explicitly isolated.

* **`config.py`**: Static immutable data layer housing token structures, character sets, and dictionary blocklists.
* **`entropy.py`**: Mathematical computation engine focusing strictly on Shannon Entropy calculations.
* **`analyzer.py`**: Core heuristic evaluation engine assessing string components against rules and calculating risk rankings.
* **`generator.py`**: Cryptographically secure pseudo-random number generator (CSPRNG) policy execution layer.
* **`reports.py`**: Presentation and formatting layer parsing dictionaries into UI logs or exportable markdown compliance artifacts.
* **`app.py`**: Orchestration and control routing interface.

---

## Technology Stack

* **Core Language:** Python 3.8+
* **Standard Library Primitives:**
* `secrets`: Cryptographically Secure Pseudo-Random Number Generation (CSPRNG).
* `math`: Computational log calculation functions.
* `string`: Secure, standardized character definitions.
* `logging`: Enterprise system log output handling.



---

## Installation

### Prerequisites

Ensure your local host has Python 3.8 or a higher runtime environment deployed. Verify using:

```bash
python3 --version

```

### Clone Repository

```bash
git clone https://github.com/muhammad-umair09/secure-password-guide.git
cd secure-password-guide

```

### Install Dependencies

This utility relies entirely on the native Python Standard Library. No external third-party PIP dependencies are required, shrinking your software supply chain attack surface to zero.

### Run Project

Execute the primary orchestration script to initialize the CLI interactive control environment:

```bash
python3 app.py

```

---

## Usage

### 1. Passive Password Auditing

Choose option `1` from the main menu, and input a target password string to evaluate:

```text
[->] Enter target password to evaluate: P@ssword123!

```

**Terminal Report Output:**

```text
============================================================
          PASSWORD SECURITY ASSESSMENT REPORT
============================================================
 Metrics & Analysis  :
  [-] Character Length : 12
  [-] Shannon Entropy  : 78.6 bits
  [-] Strength Category: WEAK
  [-] Risk Designation : HIGH
------------------------------------------------------------
 Defensive Diagnostics & Vulnerabilities:
  [!] WARNING: Found predictable alphanumeric sequence keyboard layout zone: 'word'.
  [!] FAIL: Missing character pools: Lowercase Letters override flag.
------------------------------------------------------------
 Security Remediation Protocols:
  [*] Avoid standard sequential layouts (alphabetic order or sequential rows).
============================================================
Export this data run to standard markdown file report? (y/n): y
[+] Operational Report safely structured and written out to: /path/to/password_audit_report.md

```

### 2. Cryptographically Secure Password Generation

Choose option `2` from the main menu to craft randomized, unguessable key material matching specified corporate security policies:

```text
[->] Define Required Character Length Count: 16
[->] Include Uppercase Alpha [A-Z]? (y/n): y
[->] Include Digits [0-9]? (y/n): y
[->] Include Special Signs [!@#$]? (y/n): y

[+] SECURELY GENERATED UNPREDICTABLE KEY MATERIAL: kP$9!mF_wX29z@aQ

```

---

## Project Structure

```text
secure_password_guide/
├── config.py              # Security thresholds, character pools, and dictionary lists
├── entropy.py             # Mathematical Shannon Entropy calculators
├── analyzer.py            # Rule-based validation and pattern analyzers
├── generator.py           # CSPRNG security password generator module
├── reports.py             # Console layout formatter and markdown report exporter
├── app.py                 # Primary interactive program runtime CLI
└── README.md              # Project documentation file

```

---

## Configuration

All custom thresholds can be securely updated within the `config.py` file. If your compliance framework requires higher entry-level entropy metrics or localized common dictionaries, modify these parameters directly:

```python
# System threshold parameters inside config.py
ENTROPY_THRESHOLDS = {
    "Very Weak": 28,
    "Weak": 36,
    "Moderate": 60,
    "Strong": 80,
    "Very Strong": 128
}

```

---

## Security Considerations

1. **Memory Handling:** Passwords evaluated through the terminal are processed as standard string references in transient volatile system memory. For high-assurance processing, clear memory pools explicitly where necessary to prevent memory scraping.
2. **CSPRNG vs PRNG:** This application strictly avoids Python's default `random` module, as its internal Mersenne Twister engine can be reverse-engineered after observing 624 outputs. By using the `secrets` module, it taps directly into `/dev/urandom`, which is cryptographically secure and safe for production environments.

---

## Testing

To run the automated validation test suites, execute the built-in python discovery command from the project root:

```bash
python3 -m unittest discover -s tests

```

*(Note: Create a separate `/tests/` directory to write targeted verification units for specialized local deployment paths).*

---

## Troubleshooting

### Issue: `ModuleNotFoundError` on Launch

* **Cause:** Running an older, unmapped Python runtime engine environment.
* **Resolution:** Ensure you target execution paths using explicit explicit references: `python3 app.py`.

### Issue: Permission Denied When Exporting Markdown

* **Cause:** The current system user lacks write permissions for the installation directory.
* **Resolution:** Adjust local access configurations or execute the tool within an authorized workspace.

---

## Performance Optimization

The pattern matching architecture utilizes targeted window slides rather than heavy regular expressions (RegEx), keeping the algorithmic runtime complexity bounded at:

$$\mathcal{O}(N)$$

This approach keeps execution lightweight and lightning-fast, making it perfectly suited for high-volume authentication pipelines or embedded Docker containers.

---

## Future Enhancements / Roadmap

* [ ] **HaveIBeenPwned API (v3) Integration:** Implement k-Anonymity SHA-1 hash checks against real-world breach data.
* [ ] **Levenshtein Distance Analysis:** Flag passwords that are minor variants of your organization's name or common localized terms.
* [ ] **Full GUI Integration:** Deconstruct terminal layouts into a streamlined web interface using Streamlit or FastAPI.

---

## Contributing

Contributions are highly encouraged! Please follow this workflow to maintain a reliable project history:

1. Fork the Repository.
2. Create a Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## Code Style Guidelines

All contributions must comply strictly with the PEP 8 programming standard guide layout metrics. Enforce standard variable configurations, clear docstring declarations, and avoid importing unnecessary modules.

---

## Git Workflow

* Main Branch: `main` (Production Ready, fully stable).
* Development Path: Create functional branches targeting descriptive titles: `feature/`, `bugfix/`, `refactor/`.

---

## License

Distributed under the terms of the **MIT License**. For details, review the file artifact contents within `LICENSE`.

---

## Author

**Senior Cybersecurity Engineer & IAM Consultant**

* GitHub Username: [muhammad-umair09](https://www.google.com/search?q=https://github.com/yourusername)
* Specialized Field Focus: Identity Access Management, Threat Vector Penetration Modeling, Secure Software Engineering.

---

## Acknowledgements

* **NIST SP 800-63B:** Guidelines on Digital Identity Guidelines and Authentication Management parameters.
* **OWASP Top 10:** Framework for addressing Authentication Design Flaws and Broken Access Control mechanics.

---

## Support

For technical assistance or deployment questions, please open an Issue in the official GitHub repository tracker.

---

## Contact Information

* **Project Maintainer:** security-eng@yourdomain.local
* **Security Reporting:** security-bounties@yourdomain.local

---

## Star the Repository

If this Identity and Access Management tool helped you understand Shannon Entropy or improved your security awareness programs, **please star this repository and fork it to build your portfolio!** ⭐