from google_images_download import google_images_download  
   
response = google_images_download.googleimagesdownload()  
  
search_query = input("Enter something: ")
  
def downloadimages(query): 
    arguments = {"keywords": search_query, "format": "jpg","limit":1, "print_urls":True, "size": "medium", "aspect_ratio": "panoramic"} 
    try: 
        response.download(arguments)      
    except FileNotFoundError:  
        arguments = {"keywords": search_query,"format": "jpg","limit":1, "print_urls":True,"size": "medium"} 
                        
        try: 
            response.download(arguments)  
        except: 
            pass
  
 
downloadimages(search_query)  
print() 