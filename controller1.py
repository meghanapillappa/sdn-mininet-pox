
from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

# MAC learning table
mac_to_port = {}

# Packet statistics
packet_stats = {}

def _handle_PacketIn(event):
    packet = event.parsed
    if not packet:
        return

    dpid = event.dpid

    # Initialize switch table
    if dpid not in mac_to_port:
        mac_to_port[dpid] = {}

    src = packet.src
    dst = packet.dst
    in_port = event.port

    # =========================
    # 📊 TRAFFIC MONITORING
    # =========================
    key = str(src)
    if key not in packet_stats:
        packet_stats[key] = 0

    packet_stats[key] += 1

    print("\n==========================")
    print(f"Packet from: {src}")
    print(f"To: {dst}")
    print(f"In Port: {in_port}")
    print(f"Total packets from {src}: {packet_stats[key]}")
    print("==========================")

    # =========================
    # 🔥 FIREWALL (IP BASED)
    # Block h1 → h2
    # =========================
    ip_packet = packet.find('ipv4')

    if ip_packet:
        src_ip = str(ip_packet.srcip)
        dst_ip = str(ip_packet.dstip)

        if src_ip == "10.0.0.1" and dst_ip == "10.0.0.2":
            print("🚫 BLOCKED: h1 → h2")
            return  # Drop packet

    # =========================
    # 🧠 LEARNING SWITCH
    # =========================
    mac_to_port[dpid][src] = in_port

    if dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][dst]
    else:
        out_port = of.OFPP_FLOOD

    # =========================
    # 📤 SEND PACKET
    # =========================
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.in_port = in_port
    msg.actions.append(of.ofp_action_output(port=out_port))

    event.connection.send(msg)


def launch():
    log.info("POX Controller running with monitoring, statistics & firewall...")
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
```
