import paramiko
import time
import requests

# Define variables
ROUTER_IP = "192.168.1.1"  # Change this to your router's IP address
ROUTER_USERNAME = "admin"  # Change this to your router's username
ROUTER_PASSWORD = "password"  # Change this to your router's password
WAN_INTERFACE = "eth0"  # Change this to your WAN interface name
LAST_IP = ""  # Variable to store the last WAN IP address

# Loop forever
while True:
    # Get the current WAN IP address
    current_ip = requests.get('https://api.ipify.org').text.strip()

    # If the IP address has changed, update the router configuration
    if current_ip != LAST_IP:
        print(f"WAN IP address has changed to {current_ip}")
        
        # Create an SSH client and connect to the router
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(ROUTER_IP, username=ROUTER_USERNAME, password=ROUTER_PASSWORD)
        
        # Enter configuration mode and update the WAN interface configuration
        ssh_shell = ssh_client.invoke_shell()
        ssh_shell.send("configure\n")
        time.sleep(1)
        ssh_shell.send(f"set interfaces ethernet {WAN_INTERFACE} address {current_ip}/24\n")
        time.sleep(1)
        ssh_shell.send("commit\n")
        time.sleep(1)
        ssh_shell.send("save\n")
        time.sleep(1)
        ssh_shell.send("exit\n")
        time.sleep(1)
        
        # Close the SSH connection
        ssh_client.close()
        
        LAST_IP = current_ip

    # Wait 5 minutes before checking again
    time.sleep(300)
