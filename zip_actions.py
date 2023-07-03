def extract_all(extract_from, extract_to):
    import zipfile
    import os

    script_directory = os.path.dirname(os.path.abspath(__file__)) #Directory of script
    target_directory = os.path.join(script_directory, extract_from)
    os.mkdir(target_directory)

    file_names = []

    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_names.append((os.path.join(root, file)).split("\\")[-1]) #Finding all of the filenames in the directory.

    for file_name in file_names:
        zip_file_path = os.path.join(script_directory, (extract_from + "\\" + file_name)) #Find the path to the target zip file.
        destination_folder = os.path.join(script_directory, extract_to)

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref: #Extract the zip file.
            zip_ref.extractall(destination_folder)