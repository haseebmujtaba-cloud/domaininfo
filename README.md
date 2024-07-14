# Domain Information Gathering Script

This Python script gathers various pieces of information about a given domain, including its IP address, DNS records, server details, and WHOIS information.

## Prerequisites

- Python 3.x installed
- Required Python packages:
  - `requests`
  - `dnspython`
  - `python-whois`

Install the required packages using pip:

```bash
pip install requests dnspython python-whois
```

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your/repository.git
    cd repository-directory
    ```

2. Run the script:

    ```bash
    python domaininfotool.py
    ```

3. Follow the prompts:

    Enter the domain name when prompted.

4. View the results:

    The script will display the gathered information for the provided domain.

## Features

- **IP Address**: Retrieves the IP address of the domain.
- **DNS Records**: Fetches various DNS records (A, AAAA, MX, NS, TXT) associated with the domain.
- **Server Details**: Retrieves server information (via HTTP headers) for the domain.
- **WHOIS Information**: Fetches registration details for the domain.

## Error Handling

- Errors encountered during the retrieval of information (such as network issues or invalid domains) are captured and displayed with appropriate error messages.

## Notes

- Make sure your environment has network access to query DNS records and access WHOIS services.
- Ensure the domain name entered is correctly formatted and exists.
- Some features may not work if the domain does not support certain types of DNS records or WHOIS information is not publicly available.

