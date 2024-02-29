### CLI COMMANDS FOR FLASK APP.


import pandas as pd
from fuzzywuzzy import process
from models import db, Product, Test
import click




def match_column_names(df_columns, model_attributes):
    column_map = {}
    for attribute in model_attributes:
        match, score = process.extractOne(attribute, df_columns)
        if score > 80:  # Adjust the threshold as needed
            column_map[match] = attribute
    return column_map

def import_csv_to_database(file_path):

    if file_path == "products.csv":
        df = pd.read_csv(file_path,delimiter=";")
        model_attributes = [attr.name for attr in Product.__table__.columns]
        column_map = match_column_names(df.columns, model_attributes)
        for _, row in df.iterrows():
                code = row['Code']

                existing_product = Product.query.filter_by(Code=code).first()

                if existing_product:
                    print(f"Product with code {code} already exists, skipping...")
                else:
                    product_data = {}
                    for csv_column, model_attribute in column_map.items():
                        product_data[model_attribute] = row[csv_column]

                    product = Product(**product_data)
                    db.session.add(product)

        db.session.commit()
    elif file_path == "tests.csv":
        df = pd.read_csv(file_path,delimiter=";")
        model_attributes = [attr.name for attr in Test.__table__.columns]
        column_map = match_column_names(df.columns, model_attributes)
        for _, row in df.iterrows():
                test_data = {}
                for csv_column, model_attribute in column_map.items():
                    test_data[model_attribute] = row[csv_column]

                test = Test(**test_data)
                db.session.add(test)

        db.session.commit()



## CLI Command: flask read-products
# reads the products.csv file into the database
@click.command()
def read_products():
    import_csv_to_database("products.csv")
    click.echo("Products imported successfully!")


@click.command()
def read_tests():
    import_csv_to_database("tests.csv")
    click.echo("Tests imported successfully!")