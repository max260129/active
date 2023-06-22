import argparse
import sys
import socket
import select

class CustomHelpParser(argparse.ArgumentParser):
    def format_help(self):
        custom_help = """
        Welcome to TinyScanner v1.0.0

        Usage: tinyscanner [OPTIONS] [HOST] [PORT]

        OPTIONS:
            -p, --ports  Single port or range of ports to scan
            -u, --udp  UDP scan
            -t, --tcp  TCP scan
            --help  Show this message and exit.
        """
        return custom_help

def tcp_scan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
    except socket.gaierror:
        print('Hostname could not be resolved.')
    except socket.error:
        print("Couldn't connect to server.")


import select

def udp_scan(host, port):
    try:
        # Créer un socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(5)  # Délai d'attente de 5 secondes

        # Essayer d'envoyer des données à l'hôte sur le port spécifié
        sock.sendto(bytes("data", "utf-8"), (host, port))

        ready = select.select([sock], [], [], 5)
        if ready[0]:
            # Si on reçoit une réponse, on la lit
            data, addr = sock.recvfrom(1024)
        else:
            # Si on ne reçoit pas de réponse après 5 secondes, on suppose que le port est ouvert
            print(f"Port {port} is open")

        sock.close()

    except socket.gaierror:
        print('Hostname could not be resolved.')
    except socket.error:
        print(f"Port {port} is closed.")

        

def main(argv):
    parser = CustomHelpParser(description='TinyScanner')
    parser.add_argument('host', type=str, nargs='?', help='The host to scan.')
    parser.add_argument('-p', '--ports', type=str, help='Single port or range of ports to scan.')
    parser.add_argument('-u', '--udp', action='store_true', help='UDP scan.')
    parser.add_argument('-t', '--tcp', action='store_true', help='TCP scan.')

    args = parser.parse_args(argv)

    if args.tcp:
        if args.host and args.ports:
            if '-' in args.ports:
                start_port, end_port = map(int, args.ports.split('-'))
                for port in range(start_port, end_port + 1):
                    tcp_scan(args.host, port)
            else:
                tcp_scan(args.host, int(args.ports))
        else:
            print("Please specify a host and a port or a range of ports for the TCP scan.")
    elif args.udp:
        if args.host and args.ports:
            if '-' in args.ports:
                start_port, end_port = map(int, args.ports.split('-'))
                for port in range(start_port, end_port + 1):
                    udp_scan(args.host, port)
            else:
                udp_scan(args.host, int(args.ports))
        else:
            print("Please specify a host and a port or a range of ports for the UDP scan.")


if __name__ == "__main__":
    main(sys.argv[1:])
