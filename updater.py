def update(dataframe, most_recent_date):
    from crawl import activate_crawler

    activate_crawler("raw_zip_files", most_recent_date,'http://www.nemweb.com.au/Reports/ARCHIVE/Dispatch_SCADA/') #Crawls for all the data beyond the most recent date.

    return(dataframe)