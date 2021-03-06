import telnetlib


class hdmi_controller:
    # define class variables

    outputs = {"output_1": "input_1",
               "output_2": "input_1",
               "output_3": "input_1",
               "output_4": "input_1",
               "output_5": "input_1",
               "output_6": "input_1",
               "output_7": "input_1",
               "output_8": "input_1"}


    # read codes for hdmi switcher

    #
    # These are the codes and the responses
    #
    # R80http://10.13.37.103/potato.jpg01	:  Read INPUT Link States
    # R8002	:  Read OUTPUT Link States
    # R8003	:  Read INPUT HDCP States
    # R8004	:  Read OUTPUT HDCP States
    # R8006	:  Read OUTPUT Channel Set States
    # R8007	:  Read OUTPUT ON/OFF States
    # R8008	:  Read External Audio Output Enable States
    # R8009	:  Read INPUT EDID Set States
    # R8010[x1]	:  Read INPUT x1 EDID Data
    # R8011[x1]	:  Read OUTPUT x1 EDID Data
    # R8012	:  Read Network States
    # R8017	:  Read Cascading Mode Enable/Disable


    read_code = {'input_link_states': ">@ R8001\r", \
                 'output_link_states': ">@ R8002\r", \
                 'input_hdcp_states': ">@ R8003\r", \
                 'output_hdcp_states': ">@ R8004\r", \
                 'output_channel_states': ">@ R8006\r", \
                 'output_onoff_states': ">@ R8007\r", \
                 'system_status': ">@ RSTA\r", \
                 'network_states': ">@ R8012\r"}

    # telnet settings to access hdmi switcher
    HOST = '172.16.1.35'
    TCP_PORT = 23
    BUFFER_SIZE = 32767

    # constructors
    def __init__(self):
        # default constructor
        print("New instance of hdmi_controller has been created")

    def get_outputs(self):
        tn = telnetlib.Telnet(self.HOST, self.TCP_PORT)
        print("Read HDMI Input Link States by sending: ")
        # Write the command to read the input link states
        # tn.write(read_code['input_link_states'])

        tn.write((">@ R8006\r").encode("utf-8"))

        # What input is going to which output?
        # tn.write(read_code['output_channel_states'])
        # Read data until there is a new line

        data = tn.read_until(b'\n')
        data = tn.read_until(b'\n')

        data = str(data).strip()
        new_data = data.split("[")

        print(data)
        for i in range(1, len(new_data)):
            self.outputs['output_' + str(i)] = new_data[i][1]

        tn.close()
        return self.outputs

    def switch_inputs(self, output, input):
        tn = telnetlib.Telnet(self.HOST, self.TCP_PORT)
        # Write the command to read the input link states
        # tn.write(read_code['input_link_states'])

        tn.write((">@ WVSO[" + output + "]I[" + input + "]\r").encode("utf-8"))

        data = tn.read_until(b'\n')
        data = tn.read_until(b'\n')
        print(str(data))

        print(str(data).find("[N]"))

        tn.close()
