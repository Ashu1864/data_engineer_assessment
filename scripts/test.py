# scripts/load_data.py

import json
import mysql.connector

config = {
    'user': 'db_user',
    'password': '6equj5_db_user',
    'host': '127.0.0.1',
    'database': 'home_db',
    'raise_on_warnings': True,
}

def connect_db():
    return mysql.connector.connect(**config)

def insert_property(cursor, prop):
    add_property = ("INSERT INTO property "
                    "(property_title, address, market, flood, street_address, city, state, zip, property_type, year_built, sqft_basement, bed, bath, latitude, longitude, subdivision, school_average) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data_property = (
        prop.get('Property_Title'),
        prop.get('Address'),
        prop.get('Market'),
        prop.get('Flood'),
        prop.get('Street_Address'),
        prop.get('City'),
        prop.get('State'),
        prop.get('Zip'),
        prop.get('Property_Type'),
        prop.get('Year_Built'),
        prop.get('SQFT_Basement'),
        prop.get('Bed'),
        prop.get('Bath'),
        prop.get('Latitude'),
        prop.get('Longitude'),
        prop.get('Subdivision'),
        prop.get('School_Average'),
    )
    cursor.execute(add_property, data_property)
    return cursor.lastrowid

def insert_leads(cursor, property_id, record):
    add_leads = ("INSERT INTO leads "
                 "(property_id, reviewed_status, most_recent_status, source, occupancy, net_yield, irr, selling_reason, seller_retained_broker, final_reviewer) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data_leads = (
        property_id,
        record.get('Reviewed_Status'),
        record.get('Most_Recent_Status'),
        record.get('Source'),
        record.get('Occupancy'),
        record.get('Net_Yield'),
        record.get('IRR'),
        record.get('Selling_Reason'),
        record.get('Seller_Retained_Broker'),
        record.get('Final_Reviewer'),
    )
    cursor.execute(add_leads, data_leads)

def insert_valuation(cursor, property_id, record):
    add_valuation = ("INSERT INTO valuation "
                     "(property_id, previous_rent, list_price, zestimate, arv, expected_rent, rent_zestimate, low_fmr, high_fmr, redfin_value) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data_valuation = (
        property_id,
        record.get('Previous_Rent'),
        record.get('List_Price'),
        record.get('Zestimate'),
        record.get('ARV'),
        record.get('Expected_Rent'),
        record.get('Rent_Zestimate'),
        record.get('Low_FMR'),
        record.get('High_FMR'),
        record.get('Redfin_Value'),
    )
    cursor.execute(add_valuation, data_valuation)

def insert_hoa(cursor, property_id, record):
    add_hoa = ("INSERT INTO hoa "
               "(property_id, hoa_flag, hoa_amount) "
               "VALUES (%s, %s, %s)")
    data_hoa = (
        property_id,
        record.get('HOA_Flag'),
        record.get('HOA'),
    )
    cursor.execute(add_hoa, data_hoa)

def insert_rehab(cursor, property_id, record):
    add_rehab = ("INSERT INTO rehab "
                 "(property_id, underwriting_rehab, rehab_calculation, paint, flooring_flag, foundation_flag, roof_flag, hvac_flag, kitchen_flag, bathroom_flag, appliances_flag, windows_flag, landscaping_flag, trashout_flag) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data_rehab = (
        property_id,
        record.get('Underwriting_Rehab'),
        record.get('Rehab_Calculation'),
        record.get('Paint'),
        record.get('Flooring_Flag'),
        record.get('Foundation_Flag'),
        record.get('Roof_Flag'),
        record.get('HVAC_Flag'),
        record.get('Kitchen_Flag'),
        record.get('Bathroom_Flag'),
        record.get('Appliances_Flag'),
        record.get('Windows_Flag'),
        record.get('Landscaping_Flag'),
        record.get('Trashout_Flag'),
    )
    cursor.execute(add_rehab, data_rehab)

def insert_taxes(cursor, property_id, record):
    add_taxes = ("INSERT INTO taxes "
                 "(property_id, tax_rate, tax_amount) "
                 "VALUES (%s, %s, %s)")
    data_taxes = (
        property_id,
        record.get('Tax_Rate'),
        record.get('Taxes'),
    )
    cursor.execute(add_taxes, data_taxes)

def main():
    cnx = connect_db()
    cursor = cnx.cursor()

    with open('fake_property_data_new.json', 'r') as f:
        data = json.load(f)

    for record in data:
        property_id = insert_property(cursor, record)
        insert_leads(cursor, property_id, record)
        insert_valuation(cursor, property_id, record)
        insert_hoa(cursor, property_id, record)
        insert_rehab(cursor, property_id, record)
        insert_taxes(cursor, property_id, record)

    cnx.commit()
    cursor.close()
    cnx.close()

if __name__ == '__main__':
    main()
