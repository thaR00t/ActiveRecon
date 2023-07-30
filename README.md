# ActiveRecon
Active Reconnaissance automation tool

The script can be run on:
``
Linux and
Windows
``

Installation:

```
pip install -r requirements.txt
```
What the script really does:
1) Ip lookup
2) Whois
3) nslookup
4) Nmap scan (ARP Ping Scan, Parallel DNS resolution, SYN Stealth Scan, Service scan)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Usage:
```
python ar-tool.py <host> // recon of the selected host
python ar-tool.py <host> --save // Save the results into differents files
```
