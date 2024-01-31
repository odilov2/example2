from datetime import datetime

import BASE


class City:
    def __init__(self, city_id, name):
        self.city_id = city_id
        self.name = name
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_into(data):
        query = f"""
        INSERT INTO city(name) VALUES('{data['name']}')
        """
        return BASE.Database.connect(query)


class Address:
    def __init__(self, address_id, city_id, name):
        self.address_id = address_id
        self.city_id = city_id
        self.name = name
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_into(data):
        query = f"""
        INSERT INTO address(city_id, name) VALUES('{data['city_id']}', '{data['name']}')
        """
        return BASE.Database.connect(query)


class Kasalxona:
    def __init__(self, kasalxona_id, address_id, name, work_start_time, end_start_time):
        self.kasalxona_id = kasalxona_id
        self.address_id = address_id
        self.name = name
        self.work_start_time = work_start_time
        self.end_start_time = end_start_time

    @staticmethod
    def insert_into(data):
        query = f"""
        INSERT INTO kasalxona(address_id, name, work_start_time, end_start_time) VALUES('{data['address_id']}', '{data['name']}',  '{data['work_start_time']}', '{data['end_start_time']}')
        """
        return BASE.Database.connect(query)


class Staff:
    def __init__(self, staff_id, address_id, first_name, last_name, phone_number):
        self.staff_id = staff_id
        self.address_id = address_id
        self.first_name = first_name
        self.last_name =  last_name
        self.phone_number = phone_number
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_into(data):
        query = f"""
        INSERT INTO staff(address_id, first_name, last_name, phone_number) VALUES('{data['address_id']}','{data['first_name']}', '{data['last_name']}', '{data['phone_number']}')
        """
        return BASE.Database.connect(query)


class People:
    def __init__(self, people_id, staff_id, address_id, first_name, last_name):
        self.people_id = people_id
        self.staff_id = staff_id
        self.address_id = address_id
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def insert_into(data):
        query = f"""
        INSERT INTO people(staff_id, address_id, first_name, last_name) VALUES('{data['staff_id']}','{data['address_id']}',  '{data['first_name']}', '{data['last_name']}')
        """
        return BASE.Database.connect(query)


class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_into(data):
        query = f"""
        INSERT INTO category(name) VALUES('{data['name']}')
        """
        return BASE.Database.connect(query)


class Staff_category:
    def __init__(self, category_id, staff_id):
        self.category_id = category_id
        self.staff_id = staff_id
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_into(data):
        query = f"""
        INSERT INTO staff_category(category_id, staff_id) VALUES('{data['category_id']}', '{data['staff_id']}')
        """
        return BASE.Database.connect(query)

