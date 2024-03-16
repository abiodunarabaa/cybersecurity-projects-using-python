from scapy.all import *

# Define the target IP range
target_ip_range = "192.168.1.1/24"

# Send ICMP ping requests to the target IP range
ans, unans = sr(IP(dst=target_ip_range)/ICMP(), timeout=2)

# Process the responses
for sent, received in ans:
    print(received.sprintf("IP %IP.src% is online"))

# Display the list of IPs that did not respond to the ICMP ping
for sent in unans:
    print(sent.dst, "did not respond")

#Example:
#Import the sr function from Scapy, which is used to send packets and receive responses.
#Define the target IP range to scan (target_ip_range) as "192.168.1.1/24", which represents all IP addresses in the 192.168.1.0/24 subnet.
#Send ICMP ping requests (ICMP()) to each IP address in the target IP range using the sr function. We specify a timeout of 2 seconds.
#Process the responses (ans) and print out the IP addresses that responded to the ICMP ping requests.
#Print out the IP addresses that did not respond (unans) "'