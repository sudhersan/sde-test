# Command Line instructions

docker run sde-test-image input_file.json output_file.json

Command expects one argument for input file and another for output file. Else it fails.

## Design

* Created seperate list for Corporate and government bonds
* Looped over Corporate bond List(Outer loop) and govermennt bond(Inner Loop) to calculate yield and spread
* Before Step2, sorted government bond list in descending order based on outstanding amount to help with tie breaker situation.The one with the highest was used.
* Tested all scenarios for the expected output.


