import time

def brute_force_demo(correct_password):
    print("\n[+] Brute Force Simulation Started")

    wordlist = ["admin", "password", "123456", "letmein", "admin123"]

    for attempt_no, guess in enumerate(wordlist, start=1):
        print(f"Attempt {attempt_no}: Trying '{guess}'")
        time.sleep(0.5)

        if guess == correct_password:
            print(f"[SUCCESS] Password cracked: {guess}")
            return

    print("[FAILED] Password not found in wordlist")
