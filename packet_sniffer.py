import socket

try:

    # Create raw socket
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

    # Bind socket
    s.bind(("0.0.0.0", 0))

    # Include IP headers
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    print("Sniffer Started...\n")

    while True:

        packet = s.recvfrom(65565)

        print(packet)

except PermissionError:

    print("Run the program as Administrator!")