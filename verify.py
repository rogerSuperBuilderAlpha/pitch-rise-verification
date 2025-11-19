#!/usr/bin/env python3
"""
Pitch Rise Verification Script
Verifies the provided verification code.
"""

import sys
import re

def verify_code(code):
    """
    Verify the provided code format and validity.
    
    Args:
        code (str): The verification code to check
        
    Returns:
        tuple: (is_valid, message)
    """
    # Expected format: PITCH-XXXX-XXXX-XXXX
    pattern = r'^PITCH-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$'
    
    if not code:
        return False, "Error: No code provided"
    
    if not re.match(pattern, code):
        return False, f"Error: Invalid code format. Expected format: PITCH-XXXX-XXXX-XXXX"
    
    # Code format is valid
    return True, f"Verification code '{code}' is valid!"

def main():
    if len(sys.argv) > 1:
        code = sys.argv[1]
    else:
        code = input("Enter verification code: ").strip()
    
    is_valid, message = verify_code(code)
    
    print(message)
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()

