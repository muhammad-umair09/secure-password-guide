"""
Main Application Orchestrator: app.py
Description: Launches CLI framework processing control for password generation and auditing.
Author: Senior Cybersecurity Engineer
"""
import sys
from analyzer import PasswordAnalyzer
from generator import SecurePasswordGenerator
from reports import ReportEngine

def display_banner():
    print("""
############################################################
#                                                          #
#       SECURE PASSWORD CREATION GUIDE & AUDIT SUITE       #
#          Enterprise-Grade IAM Assessment System          #
#                                                          #
############################################################
    """)

def display_educational_insights():
    print("""
================================================================================
                    CYBERSECURITY EDUCATION BRIEFING
================================================================================
1. WHY PASSWORD SECURITY MATTERS:
   In modern infrastructure, authentication tokens are the primary perimeter line. 
   Weak password structures result in immediate entry Vectors for unauthorized persistence.

2. RECONNAISSANCE & AUTHENTICATION ATTACKS:
   - Brute-Force Attacks : Systematic permutation guessing across keyspaces.
   - Dictionary Attacks  : Using automated wordlists of previously leaked credentials.
   - Credential Stuffing : Testing stolen username/password pairs across unrelated platforms.
   - Password Spraying   : Testing a few common passwords (like 'Password123') across thousands of enterprise accounts to bypass account lockout thresholds.

3. STRATEGIC MODERN CONTROLS:
   - Multi-Factor Authentication (MFA): Imposes secondary independent challenges (TOTP/WebAuthn).
   - Password Managers   : Eliminates reuse by generating and keeping encrypted local storage keys.
   - Entropy Standard    : Strive for > 80 bits of structural layout complexity.
================================================================================
    """)

def run_cli_loop():
    while True:
        display_banner()
        print("1. Run Passive Audit on a Password String")
        print("2. Run Cryptographically Secure Password Generation Engine")
        print("3. Review Educational Threat Vector Briefing")
        print("4. Exit Application Platform")
        
        choice = input("\nSelect Action Option [1-4]: ").strip()
        
        if choice == "1":
            target = input("[->] Enter target password to evaluate: ").strip()
            if not target:
                print("[-] Input error: String length cannot be zero.")
                continue
            
            analyzer = PasswordAnalyzer(target)
            results = analyzer.analyze()
            ReportEngine.print_terminal_report(results)
            
            export_choice = input("Export this data run to standard markdown file report? (y/n): ").strip().lower()
            if export_choice == 'y':
                ReportEngine.export_to_markdown(results)
                
        elif choice == "2":
            try:
                length = int(input("[->] Define Required Character Length Count: ").strip())
                inc_upper = input("[->] Include Uppercase Alpha [A-Z]? (y/n): ").strip().lower() == 'y'
                inc_digits = input("[->] Include Digits [0-9]? (y/n): ").strip().lower() == 'y'
                inc_special = input("[->] Include Special Signs [!@#$]? (y/n): ").strip().lower() == 'y'
                
                generated_pass = SecurePasswordGenerator.generate(length, inc_upper, inc_digits, inc_special)
                print(f"\n[+] SECURELY GENERATED UNPREDICTABLE KEY MATERIAL: {generated_pass}")
                
                # Automatically run analytics tracking verification output
                analyzer = PasswordAnalyzer(generated_pass)
                ReportEngine.print_terminal_report(analyzer.analyze())
            except ValueError:
                print("[-] Format validation error: Length parameter requires integer conversion values.")
                
        elif choice == "3":
            display_educational_insights()
            input("Press [Enter] to resume program loop interaction...")
            
        elif choice == "4":
            print("\n[+] Gracefully closing execution session frameworks. Stand down.")
            sys.exit(0)
        else:
            print("[-] Choice match index missing. Review selection parameter range.")

if __name__ == "__main__":
    try:
        run_cli_loop()
    except KeyboardInterrupt:
        print("\n\n[-] Context termination triggered from keyboard sequence. Shutting down system controls.")
        sys.exit(0)