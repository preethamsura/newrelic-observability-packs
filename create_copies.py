#!/usr/local/bin/python3
import os
import json
import sys

template_path = ""
copy_path = ""
keyword_dict = {}
length = 0

def parse_json(json_location):
    global template_path, copy_path, keyword_dict, length
    with open(json_location) as json_file:
        data = json.load(json_file)
        template_path = data['template']
        copy_path = data['copy_path']
        keyword_dict = data['keywords']
        length = data['length']

def copy_file_location(template_file, keyword_dict, target_location, length):
    if not (".jpg" in template_file or ".png" in template_file or ".jpeg" in template_file):
        f = open(template_file, "r")
        content = f.read()
        file_contents = [content] * length
        file_locations = [target_location] * length
        for k in keyword_dict:
            for i in range(len(keyword_dict[k])):
                file_contents[i] = file_contents[i].replace("<" + k + ">", keyword_dict[k][i])
                file_locations[i] = file_locations[i].replace("<" + k + ">", keyword_dict[k][i])

        for j in range(length):
            filename = file_locations[j]
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            f2 = open(filename, "w")
            f2.write(file_contents[j])

parse_json(sys.argv[1])
copy_file_location(template_path, keyword_dict, copy_path, 2)