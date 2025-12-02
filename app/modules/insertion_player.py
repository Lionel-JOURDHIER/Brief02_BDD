import pandas as pd

from app.db.tables import Players, Contacts, Addresses, Cities, Countries, Postal_codes, City_pc_corresps
from app.modules.encrypt import encrypt_string
from app.modules.session import create_session
from app.modules.get_player import existing_city_cp, get_city_id, get_pc_id

def players_to_add(data: pd.DataFrame):
    players_to_add = []

    for row in data.itertuples():
        player_to_add = Players(
            first_name = encrypt_string(row.first_name),
            last_name = encrypt_string(row.last_name),
            contact_id = row.contact_id,
            address_id = row.address_id,
            )
        players_to_add.append(player_to_add)
    return players_to_add

def contacts_to_add(data: pd.DataFrame):
    contacts_to_add = []

    for row in data.itertuples():
        contact_to_add = Contacts(
            email = encrypt_string(row.email),
            mobile_phone = encrypt_string(row.mobile_phone)
            )
        contacts_to_add.append(contact_to_add)
    return contacts_to_add

def addresses_to_add(data: pd.DataFrame):
    addresses_to_add = []

    for row in data.itertuples():
        address_to_add = Addresses(
            address_number = encrypt_string(str(row.address_number)),
            street_name = encrypt_string(row.street_name),
            street_type_id = row.street_type_id,
            postal_code_id = row.postal_code_id
            )
        addresses_to_add.append(address_to_add)
    return addresses_to_add

def cities_to_add(data: pd.DataFrame):
    cities_to_add = []
    seen_cities = set()
    #! ADD CHECK CITIES 
    for row in data.itertuples():
        city_name = row.city
        if city_name not in seen_cities:
            seen_cities.add(city_name)
            city_to_add = Cities(
            city_name = (row.city),
            country_id = row.country_id,
            )
            cities_to_add.append(city_to_add)
    return cities_to_add

def countries_to_add(data: pd.DataFrame):
    countries_to_add = []
    seen_countries = set()
    #! ADD CHECK COUNTRIES
    for row in data.itertuples():
        country_name = row.country
        if country_name not in seen_countries:
            seen_countries.add(country_name)
            country_to_add = Countries(
                country_name = (row.country),
                )
            countries_to_add.append(country_to_add)
    return countries_to_add

def postal_code_to_add(data : pd.DataFrame):
    pcs_to_add = []
    seen_pc = set()
    #! ADD CHECK POSTAL CODE
    for row in data.itertuples():
        postal_code = row.postal_code
        if postal_code not in seen_pc:
            seen_pc.add(postal_code)
            pc_to_add = Postal_codes(
                postal_code_value = row.postal_code,
                )
            pcs_to_add.append(pc_to_add)
    return pcs_to_add

def city_cp_corresp_to_add(data : pd.DataFrame):
    city_cps_to_add = []
    existing_city_cps = existing_city_cp()

    for row in data.itertuples():
        if pd.isna(row.postal_code) or pd.isna(row.city) :
            continue
        postal_code_id = get_pc_id(row.postal_code)
        city_id = get_city_id(row.city)
        city_cp_tuple = (postal_code_id, city_id)
        if city_cp_tuple in existing_city_cps :
            city_cp_to_add = City_pc_corresps(
                postal_code_id = postal_code_id,
                city_id = city_id
                )
            city_cps_to_add(city_cp_to_add)
    return city_cps_to_add


def players_all_to_db (data: pd.DataFrame):

    session = create_session()

    for i in players_to_add(data):
        session.add(i)

    for i in contacts_to_add(data):
        session.add(i)

    for i in addresses_to_add(data):
        session.add(i)
        
    for i in cities_to_add(data):
        session.add(i)

    for i in countries_to_add(data):
        session.add(i)

    for i in postal_code_to_add(data):
        session.add(i)
        
    for i in city_cp_corresp_to_add(data):
        session.add(i)
        
    session.commit()
    session.close()