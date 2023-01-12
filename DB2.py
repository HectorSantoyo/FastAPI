import psycopg2 as pg
import pandas as pd

sql = '''SELECT a."CountryCode", e."EmployeeName", mg."MgrName" 
FROM "Address" a
JOIN "Employee" e
ON a."AddressId" = e."AddressId"
LEFT JOIN "Mgr" mg
ON mg."MgrId" = e."MgrId"'''

with pg.connect("dbname=employees user=postgres password=''") as conn:
    my_table = pd.read_sql(sql, conn)

    my_table.sort_values("CountryCode", inplace=True)
    duplicated = my_table['CountryCode'].duplicated()
    my_table.loc[duplicated, 'CountryCode'] = ''
    print(my_table)
