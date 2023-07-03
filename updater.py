def update(dataframe, most_recent_date):
    from crawl import activate_crawler
    from zip_actions import extract_all
    from deleter import delete_files_in_folder, delete_folder

    activate_crawler("raw_zip_files", most_recent_date,'http://www.nemweb.com.au/Reports/ARCHIVE/Dispatch_SCADA/') #Crawls for all the data beyond the most recent date.

    extract_all('raw_zip_files', 'next_layer_zip_files') #Extracts the five min interval zip files from the daily zip files.
    delete_files_in_folder("raw_zip_files")
    delete_folder("raw_zip_files")

    extract_all('next_layer_zip_files', 'raw_csv_files') #Extracts the csv files from the 5 min zip files.
    delete_files_in_folder("next_layer_zip_files")
    delete_folder("next_layer_zip_files")

    return(dataframe)