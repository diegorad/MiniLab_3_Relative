import mido
import mido.backends.rtmidi

#Intercept list of control_change midi messages with control value:
interceptList = [86, 87, 89, 90, 110, 111, 116, 117]

#Sensitivity value
sensitivity = 4

class MidiMessageHandler:
    def __init__(self):
        self.previous_message = None
        self.current_message = None

    def handle_midi_message(self, message, output_port):
        self.previous_message = self.current_message
        self.current_message = message
        
        if self.current_message.type == 'control_change' and self.current_message.control in interceptList and hasattr(self.current_message, 'value'):
            if self.previous_message is not None and self.previous_message.type == 'control_change' and hasattr(self.previous_message, 'value') and self.previous_message.control==self.previous_message.control:
                if self.current_message.value > self.previous_message.value:
                    offset = 1 * sensitivity
                elif self.current_message.value < self.previous_message.value:
                    offset = -1 * sensitivity
                else:
                    if self.current_message.value == 0:
                        offset = -1 * sensitivity
                    elif self.current_message.value == 127:
                        offset = 1 * sensitivity
                    else:
                        offset = 0
        
                relVal = 64 + offset
                newMessage=message.copy(value = relVal, channel = 0)
            else:
                newMessage=message.copy(value = 64)
        else:
            newMessage=message.copy()
                    
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
