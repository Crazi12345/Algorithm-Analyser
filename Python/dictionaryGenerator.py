def input_nodes():
    number_of_nodes = int(input("Please enter the number of nodes: "))
    
    nodes_dict = {}  # Initialize an empty dictionary
    
    for i in range(number_of_nodes):
        key = input("Please enter the key for node {}: ".format(i+1))
        
        values = input("Please enter comma separated values for node {}: ".format(i+1)).split(',')
        
        nodes_dict[key] = values
        
    return nodes_dict

nodes_dict = input_nodes()
print(nodes_dict)
