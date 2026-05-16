from scapy.all import sniff, IP, TCP, UDP, Raw

# Function to analyze packets
def packet_info(packet):

    # Check if packet contains IP layer
    if packet.haslayer(IP):

        print("\n========== Packet Captured ==========")

        # Source IP
        print("Source IP      :", packet[IP].src)

        # Destination IP
        print("Destination IP :", packet[IP].dst)

        # Detect Protocol
        if packet.haslayer(TCP):
            print("Protocol       : TCP")

        elif packet.haslayer(UDP):
            print("Protocol       : UDP")

        else:
            print("Protocol       : Other")

        # Display Payload Data
        if packet.haslayer(Raw):

            payload = packet[Raw].load

            print("Payload Data   :", payload[:50])

        print("=====================================")

# Start packet sniffing
print("Starting Packet Sniffer...\n")

sniff(prn=packet_info, store=False, count=10)