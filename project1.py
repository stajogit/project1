import socket

def get_domain_name(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return "No domain name found"

ip_address = "8.8.8.8" # Google DNS server
domain_name = get_domain_name(ip_address)
print(f"The domain name for {ip_address} is {domain_name}")