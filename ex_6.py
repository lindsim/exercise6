def opening_path_creating_dictionary(path):
    my_file = open(path)
    my_dictionary = {}
   
    for l in my_file: 
        line = l.rstrip()
        line_from_file = line.split(':')
        my_dictionary[line_from_file[0]] = line_from_file[1]

    return my_dictionary

def sort_and_print(dictionary):
    ordered_list_from_dictionary = sorted(dictionary.items())
    
    for name, rating in ordered_list_from_dictionary:
        print "Restaurant %s is rated at %s." % (name, rating)



sort_and_print(opening_path_creating_dictionary("scores.txt"))
