def scan(host):
    import nmap3
    import pprint
    nma = nmap3.Nmap()
    result = nma.nmap_version_detection(host)
    #print("{0}".format(result))
    pprint.pprint(result)

def scan_saved(host):
    import nmap3
    nma = nmap3.Nmap()
    result = nma.nmap_version_detection(host)
    resul_t = str(result)
    with open("nmap.json", "w") as f:
        f.write(resul_t)