import os

#given_directory = "./_template"
given_directory = "./test"

keyword_dict = {
    "main": ["test1", "test2"],
    "CLUSTER-NAME": ["cluster1", "cluster2"]
}

def copy_directory(template_dir, keyword_dict):
    contents = os.listdir(template_dir)
    for c in contents:
        new_path = template_dir+"/"+ c
        if os.path.isfile(new_path):
            copy_file(new_path, keyword_dict)
        elif os.path.isdir(new_path):
            copy_directory(new_path, keyword_dict)

def copy_file(template_file, keyword_dict):
    if not (".jpg" in template_file or ".png" in template_file or ".jpeg" in template_file):
        f = open(template_file, "r")
        content = f.read()
        file_contents = [content]*len(keyword_dict["main"])
        for k in keyword_dict:
            for i in range(len(keyword_dict[k])):
                file_contents[i] = file_contents[i].replace("<" + k + ">", keyword_dict[k][i])
        for j in range(len(file_contents)):
            filename = template_file.replace(given_directory, "./" + keyword_dict["main"][j])
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
                
            f2 = open(filename, "w")
            f2.write(file_contents[j])


copy_directory(given_directory, keyword_dict)

#copy_directory(given_directory, {})