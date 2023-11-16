from sqlalchemy import create_engine

class FilesManagement:
    def add_data(self, dataframe, model):
        # path_file = "test_compras.xlsx"
        # df = pd.read_excel(path_file)
        engine = create_engine("sqlite:///db.sqlite3")
        dataframe.to_sql(model._meta.db_table, if_exists="replace", con=engine, index = True, index_label = "id")
        # to_sql necesita el nombre de la tabla, para esto se aplica "_meta.db_table" a la clase de la tabla