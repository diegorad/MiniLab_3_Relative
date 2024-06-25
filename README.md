# MiniLab 3 Relative
Here it is provided a MIDI remote script and a translation layer for the implementation of a "Relative DAW" mode for the Arturia MiniLab 3 controller in Ableton.

The provided "DAW" mode in the MiniLab 3 implements the 8 infinite encoders as abolute knobs. This is a major downfall as when a knob mapping is changed (e.g. when switching tracks), moving the knob will result in the currently mapped parameter value *jumping* to the absolute value of the knob, which is far from ideal. Here I provide a workaround this issue using a modified *MIDI remote script* and a translation layer for the incoming MIDI signals from the Minilab 3.

The `MiniLab_3_Rel` folder is a modified version of the official MIDI remote script included in Ableton 12 for the MiniLab 3. It includes a modification in the *elements.py* module which tells Ableton to expect relative values (*LinearBinaryOffset*) from the MiniLab 3 knobs.

The `Rel_to_abs_translator` folder includes a python script and its executable (only for Apple M series machines) which intercept all messages comming from the MiniLab 3 and translates the values from the 8 encoders from abolute to a relative ones.

Installation
------------

1. Download the files in this repository.
1.	Stop Live if it is running.
1.	Add *MiniLab_3_Rel* to Ableton Live's MIDI Remote Scripts library

	The folder `MiniLab_3_Rel` contains the MIDI Remote Script. To install it follow the [official Ableton's guide to install a third-party remote script](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts).
1. Connect your **MiniLab 3** device to your computer using a USB cable.
1.	Run the translation layer included in the 'Rel_to_abs_translator' folder. It can be executed in two ways (see below). In any case the message `Listening on Minilab3 MIDI and sending on Virtual Output..` indicates that it is successfully runing.
    1) **Using the executable**
       
       Convenient executable versions of the translator script are provided. These can be executed just by double-clicking on them. Currently it is only provided for M series apple machines. The first time it is necessary to make the file executable (refer to [Apple's terminal user guide](https://support.apple.com/guide/terminal/make-a-file-executable-apdd100908f-06b3-4e63-8a87-32e71241bab4/mac) for further info)
    	- Open a terminal window in the directory containing the file, for example:
    	 	```bash
     		   cd /Users/YourUserName/Downloads/MiniLab_3_Relative/Rel_to_abs_translator/Executables/Apple_M
       		```
    	- Make it executable running the following command 
			```bash
     		chmod 755 MiniLab_3_AbsToRelTranslator
     		```
     	- From now on it can be executed by double clicking on it
    
    1) **Running it from python**
  
       The source python script `MiniLab_3_AbsToRelTranslator.py` it is also provided. It can run in any system with the appropiate python setup:
       
        1) **Install Python**:
           - Download the installer from [python.org](https://www.python.org/downloads/). Follow the installation instructions for your operating system.
        1) **Install Required Libraries**:
            - Open a terminal or command prompt.
            - Install `mido` and `python-rtmidi` by running the following commands:
             ```bash
             python3 -m pip install mido[ports-rtmidi]
             ```
             If you encounter issues in this step refer to the [MIDO library documentation](https://mido.readthedocs.io/en/stable/installing.html).
        1) **Run the Script**:
          - Open a terminal or command prompt instance in the directory containing the script.
          - Execute the script with Python:
              ```bash
              python3 MiniLab_3_AbsToRelTranslator.py
              ```
        The details of the commands may vary depending on your system. If you encounter problems please to the [official guide](https://packaging.python.org/en/latest/tutorials/installing-packages/) for further suppont on installing the libraries.
1.	Open Live and enable **MiniLab 3 Rel** as a Control Surface

	In Live’s Preferences go to the *Link, Tempo & MIDI* tab and select *MiniLab 3 Rel* in the dropdown list of available Control Surfaces. As MIDI Input select `Virtual Output`. As MIDI Output select `MiniLab3 (MIDI)`. In the *Input Ports* configuration the *Track* and *Remote* boxes should be unticked for the `MiniLab3` and ticked for the `Virtual Output`. *Takeover mode* can be set to None.
