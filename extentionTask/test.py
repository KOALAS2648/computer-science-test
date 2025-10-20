data ={101: {'name': 'Python Basics', 'borrowed': True}, 102: {'name': 'AI Explained', 'borrowed': True}, 103: {'name': 'Data Structures', 'borrowed': True}, 104: {'name': 'The Code Breakers', 'borrowed': True}}

def write_to_file(filename, dict_to_write):
    filewrite = open(filename, "w")
    for i in dict_to_write:
        temp = dict_to_write[i]
        filewrite.write(f"{i},")
        filewrite.write(f"{temp['name']},")
        filewrite.write(f"{temp['borrowed']}")
        filewrite.write("\n")

correct = False

if correct:
    print("hello")