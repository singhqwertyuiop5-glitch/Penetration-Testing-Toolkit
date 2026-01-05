from port_scanner import port_scan
from brute_force_demo import brute_force_demo

def show_menu():
    print("\n--- Penetration Testing Toolkit ---")
    print("1. Port Scanner")
    print("2. Brute Force Demo")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            target = input("Enter target IP (127.0.0.1 recommended): ")
            ports = [21, 22, 80, 443, 8080]
            port_scan(target, ports)

        elif choice == "2":
            brute_force_demo("admin123")

        elif choice == "3":
            print("Exiting toolkit...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
