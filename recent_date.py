def get_recent_date(dataframe):
    import datetime as dt
    not_datetime = dataframe["Datetime"].iloc[-1]
    return(not_datetime)