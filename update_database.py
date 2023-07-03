from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from updater import update
from recent_date import get_recent_date
import datetime as dt

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="ThomasAppMaker",
    password="P_R5nvjG5DV4Vd6",
    hostname="ThomasAppMaker.mysql.pythonanywhere-services.com",
    databasename="ThomasAppMaker$ipcollect",
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

THIS_FOLDER = Path(__file__).parent.resolve()

df = pd.read_sql_table("emissions_database", con=engine, index_col="index")

print(get_recent_date(df))

print(get_recent_date(df) + dt.timedelta(days = 1))

df = update(df)

df.to_sql("emissions_database", con=engine, if_exists="replace")