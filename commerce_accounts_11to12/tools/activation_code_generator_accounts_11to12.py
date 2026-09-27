import hmac
import hashlib

# KEEP THIS SECRET! This must match _masterSecret in
# lib/services/license_service.dart exactly, and must be UNIQUE to this
# app (do not reuse the secret from the Maths, English, or Science apps)
# so a code generated here cannot unlock a different app.
MASTER_SECRET = "ShineAcademyAccounts11to12Key2026"


def generate_activation_code(device_id):
    device_id_bytes = device_id.strip().encode('utf-8')
    secret_bytes = MASTER_SECRET.encode('utf-8')

    hashed = hmac.new(secret_bytes, device_id_bytes, hashlib.sha256).hexdigest()

    return hashed[:8].upper()


if __name__ == "__main__":
    print("=== Shine Academy Accounts 11-12 — Activation Code Generator ===")
    while True:
        dev_id = input("\nEnter student's Device Code (or type 'exit' to quit): ")
        if dev_id.lower() == 'exit':
            break
        if not dev_id.strip():
            continue

        code = generate_activation_code(dev_id)
        print(f"Unlock Code to send them: {code}")
