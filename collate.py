def reduce(input_files, output_files):
    import pandas as pd
    import numpy as np
    from file_names import get_names
    import warnings
    from pathlib import Path
    import os

    script_directory = os.path.dirname(os.path.abspath(__file__)) #Directory of script
    result_directory = os.path.join(script_directory, output_files) #Directory of where to extract to
    os.mkdir(result_directory)

    THIS_FOLDER = Path(__file__).parent.resolve() #Finds the path to the folder that the script is in. This means that the script can still run on PythonAnywhere.
    warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

    file_names = get_names(input_files)

    datetimes = []
    stations = []

    count = 0 

    data_frame = pd.DataFrame()

    for file_name in file_names:

        data = pd.read_csv(str(THIS_FOLDER) + "/" + input_files +"/"+ file_name)

        outputs = data.iloc[:,6].to_list()[1:-1]
        these_stations = data.iloc[:,5].to_list()[1:-1]

        for station in these_stations:
            if station not in stations:
                data_frame[station] = np.zeros(len(datetimes))
                stations.append(station)

        datetime = (data.iloc[:,4].to_list()[2])
        data_frame.loc[datetime] = np.zeros(len(stations))

        index = 0
        for station2 in these_stations:
            data_frame.loc[datetime,station2]=outputs[index]
            index = index + 1

        datetimes.append(datetime)

        count = count + 1
        if(count > 300):
            count = 0
            datetime_name = ("v").join((datetime.split(" ")[0]).split("/"))
            data_frame.to_csv(str(THIS_FOLDER)+ "/"+ output_files+"/"+datetime_name+".csv")
            data_frame = pd.DataFrame()
            datetimes = []
            stations = []