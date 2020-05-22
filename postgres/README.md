# Sparkify Postgres ETL
 Using Python to create a data pipeline to store data in PostgreSQL.

## Project Overview
Sparkify is a ficitional music company that has a set of datasets that needs to be stored in a postgres database. The purpose of the project is to extract. tranform, and load these files onto postgres so that it could be used for further analysis. 

## Resources
- Data Sources: http://millionsongdataset.com/
- Software: Python 3.6.1, PostgreSQL 12.0, pgAdmin4 4.2

## Summary 
The project was to create an data pipeline that would extract datasets from a json file and transform it in python to be useable. It would finally be loaded on to postgres where the databases could be used for analysis.

1. First the dataset filepaths were first located using a function.
2. Each different databases were then created in the sql schema code.
3. The create_table.py was then run to create the tables in postgres.
4. The etl.ipynb was then used to transform the different tables.
5. Five different tables were then extracted, transformed, and loaded onto postgres.
