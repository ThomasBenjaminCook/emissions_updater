def activate_crawler(target_directory, date_boundary, url):

    def number_to_date(number):
        year = number[0:4]
        month = number[4:6]
        day = number[6:8]
        return(year+"/"+month+"/"+day)
    
    def compare_dates(this_date,baseline_date,buffer):
        baseline_date_object_with_buffer = baseline_date-dt.timedelta(days=buffer)
        this_date_object = dt.datetime(int(this_date.split("/")[0]),int(this_date.split("/")[1]),int(this_date.split("/")[2]))
        return(this_date_object>=baseline_date_object_with_buffer)

    import os
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    import datetime as dt

    download_directory = os.path.join(os.getcwd(), target_directory) # Directory to save the downloaded files
    os.mkdir(download_directory)

    response = requests.get(url) #Asks for the html page

    soup = BeautifulSoup(response.text, 'html.parser') #Soup translates it to HTML

    links = soup.find_all('a', href=True) #Finds all the links

    # Download each zip file
    for link in links:
        # Get the absolute URL of the zip file
        file_url = urljoin(url, link['href']) #The link will just have the end of the link. Add it to main link.

        # Check if the link points to a zip file
        if file_url.endswith('.zip'):
            numberdate_selected_zip = number_to_date(((file_url.split("/")[-1]).split("_")[-1]).split(".")[0])
            if(compare_dates(numberdate_selected_zip,date_boundary,8)):
                # Send a GET request to download the file
                file_response = requests.get(file_url)

                filename = os.path.basename(file_url) #Extract the filename from the URL

                # Save the file to the download directory
                with open(os.path.join(download_directory, filename), 'wb') as f:
                    f.write(file_response.content)