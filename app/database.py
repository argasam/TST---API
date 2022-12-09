from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, dotenv_values

# choose config files
load_dotenv()
config = dotenv_values(".env")

#Creates database engine
db_user = "doadmin"
db_password = "AVNS_HQ67mah5grQkmlcXlM8"
db_host = "db-arga-plss-ngerjain-tubes-do-user-10225549-0.b.db.ondigitalocean.com"
db_port = 25060
db_database = "worldcup"
db_sslmode = 1
db_engine = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}"
#engine = create_engine("mysql://root:ninjasaga1@localhost/local_tst")
engine = create_engine(db_engine)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
conn = engine.connect()

