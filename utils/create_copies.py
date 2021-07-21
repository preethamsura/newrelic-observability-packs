#!/usr/local/bin/python3
import os
import json
import sys

template_path = ""
copy_path = ""
keyword_dict = {}
length = 0

"""
Given some input json file with the metadata for how we are going
to be copying files, we take the json and get the corresponding
template_path, copy_path, keyword_dict, and length. As a note, these are global
variables which we update.

INPUTS:
json_location -> path to the json file we want to parse
"""
def parse_json(json_location):
    global template_path, copy_path, keyword_dict, length
    with open(json_location) as json_file:
        data = json.load(json_file)
        template_path = data['template']
        copy_path = data['copy_path']
        keyword_dict = data['keywords']
        length = data['length']

"""

"""
def copy_file_location(template_file, keyword_dict, target_location, length):
    # Make sure we do have enough keywords to replace given our length
    for keywords in keyword_dict.values():
        assert len(keywords) >= length

    if not (".jpg" in template_file or ".png" in template_file or ".jpeg" in template_file):
        f = open(template_file, "r")
        content = f.read()

        # Creates the contents of all the copy files first
        file_contents = [content] * length

        # Creates copies of the file location which will also be updated using the keywords
        file_locations = [target_location] * length

        # Updates the keywords in each of the copies together with the ith index in our keyword_dict
        # corresponding to the ith copy
        for keyword in keyword_dict:
            for i in range(length):
                file_contents[i] = file_contents[i].replace("<" + keyword + ">", keyword_dict[keyword][i])
                file_locations[i] = file_locations[i].replace("<" + keyword + ">", keyword_dict[keyword][i])

        # Creates all the files based on their replaced contents
        for i in range(length):
            filename = file_locations[i]
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            f2 = open(filename, "w")
            f2.write(file_contents[i])

# First we parse the json based on the json path
parse_json(sys.argv[1])

# We update the files with their keywords and copy the files to their new locations
copy_file_location(template_path, keyword_dict, copy_path, 2)