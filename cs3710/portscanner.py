# Wesley Stepler (pws3ms)
# CS 3710, Introduction to Cybersecurity
# Programming Assignment 1: Port Scanner

# Sources consulted: 
# https://docs.python.org/3/library/socket.html
# https://realpython.com/python-sockets/
# https://www.geeksforgeeks.org/port-scanner-using-python/

import socket
import datetime

addr = input("Enter a target to scan: ")
host = socket.gethostbyname(addr) # Use the user input to get the target's IP address or domain name.

port_start = int(input("Enter a Start Port: ")) # Port we will start scanning at
port_end = int(input("Enter an End Port: ")) # The first port we don't scan

print(f"Port scan started at {datetime.datetime.now()}") # Display the start time of the port scan.
for port in range(port_start, port_end): # Loop through each port and check if it's open
    network = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a new socket object
    network.settimeout(1)
    check_port = network.connect_ex((host, port)) # Establish a connection with the port on our target machine
                                                  # using the socket object we created
    if check_port == 0: # If the port is open, print the following message.
        print(f"Port {port} is open.")
    else: # Otherwise, print this message
        print(f"Port {port} is closed.")
print(f"Port scan completed at {datetime.datetime.now()}.")
