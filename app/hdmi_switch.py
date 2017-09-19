import telnetlib
import time
from telnetlib import Telnet

read_code = {'input_link_states': ">@ R8001\r",
             'output_link_states': ">@ R8002\r",
             'input_hdcp_states': ">@ R8003\r",
             'output_hdcp_states': ">@ R8004\r",
             'output_channel_states': ">@ R8006\r",
             'output_onoff_states': ">@ R8007\r",
             'system_status': ">@ RSTA\n",
             'network_states': ">@ R8012\r"}

HOST = "172.16.1.35"
# HOST = "mapscii.me"
TCP_PORT = 23
BUFFER_SIZE = 32767
# Telnet to the HDMI router
tn = telnetlib.Telnet(HOST, TCP_PORT)
print("Read HDMI Input Link States by sending: ")
# Write the command to read the input link states
# tn.write(read_code['input_link_states'])


tn.write((">@ R8006\r").encode("utf-8"))


# What input is going to which output?
# tn.write(read_code['output_channel_states'])
# Read data until there is a new line
data = tn.read_some()
# data = tn.read_lazy()

#   print("We got: " + data)
#   tn.write(read_code['system_status'])

data = tn.read_until(b'\r\n')
print(data)
tn.close()
