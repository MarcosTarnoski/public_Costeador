from django.core.management.base import BaseCommand
from modulos.models import Articulos
import pandas as pd
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = "Add data from file to the database"

    def handle(self, dataframe, model, *args, **options):
        # path_file = "test_compras.xlsx"
        # df = pd.read_excel(path_file)
        engine = create_engine("sqlite:///db.sqlite3")
        dataframe.to_sql(model._meta.db_table, if_exists="replace", con=engine, index = False)
        # to_sql necesita el nombre de la tabla, para esto se aplica "_meta.db_table" a la clase de la tabla