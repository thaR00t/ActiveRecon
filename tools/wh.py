def whois_check(host):
    import whois
    who = whois.whois(host)
    print(who.text)
    
def whois_check_saved(host):
    import whois
    who = whois.whois(host)
    with open("whois.txt", 'w') as f:
        f.write(who.text)
    
