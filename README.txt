PiMorseCode Readme:

--- Usage ---
sudo python PiMorse.py [-h] [-D] [-d DIT] [-g GPIO] [-c CODE] [-f] text

--- Parameters ---
-h / --help : Show commandline help
-D / --debug: Output the sequence that is being shown
-d / --DIT  : (float) The amount of seconds that the smallest light. The timing of the whole program depends on this value. default: 0.3
-g / --GPIO : (int) The # of the GPIO-Pin (BCM-Mode), default = 4
-c / --code : (string) The CodeFile for non morseCode usage. default: morseCode.cod
-f / --file : takes the text-value as a filename to read from. File contents will be converted and sent
text	    : The Text to send

--- simple circuit ---
  GPIO----(X)-----Ground


