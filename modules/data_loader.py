import os
import pandas as pd

from utils.database import get_engine


def load_data():

    environment = os.getenv(
        "APP_ENV",
        "local"
    )

    if environment == "cloud":
        df = pd.read_csv(
            "data/hotel_bookings.csv"
        )

    else:
        engine = get_engine()

        query = """
        SELECT *
        FROM hotel_bookings
        """

        df = pd.read_sql(
            query,
            engine
        )

    return df