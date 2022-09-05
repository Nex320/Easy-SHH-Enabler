import os, sys, platform, time

if platform.system() == "Windows":
                    print(" ")
                    print("This script only supports linux.")
                    print("Please do not attempt to run this on Windows.")
                    print(" ")
                    sys.exit()

while True:
    os.system('clear')
    print("Welcome to the SSH Enable / Disable tool - Made by Nex389.")
    print("Options: enable, disable, status, exit")
    option = input("-> ")
    if option == "enable":
                os.system('clear')
                print("Enabling SSH... This may ask for your password")
                print("----========----")
                os.system('sudo systemctl enable sshd')
                os.system('sudo systemctl start sshd')
                print("----========----")
                print("SSH Should be Enabled now!")
                print("----========----")
                os.system('sudo systemctl status sshd')
                print("----========----")
                i = input("Press Enter to continue... ")
                    
    elif option == "disable":
                os.system('clear')
                print("Disabling SSH... This may ask for your password")
                print("----========----")
                os.system('sudo systemctl stop sshd')
                os.system('sudo systemctl disable sshd')
                print("----========----")
                print("SSH Should be Disabled now!")
                print("----========----")
                os.system('sudo systemctl status sshd')
                print("----========----")
                i = input("Press Enter to continue... ")
    elif option == "status":
                os.system('clear')
                print("SSH Status. This may ask for your password")
                print("----========----")
                os.system('sudo systemctl status sshd')
                print("----========----")
                i = input("Press Enter to continue... ")
    elif option == "exit":
                os.system('clear')
                print("Exiting...")
                sys.exit()
    else:
                os.system(option)                