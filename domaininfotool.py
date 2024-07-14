import socket
import requests
import dns.resolver
import whois

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.error as err:
        return f"Error retrieving IP address: {err}"

def get_dns_records(domain):
    records = {}
    try:
        for record_type in ['A', 'AAAA', 'MX', 'NS', 'TXT']:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [str(rdata) for rdata in answers]
    except Exception as err:
        records['Error'] = f"Error retrieving DNS records: {err}"
    return records

def get_server_details(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        server = response.headers.get('Server', 'N/A')
        return server
    except requests.RequestException as err:
        return f"Error retrieving server details: {err}"

def get_whois_info(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as err:
        return f"Error retrieving WHOIS info: {err}"

def main():
    domain = input("Enter domain: ")
    print(f"Gathering information for domain: {domain}\n")

    ip_address = get_ip_address(domain)
    print(f"IP Address: {ip_address}\n")

    dns_records = get_dns_records(domain)
    print("DNS Records:")
    for record_type, records in dns_records.items():
        print(f"  {record_type}: {records}")
    print()

    server_details = get_server_details(domain)
    print(f"Server Details: {server_details}\n")

    whois_info = get_whois_info(domain)
    print("WHOIS Information:")
    for key, value in whois_info.items():
        print(f"  {key}: {value}")
    print()

if __name__ == "__main__":
    main()
