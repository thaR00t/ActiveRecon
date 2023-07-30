import ipapi

def check(host):
    from IPy import IP
    import socket
    ip_address = socket.gethostbyname(host)
    ip_check = IP(ip_address)
    return ip_check.iptype()

def resolver(host):
    import socket
    from requests import get
    from IPy import IP
    from rich import print
    try:
        ip_address = socket.gethostbyname(host)
        print(f'{host} - {ip_address}')
        ip_check = IP(ip_address)
        print(f"The following IP address {ip_address} is {ip_check.iptype()}\n")
        print("[bold red]-[/bold red]"*15,"[bold blue]Additional info[/bold blue]", "[bold red]-[/bold red]"*18)
        response = get(f'https://ipapi.co/{ip_address}/json/').json()
        location_data = {
            "country": response.get("country_name"),
            "region": response.get("region"),
            "ip": response.get("ip"),
            "network": response.get("network"),
            "version": response.get("version"),
            "city": response.get("city"),
            "region": response.get("region"),
            "region_code": response.get("region_code"),
            "country": response.get("country"),
            "country_name": response.get("country_name"),
            "country_tld": response.get("country_tld"),
            "asn": response.get("asn"),
            "org": response.get("org")
        }
    
        for key in location_data:
            print(f"{key}: {location_data[key]}")
        #ipapi.location(ip=host)
    except socket.gaierror as e:
        print(f"Could not resolve the hostname: {host}\nThe error is the following:\n {e}")
    

def resolver_saved(host):
    import socket
    from requests import get
    from IPy import IP
    from rich import print
    
    ip_address = socket.gethostbyname(host)
    ip_check = IP(ip_address)        
    response = get(f'https://ipapi.co/{ip_address}/json/').json()
    datas = {
        "country": response.get("country_name"),
        "region": response.get("region"),
        "ip": response.get("ip"),
        "network": response.get("network"),
        "version": response.get("version"),
        "city": response.get("city"),
        "region": response.get("region"),
        "region_code": response.get("region_code"),
        "country": response.get("country"),
        "country_name": response.get("country_name"),
        "country_tld": response.get("country_tld"),
        "asn": response.get("asn"),
        "org": response.get("org")
    }
    data = ""
    for keys in datas:
        data += f"{keys}:{datas[keys]}"+"\n"
    with open("ip_check.txt", "w")as f:
        f.write(data)   

    