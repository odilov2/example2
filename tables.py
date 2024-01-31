from BASE import Database


def create_tables():
    city = f"""
    CREATE TABLE city(
        city_id SERIAL PRIMARY KEY,
        name VARCHAR(40),
        last_update TIMESTAMP DEFAULT NOW())
    """

    address = f"""
    CREATE TABLE address(
        address_id SERIAL PRIMARY KEY,
        city_id INT REFERENCES city(city_id),
        name VARCHAR(40),
        last_update TIMESTAMP DEFAULT NOW())
    """

    kasalxona = f"""
    CREATE TABLE kaslaxona(
        kasalxona_id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        address_id INT REFERENCES address(address_id),
        work_start_time TIME,
        end_start_time TIME)
    """

    staff = f"""
    CREATE TABLE staff(
        staff_id SERIAL PRIMARY KEY,
        address_id INT REFERENCES address(address_id),
        first_name VARCHAR(40),
        last_name VARCHAR(40),
        phone_number VARCHAR(10),
        last_update TIMESTAMP DEFAULT NOW())
    """


    people = f"""
    CREATE TABLE people(
        people_id SERIAL PRIMARY KEY,
        staff_id INT REFERENCES staff(staff_id),
        address_id INT REFERENCES address(address_id),
        first_name VARCHAR(40),
        last_name VARCHAR(40))
    """


    category = f"""
    CREATE TABLE category(
        category_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        last_update TIMESTAMP DEFAULT NOW())
    """


    staff_category = f"""
    CREATE TABLE staff_category(
        category_id INT REFERENCES category(category_id),
        staff_id INT REFERENCES staff(staff_id),
        last_update TIMESTAMP DEFAULT NOW())
    """
    tables = [city, address, kasalxona, staff, people, category, staff_category]
    for table in tables:
        data = Database.connect(table)
        print(data)


if __name__ == "__main__":
    create_tables()