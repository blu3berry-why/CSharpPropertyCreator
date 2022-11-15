# This is C# property creator
# it can take this format:
# public Type PropertyName { get; set;}

def create_properties_in_file(in_name, out_name):
    with open(in_name, 'r') as in_file:
        with open(out_name, 'w') as out_file:
            lines = in_file.readlines()
            for line in lines:
                if is_line_property(line):
                    out_file.write(create_property(line))
                else:
                    out_file.write(line)


def create_property(string):
    element_list = remove_empty(string.split(" "))

    public_name = element_list[2]
    private_name = create_private_name(public_name)

    type_name = element_list[1]

    prop = f"""
        public {type_name} {public_name} {{ 
                get {{
                    return {private_name}; }} 
                set {{
                    {private_name} = value; 
                    notifyPropertyChanged(nameof({public_name})); 
            }} 
        }}

        private {type_name} {private_name};

        """

    return prop


def create_private_name(name):
    name = str(name)
    name = name.replace(name[0], name[0].lower(), 1)
    return "_" + name


def run():
    string = "        public string Eredet { get; set; }"

    print(is_line_property(string))


def remove_empty(array):
    new_array = []
    for item in array:
        if item != "":
            new_array.append(item)

    return new_array


def is_property(array):
    if len(array) < 4:
        return False

    if array[2].__contains__("("):
        return False

    if array[0] == 'public' and array[3] == '{':
        return True

    return False


def is_line_property(line):
    return is_property(remove_empty(line.split(" ")))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # run()
    in_file = str(input("adja meg az input filet \n> "))
    out_file = str(input("adja meg az output filet \n> "))

    create_properties_in_file(in_file, out_file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
