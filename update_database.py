from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="ThomasAppMaker",
    password="P_R5nvjG5DV4Vd6",
    hostname="ThomasAppMaker.mysql.pythonanywhere-services.com",
    databasename="ThomasAppMaker$ipcollect",
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

THIS_FOLDER = Path(__file__).parent.resolve()

df = pd.read_csv(THIS_FOLDER / "emissions_file.csv")
df.to_sql("emissions_database", con=engine, if_exists="replace")