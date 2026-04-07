# sdn-mininet-pox

# SDN Mininet Project using POX Controller

## Title

Traffic Monitoring and Statistics Collection with Firewall using POX Controller

---

## Overview

This project demonstrates a Software Defined Networking (SDN) setup using Mininet and a POX controller.
It implements traffic monitoring, packet statistics collection, and a firewall rule to control network communication.

---

## Tools & Technologies

* Mininet
* POX Controller
* Python
* Ubuntu (WSL / Virtual Machine)

---

## Network Topology

* 1 Switch (s1)
* 3 Hosts (h1, h2, h3)
* Star topology

```
      h1
       |
       |
h2 --- s1 --- h3
```

---

## Features

* Learning switch using MAC address table
* Real-time traffic monitoring (source, destination, port)
* Packet statistics collection per host
* Firewall rule to block specific traffic

---

## Firewall Rule

Traffic from **h1 → h2 (10.0.0.1 → 10.0.0.2)** is blocked.
All other traffic is allowed.

---

## Project Files

* topo.py → Defines network topology
* my_controller.py → POX controller implementation

---

## How to Run

### Start POX Controller

```
cd ~/pox
./pox.py forwarding.my_controller
```

### Run Mininet

```
sudo mn --custom topo.py --topo mytopo --controller=remote
```

### Test Network

```
pingall
h1 ping h2
h2 ping h3
```

---

## Expected Output

* h1 → h2 → Blocked
* h2 → h3 → Successful
* Packet statistics printed in controller terminal

---





## Conclusion

The project demonstrates SDN capabilities such as centralized control, traffic monitoring, and network security using programmable controllers.

