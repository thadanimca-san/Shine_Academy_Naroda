#!/usr/bin/env python3
import sys
import hashlib
import hmac

SECRET_SALT = 'ShineAcademyEduOSKey2026'

def generate_activation_code(device_code):
    key_bytes = SECRET_SALT.encode('utf-8')
    msg_bytes = device_code.encode('utf-8')
    hash_obj = hmac.new(key_bytes, msg_bytes, hashlib.sha256)
    # Take first 8 chars and uppercase
    return hash_obj.hexdigest()[:8].upper()

if __name__ == "__main__":
    print("========================================")
    print(" SHINE ACADEMY - ACTIVATION CODE GENERATOR")
    print("========================================\n")
    
    if len(sys.argv) > 1:
        device_code = sys.argv[1].upper()
    else:
        device_code = input("Enter the student's Device Code: ").strip().upper()
        
    if len(device_code) != 8:
        print(f"Warning: Expected 8 character device code. Got {len(device_code)} characters.")
        
    activation_code = generate_activation_code(device_code)
    
    print("\n----------------------------------------")
    print(f" DEVICE CODE:     {device_code}")
    print(f" ACTIVATION CODE: {activation_code}")
    print("----------------------------------------\n")
