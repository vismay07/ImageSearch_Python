
#google images package is imported here
from google_images_download import google_images_download  
#  object is created 
response = google_images_download.googleimagesdownload()  
#User input  
search_query = input("Enter something: ")
 # parametrized function is defined downloadimages with arguments for image formatting
def downloadimages(query): 
    arguments = {"keywords": query, "format": "jpg","limit":1, "print_urls":True, "size": "medium", "aspect_ratio": "panoramic"} 
    try: 
        response.download(arguments)      
    except FileNotFoundError:  
        arguments = {"keywords": query,"format": "jpg","limit":1, "print_urls":True,"size": "medium"} 
                        
        try: 
            response.download(arguments)  
        except: 
            pass
  
# here the function is called 
downloadimages(search_query)  
