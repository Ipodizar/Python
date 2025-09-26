import os
import pandas as pd
from sqlalchemy import create_engine

def get_engine():
    """MySQL 연결 엔진 생성 (.env 기반)"""
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")

    # 디버깅용 출력
    print("DEBUG get_engine:", host, user, database)

    url = f"mysql+pymysql://{user}:{password}@{host}:3306/{database}?charset=utf8mb4"
    return create_engine(url, echo=False)

def save_dataframe(df: pd.DataFrame, table_name: str, engine, if_exists: str = "append"):
    """DataFrame을 MySQL 테이블에 저장"""
    df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)
    print(f"✅ DataFrame 저장 완료: {table_name} (rows={len(df)})")