# Sparkify Amazon Redshift ETL
 Using Python to create a data pipeline to store data in Apache Cassandra.

 ## Project Overview
Sparkify is a ficitional music company that has a set of datasets that needs to be stored in an Amazon Web Service Database. The purpose of the project is to extract. tranform, and load these files onto Amazon Rdshift so that it could be used for further analysis. 

## Resources
- Data Sources: http://millionsongdataset.com/
- Software: Python 3.6.1, Amazon Redshift, AWS S3, PostreSQL 12.0

## Summary 
The project was to create an data pipeline that would extract datasets from a csv file and transform it in python to be useable. It would finally be loaded on to apache cassandra where the databases could be used for analysis.

1. First the dataset filepath was located using the glob package.
2. Cql schema code was created to create three different tables from the dataset.
3. A partition and clustering column was set to create a primary key.
4. Each table were then loaded onto cassandra.
5. These datasets were then tested with queries to see if the primary key was functional.
6. The tables were then dropped and the session and cluster were shutdown.