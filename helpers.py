#For preprocessing data
def process_results(data):
    #These are in nested format. So need to carry additional preprocesing
    nested_values = ['video', 'author', 'music', 'stats', 'authorStats', 'challenges', 'duetInfo', 'textExtra', 'stickersOnItem']

    #These are worthless data that we will skip
    skip_values = ['challenges', 'duetInfo', 'textExtra', 'stickersOnItem']
                      
    #Create blank dictionary
    flattened_data = {}

    #Loop through each video
    for idx,value in enumerate(data):                         #Adding a unique index to the data
        flattened_data[idx] = {}
        #loop through each property in each video
        for property_id, property_val in value.items():       
        #Checking if its nested data
            if property_id in nested_values: 
                #Checking if its a skip data
                if property_id in skip_values:
                    pass           
                else:
                    #Loop through each nested property
                    for nested_idx, nested_val in property_val.items():
                        flattened_data[idx][property_id+'_'+nested_idx] = nested_val
            #If not a nested data add them to the flattened data dictionary
            else:
                flattened_data[idx][property_id] = property_val

    return flattened_data       
                   