###########################################
## Transcendnece Stats to JSON Processor ##
#					  #
# Desinged to process the plain text file #
# George has given us into a pretty JSON  #
# file and this will enable us to process # 
# the content dynamically, which makes us #
# very happy. So we can add new content   #
# as it is implimented in the game. 	  #
#					  #
#  Copyright 2010 StarWeaver 		  #
# 	With slight modification by 	  #
#  Copyright 2010 Joe <Ttech> N		  #
##########################################
 
import json, sys, string
from collections import defaultdict

## Some interesting processing stuff ##
# We need to get a name of the file we want to process,
raw_name = sys.argv[1]
raw_path = "../cache/raw/"
processed_path = "../cache/processed/"


input_file = raw_path + raw_name + ".txt"
output_file = processed_path + raw_name + ".json"

def parse_tstats(infile_name, outfile_name):
    sections = defaultdict(dict)
    current_section = "@global"
    player_name = ""

    for line in open(infile_name).readlines():
	line = filtered_string = filter(lambda x: x in string.printable, line)
        if line.strip():
            try:
                key, value = line.split('\t')
                # Many values are simple integers
                try:
                    value = int(value.replace(',',''))
                except ValueError:
#		    try:
#                        value = int(value.replace(',', ''))
#                    except ValueError:
#                        value = value.strip()
                    # Value stays a string
                    value = value.strip()
                sections[current_section][key.strip()] = value
            except ValueError: # <- this means key,value=... failed
                if not player_name:
                    player_name = line.strip()
                    sections[current_section]["@player"] = player_name
                else:
                    current_section = line.strip()
   
    for section in sections:
        # If no item in section has data, it is a simple list
        # This cathes everything I currently have but Exploration
        is_list = True
        for row in sections[section]:
            if sections[section][row]:
                is_list = False

        if is_list:
            sections[section] = [key for key in sections[section]]

    json.dump(sections, open(output_file, 'w'), indent=2, encoding='ascii')

if __name__ == "__main__":
    parse_tstats(input_file, output_file)
