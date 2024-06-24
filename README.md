# MiniLab_3_Relative
MIDI remote script and translation layer for the implementation of a "Relative DAW" mode for the Arturia MiniLab 3 controller in Ableton.

The MiniLab_3_Rel folder is a modified version of the official MIDI control script included in Ableton 12 for the MiniLab 3. It includes a modification in the elements.py module which tells Ableton to expect relative (LinearBinaryOffset) values from the MiniLab 3 knobs.

The Rel_to_abs_translator folder includes a python script and its executable (only for Apple M series machines) which intercept all messages comming from the MiniLab 3 and translated the values from the 8 encoders from an abolute value (0 - 127) to a relative one.
