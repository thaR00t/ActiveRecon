def lookup(host, server='8.8.8.8'):
    import subprocess
    command = subprocess.check_output(['nslookup',host,server]) 
    data = command.decode('utf-8', errors ="backslashreplace")
    data = data.split('\n')
    for i in data:
        print(i)
    
def lookup_saved(host,server='8.8.8.8'):
    import subprocess
    command = subprocess.check_output(['nslookup',host,server]) 
    data = command.decode('utf-8', errors ="backslashreplace")
    data = data.split('\n')
    out = ""
    for i in data:
        out += i+"\n"
    with open("nsl.txt", "w") as f:
        f.write(out)