def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename,'r') as f:
        for line in f:
            cast_light.append(line.strip())
    return cast_list
