"""
database.py

Purpose:
Create connection between Python
and SQL Server.
"""

import urllib
from sqlalchemy import create_engine


def get_engine():
    """
    Creates SQLAlchemy engine.

    Returns
    -------
    engine object
    """

    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=ADMIN\\SQLEXPRESS;"
        "DATABASE=HotelBookingEDA;"
        "Trusted_Connection=yes;"
    )

    params = urllib.parse.quote_plus(
        connection_string
    )

    engine = create_engine(
        f"mssql+pyodbc:///?odbc_connect={params}"
    )

    return engine