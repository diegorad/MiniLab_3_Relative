import mido
import mido.backends.rtmidi

#Intercept list of control_change midi messages with control value:
interceptList = [86, 87, 89, 90, 110, 111, 116, 117]

#Sensitivity value
sensitivity = 4

class MidiMessageHandler:
    def __init__(self):
        self.message_states = {}

    def handle_midi_message(self, message, output_port):
        if message.type == 'control_change' and message.control in interceptList and hasattr(message, 'value'):
            control_index = message.control
            
            if control_index not in self.message_states:
                self.message_states[control_index] = {'previous_message': None, 'current_message': None}
            
            self.message_states[control_index]['previous_message'] = self.message_states[control_index]['current_message']
            self.message_states[control_index]['current_message'] = message
    
            prev_msg = self.message_states[control_index]['previous_message']
            curr_msg = self.message_states[control_index]['current_message']

            if prev_msg is not None and prev_msg.type == 'control_change' and hasattr(prev_msg, 'value') and prev_msg.control == curr_msg.control:
                if curr_msg.value > prev_msg.value:
                    offset = 1 * sensitivity
                elif curr_msg.value < prev_msg.value:
                    offset = -1 * sensitivity
                else:
                    if curr_msg.value == 0:
                        offset = -1 * sensitivity
                    elif curr_msg.value == 127:
                        offset = 1 * sensitivity
                    else:
                        offset = 0
                        
                relVal = 64 + offset
                newMessage = message.copy(value=relVal, channel=0)
            else:
                newMessage = message.copy(value=64)
        else:
             newMessage = message.copy()
                

        output_port.send(newMessage)

def main():
    # Create virtual MIDI input and output ports
    input_port_name = 'Minilab3 MIDI'
    output_port_name = 'Virtual Output'

    # Open virtual input and output ports
    with mido.open_input(input_port_name) as input_port, mido.open_output(output_port_name, virtual=True) as output_port:
        print(f"Listening on {input_port_name} and sending on {output_port_name}...")

        message_handler = MidiMessageHandler()

        # Listen for incoming MIDI messages
        for message in input_port:
            message_handler.handle_midi_message(message,output_port)

if __name__ == "__main__":
    main()
