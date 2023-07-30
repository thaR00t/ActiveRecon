#!/usr/bin/python3

import argparse
import platform
import os
import time
import sys
from rich import print
import pyfiglet
import json
from tools import ip_check, nm, wh, nsl


def clear_screen():
    if platform.system() != 'Windows':
        os.system("clear")
    else:
        os.system("cls")

        
def main():
    parser = argparse.ArgumentParser(description="Active Reconnaissance automation tool.")
    parser.add_argument("host", help="Insert the host you'd like to analyze")
    parser.add_argument("--save", action='store_true', help="Save the outputs into .JSON files")
    args = parser.parse_args()
    host = args.host
    save = args.save

    clear_screen()
    print("[bold blue]-[/bold blue]"*19,"[bold red]Ip lookup[/bold red]", "[bold blue]-[/bold blue]"*20)
    a = ip_check.check(host)
    
    if a == 'PUBLIC':
        ip_check.resolver(host)
        print("[bold blue]-[/bold blue]"*50)
        time.sleep(1.5)
        input("Press enter to continue with the whois.\n\n")
        print("[bold yellow]-[/bold yellow]"*20,"[bold blue]Whois[/bold blue]", "[bold yellow]-[/bold yellow]"*23)
        wh.whois_check(host)
        print("[bold yellow]-[/bold yellow]"*50,"\n")
        time.sleep(1.5)
        input("Press enter to continue with nslookup.\n\n")
        print("[bold purple]-[/bold purple]"*20,"[bold white]Nslookup[/bold white]","[bold purple]-[/bold purple]"*20)
        server = str(input("Select a server for the Name server lookup (Ex. 8.8.8.8):\n"))
        nsl.lookup(host,server)
        print("[bold purple]-[/bold purple]"*50)
        time.sleep(1.5)
        input("Press enter to continue with nmap.\n\n")
        print("[bold red]-[/bold red]"*20,"[bold grey]Nmap[/bold grey]","[bold red]-[/bold red]"*24)
        nm.scan(host)
        print("[bold red]-[/bold red]"*50)
    else:
        ip_check.resolver(host)
        time.sleep(1.8)
        print(f"[!] The entered IP address is private, an nmap scan against {host} will occure after you press enter.")
        input("")
        nm.scan(host)
    if save:
        print("\n\n[bold red][!]Do not interrupt the script, the file are going to be save in the working directory.\n")
        ip_check.resolver_saved(host)
        wh.whois_check_saved(host)
        nsl.lookup_saved(host,'8.8.8.8')
        nm.scan_saved(host)
   


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("[bold red]Script interrupted by user.[/bold red]")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
