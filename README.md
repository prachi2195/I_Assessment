
* Tools & Technologies:

1.    Python
2.    MySQL Workbench
3.   Pandas
4.   pymysql connector
5.   sqlalchemy 

* Working:

1.   Firstly MySQL database has been created with specified schema in MySQL Workbench.
2.   Import "patients.csv" data into "patients" Table
2.   hospital_country.py python script, fetches database by establishing connection with MySQL server. 
3.   The retrieved data is fitted into pandas dataframe for further table manipulation.
4.    show_data() & create_country_table() functions are called to fetch the desired data rows and creating tables 
For example: create_coutry_table("IND") creates "table_ind" in the hospital schema. 
5.    Check the table in mysql workbench.
    

