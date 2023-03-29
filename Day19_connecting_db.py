import mysql.connector
from config import USER, PASSWORD, HOST

class DBConnectionError(Exception):
    pass
def connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password",
        database=db_name
    )
    return cnx

def get_all_records():
    try:
        db_name = "tests"
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        query = """SELECT * FROM abcreport"""
        cur.execute(query)
        result = cur.fetchall() #returns a list with records where each is a tuple
        for record in result:
            print(record)
        cur.close()
    except Exception:
        raise DBConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB Connection is closed")

def calc_commission(sold_items, commission):
    sales = []
    for item in sold_items:
        sales.append(item[2])

    commission = sum(sales) * (commission/100)
    return commission
def get_all_records_from_rep(rep_name):
    try:
        db_name = "tests"
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")
        query = f"""SELECT Item, Units, Total FROM abcreport WHERE Rep='{rep_name}'"""
        cur.execute(query)
        result = cur.fetchall()  # returns a list with records where each is a tuple
        for record in result:
            print(record)
        cur.close()

        comp = round(calc_commission(result, commission=10), 2)
    except Exception:
        raise DBConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()

    print(f"Commission for {rep_name} is {comp}")
    return rep_name, comp

import datetime as dt
record = {
    "OrderDate": "2020-12-15",
    "Region": "Central",
    "Rep": "Evans",
    "Item": "pen",
    "Units": 200,
    "UnitCost": 2.5,
    "Total": 200*2.5
}

def insert_new_record(record):
    try:
        db_name = "tests"
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")
        query = """INSERT INTO abcreport ({}) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
            ", ".join(record.keys()),
            record["OrderDate"],
            record["Region"],
            record["Rep"],
            record["Item"],
            record["Units"],
            record["UnitCost"],
            record["Total"],
        )
        cur.execute(query)
        db_connection.commit() # VERY IMPORTANT
        cur.close()
    except Exception:
        raise DBConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB Conn Closed")


def main():
    get_all_records()
    # get_all_records_from_rep("Jones")
    # insert_new_record(record)

if __name__ == "__main__":
    main()