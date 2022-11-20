#Importing python tiktokapi sdk
from TikTokApi import TikTokApi as tiktok      
#Import helper.py for data preprocessing
from helpers import process_results
import pandas as pd

#Import sys dependency to extract command line arguments
import sys

#Function to get tiktok data from the streamlit app
def get_Data(hashtag):
    #Get cookie data
    verifyFp = "verify_kx2ee558_BH6fvQVi_cXHF_4lfK_Bimg_hH0lYMCV6Vm6"       #verify_kx2ee558_BH6fvQVi_cXHF_4lfK_Bimg_hH0lYMCV6Vm6
    #Setup instance
    api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

    #Get data by trending
    trending = api.by_hashtag(hashtag)
    # print(trending)

    #Process data
    flattened_data = process_results(trending)


    #Export data to json
    # with open('processed_export.json', 'w') as f:
    #     json.dump(flattened_data, f)

    # Convert the preprocessed data to a dataframe
    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    df.to_csv('tiktokdata.csv', index = False)  
    
    
#Running the function using command line so tiktokapi and streamlit doesnt get conflict errors
if __name__ == '__main__':
    get_Data(sys.argv[1])