import nmap

nm = nmap.PortScanner()

target = "192.168.1.1"
options = "-sV -sC"

nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        for port in sorted(port_info.keys()):
            state = port_info[port]["state"]
            service = port_info[port].get("name", "")
            print("Port: %s\tState: %s\tService: %s" % (port, state, service))
