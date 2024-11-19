from fastapi import FastAPI
from utils import extract_date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import CompanyModel, StockResponse

import os
import dotenv
dotenv.load_dotenv()

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}

@app.get("/test")
def api_test():
    return {"code": 200}


@app.get("/{date_str}", response_model=StockResponse)
def get_date(date_str: str):
    err_res = {
        "error": "Invalid date"
    }
    date_dict = extract_date(date_str)
    if not date_dict:
        return err_res
    engine = create_engine(f'postgresql://{os.environ['DBUSER']}:{os.environ['DBPASSWORD']}@{os.environ['DBHOST']}:{os.environ['DBPORT']}/{os.environ['DBNAME']}')
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(CompanyModel).filter(CompanyModel.date == f'{date_dict["year"]}-{date_dict["month"]}-{date_dict["date"]}').all()

    session.close()
    return {
        'companies': result
    }

@app.get("/{date_str}/{symbol}", response_model=StockResponse)
def get_company(date_str: str, symbol: str):
    err_res = {
        "error": "Invalid date"
    }
    date_dict = extract_date(date_str)
    if not date_dict:
        return err_res
    engine = create_engine(f'postgresql://{os.environ['DBUSER']}:{os.environ['DBPASSWORD']}@{os.environ['DBHOST']}:{os.environ['DBPORT']}/{os.environ['DBNAME']}')
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(CompanyModel).filter(CompanyModel.symbol == symbol.upper(), CompanyModel.date == f'{date_dict["year"]}-{date_dict["month"]}-{date_dict["date"]}').all()

    session.close()
    return {
        'companies': result
    }