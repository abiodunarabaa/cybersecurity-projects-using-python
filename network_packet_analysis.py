from scapy.all import sniff

# Define a callback function to handle each packet
def packet_handler(packet):
    # Print packet summary
    print(packet.summary())

# Sniff packets on the network and invoke the packet_handler function for each packet
# Adjust the parameters as needed (e.g., iface for interface, filter for specific protocols)
sniff(prn=packet_handler, count=10)  # Sniff 10 packets

#This script imports the sniff function from the scapy library, which allows you to capture and analyze network packets.
#It defines a callback function packet_handler to handle each packet captured by the sniffer. 
#The packet_handler function simply prints a summary of each packet.

#You can adjust the parameters passed to the sniff function to customize the behavior of the packet sniffer. 
#For example, you can specify the interface (iface) on which to sniff packets or apply a filter (filter) to capture only packets of specific protocols.
