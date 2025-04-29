# MiniLab 3 Notify (parameter's values)
Improved Ableton MIDI remote script for the Arturia MiniLab 3 controller.

The provided "DAW" mode in the MiniLab 3 configures its encoders as abolute knobs. The issue is that when changing parameters using these knobs, the currently mapped parameter value *jumps* to the absolute value of the knob, which is far from ideal. Here I provide a custom MIDI remote script which fixes this issue. With this script Ableton notifies the Minilab 3 the values of the currently selected device parameters and the MiniLab 3 alings the encoders to these values.

Installation
------------

1. 	Download the files in this repository.
1.	Stop Live if it is running.
1.	Add *MiniLab_3_Notify* to Ableton Live's MIDI Remote Scripts library

	The folder `Minilab_3_notify` contains the MIDI Remote Script. To install it follow the [official Ableton's guide to install a third-party remote script](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts).
1. 	Connect your **MiniLab 3** device to your computer using a USB cable.
1.	Open Live and enable **Minilab 3 notify** as a Control Surface

	In Live’s Preferences go to the *Link, Tempo & MIDI* tab and select *MiniLab 3 Notify* from the dropdown list of available Control Surfaces. As MIDI Input select `MiniLab3 (MIDI)`. As MIDI Output select `MiniLab3 (MIDI)`. *Takeover mode* can be set to None.
