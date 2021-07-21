#!/usr/local/bin/python3
import os
import json
import sys

def main():
    # First we parse the json based on the json path
    create_copies(sys.argv[1])

"""

"""
def create_copies(json_location):
    with open(json_location) as json_file:
        data = json.load(json_file)

        # Keywords and length are constant regardless of files we are copying
        keyword_dict = data['keyword_dict']
        length = data['length']

        # We can copy over multiple different files using the same keywords
        copies = data['copies']
        for copy in copies:
            template_file = copy['template_file']
            target_location = copy['target_location']
            copy_file_location(template_file, keyword_dict, target_location, length)

"""

"""
def copy_file_location(template_file, keyword_dict, target_location, length):
    print(f"create_copies.py: Copying template file: {template_file}")
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

if __name__ == "__main__":
    main()