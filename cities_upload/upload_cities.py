import psycopg2
import time


database = psycopg2.connect("dbname='bank' user='bank' host='localhost' password='qwerasdf'")
cursor = database.cursor()


def create_data():
    print '>>> creating '

    # flattened cities with regions and countries
    query_text = '''
        SELECT
            country.id as country_id,
            country.name as country_name,
            region.id as region_id,
            region.name as region_name,
            city.id as city_id,
            city.name as city_name
        FROM
            country
            left join region on region.country_id = country.id
            left join city on region.id = city.region_id
        ORDER BY
            country.id,
            region.id,
            city.id;
        '''
    cursor.execute(query_text)
    result = cursor.fetchall()

    with open('flattened_cities', 'w') as file:
        for row in result:
            # print row[0], row[1], row[2], row[3], row[4], row[5]
            file.write(';'.join([
                str(row[0]),
                row[1],
                str(row[2] if row[2] is not None else ' '),
                row[3] if row[3] is not None else ' ',
                str(row[4]) if row[4] is not None else ' ',
                row[5] if row[5] is not None else ' ',
                '\n'
            ]))


def insert_city(city_id, city_name, region_name, country_id, country_name):
    print 'INSERT INTO company_city (id, city, region, country) VALUES ('
    print city_id, city_name, region_name, country_id, '(', country_name, ')'
    # return
    sql_text = '''
        INSERT INTO company_city (id, city, region, country_id, fed_region, rank)
        VALUES (%s, %s, %s, %s, %s, %s);
    '''
    sql_data = (city_id, city_name, region_name, country_id, region_name, 0)
    cursor.execute(sql_text, sql_data)


def insert_country(country_id, country_name):
    print 'INSERT INTO company_country (id, country) VALUES ('
    print country_id, country_name
    # return
    sql_text = '''
        INSERT INTO company_country (id, country, language)
        VALUES (%s, %s, %s);
    '''
    sql_data = (country_id, country_name, 'ru')
    cursor.execute(sql_text, sql_data)


def upload_data():
    print '>>> uploading '

    agora_countries = {}
    agora_cities = {}

    cursor.execute('''
        SELECT id, country
        FROM company_country
        ORDER BY id;
    ''')
    result = cursor.fetchall()
    for row in result:
        agora_countries[row[0]] = row[1]

    cursor.execute('''
        SELECT id, city
        FROM company_city
        ORDER BY id;
    ''')
    result = cursor.fetchall()
    for row in result:
        agora_cities[row[0]] = row[1]

    free_id_countries = sorted(set(range(1, 1000)) - agora_countries.viewkeys())
    free_id_cities = sorted(set(range(1, 10000)) - agora_cities.viewkeys())

    with open('flattened_cities', 'r') as file:
        for file_row in file:
            row = file_row.split(';')
            try:
                country_id = int(row[0] if row[0] != '' else 0)
            except ValueError:
                country_id = 0
            country_name = row[1]
            region_name = row[3]
            try:
                city_id = int(row[4])
            except ValueError:
                city_id = 0
            city_name = row[5]

            if country_name in agora_countries.values():
                if city_name not in agora_cities.values():
                    agora_country_id = agora_countries.keys()[agora_countries.values().index(country_name)]
                    if city_id in agora_cities.keys():
                        city_id = free_id_cities[0]
                    insert_city(city_id, city_name, region_name, agora_country_id, country_name)
                    agora_cities[city_id] = city_name
                    if city_id in free_id_cities:
                        free_id_cities.remove(city_id)
            else:
                if country_id in agora_countries.keys():
                    country_id = free_id_countries[0]
                insert_country(country_id, country_name)
                agora_countries[country_id] = country_name
                if country_id in free_id_countries:
                    free_id_countries.remove(country_id)
                if city_id in agora_cities.keys():
                    city_id = free_id_cities[0]
                insert_city(city_id, city_name, region_name, agora_country_id, country_name)
                agora_cities[city_id] = city_name
                if city_id in free_id_cities:
                    free_id_cities.remove(city_id)

    database.commit()
    print '...done'


if __name__ == '__main__':
    # create_data()
    upload_data()
