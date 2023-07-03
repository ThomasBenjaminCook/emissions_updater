def extract_all(extract_from, extract_to):
    import zipfile
    import os
    from file_names import get_names

    script_directory = os.path.dirname(os.path.abspath(__file__)) #Directory of script
    result_directory = os.path.join(script_directory, extract_to) #Directory of where to extract to
    os.mkdir(result_directory)

    file_names = get_names(extract_from)

    for file_name in file_names:
        zip_file_path = os.path.join(script_directory, (extract_from + "\\" + file_name)) #Find the path to the target zip file.
        destination_folder = os.path.join(script_directory, extract_to)

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref: #Extract the zip file.
            zip_ref.extractall(destination_folder)