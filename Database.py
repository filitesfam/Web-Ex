import mysql.connector as connector
import pandas as pd
import matplotlib.pyplot as plt


class Database(object):

    def __init__(self):
        self.db = connector.connect(host="localhost", user="root", passwd="root", database="product_development")
        self.cursor = self.db.cursor(buffered=True)

    def write(self, query):
        self.cursor.execute(query)
        self.db.commit()
        return self.cursor

    def read(self, query):
        self.cursor.execute(query)
        return self.cursor

    def add_specialty_if_not_exist(self, specialty: str):
        select_query = "select id from specialty where name ='"+specialty+"'"
        result = self.read(select_query).fetchone()
        if result is None:
            insert_query = "insert into specialty (name) values('"+specialty+"')"
            print(insert_query)
            self.write(insert_query)
            return self.read(select_query).fetchone()[0]
        else:
            return result[0]

    def get_last_inserted_doctor_id(self):
        query = "SELECT id FROM product_development.doctor order by id desc limit 1"
        return self.read(query).fetchone()[0]

    def get_doctor_by_name(self, name: str):
        select_query = 'select id from doctor where name="'+str(name)+'"'
        result = self.read(select_query).fetchone()
        if result is not None:
            return result[0]
        else:
            return None

    def add_doctor(self, doctor):
        doctor_id = self.get_doctor_by_name(doctor["name"])
        if doctor_id is None:
            insert_query = 'insert into doctor (name,city,address,rate,page) values("'+str(doctor["name"])+'","'+str(doctor["city"])+'","'+str(doctor["address"])+'", '+str(doctor["rate"])+',"'+str(doctor["page"])+'")'
            print(insert_query)
            self.write(insert_query)
            return [self.get_last_inserted_doctor_id(), False]
        else:
            return [doctor_id, True]

    def add_doctor_overall_review_detail(self, review_detail, doctor_id):
        add_query = "insert into doctor_rate (doctor_id, communication, Scheduling, staff, treatment, bedside_manner, avg_wait_time) " \
                    "values("+str(doctor_id)+","+str(review_detail["Communication"])+","+str(review_detail["Scheduling"])+","+str(review_detail["Staff"])+","+str(review_detail["Treatment"])+","+str(review_detail["Bedside Manner"])+",'"+str(review_detail["Average Wait Time"])+"')"
        print(add_query)
        self.write(add_query)

    def add_doctor_specialty(self, doctor_id, specialties_id: list):
        query = "insert into doctor_specialty (doctor_id, specialty_id) values "
        insert_values = ""
        for specialty in specialties_id:
            if insert_values != "":
                insert_values += ","
            insert_values += "("+str(doctor_id)+","+str(specialty)+")"
        print(query+insert_values)
        self.write(query+insert_values)

    def add_reviewer_if_not_exist(self, reviewer):
        query = "SELECT id FROM reviewer where name='"+str(reviewer["reviewer_name"])+"'"
        result = self.read(query).fetchone()
        if result is None:
            if reviewer["reviewer_status"] is not None:
                status = 1
            else:
                status = 0
            insert_query = "insert into reviewer (name, trusted) value('"+str(reviewer["reviewer_name"])+"', "+str(status)+")"
            print(insert_query)
            self.write(insert_query)
            return self.get_last_inserted_reviewer_id()
        else:
            return result[0]

    def get_last_inserted_reviewer_id(self):
        query = "SELECT id FROM reviewer order by id desc limit 1"
        return self.read(query).fetchone()[0]

    def add_review(self, review, reviewer_id, doctor_id):
        content = "null"
        title = "null"
        if review["content"] is not None:
            content = review["content"].replace("'", "")
        if review["title"] is not None:
            title = review["title"].replace("'", "")
        if review["review_details"] is not None:
            query = "insert into review(title, content, communication, scheduling, staff, treatment, bedside_manner, wait_time, doctor_id, reviewer_id) values" \
                "('"+str(title)+"','"+str(content)+"',"+str(review["review_details"]["Communication"])+","+str(review["review_details"]["Scheduling"])+","+str(review["review_details"]["Staff"])+","+str(review["review_details"]["Treatment"])+","+str(review["review_details"]["Bedside Manner"])+",'"+str(review["review_details"]["Wait Time"])+"', "+str(doctor_id)+","+str(reviewer_id)+")"
        else:
            query = "insert into review(title, content, doctor_id, reviewer_id) values" \
                "('"+str(title)+"','"+str(content)+"', "+str(doctor_id)+","+str(reviewer_id)+")"
        print(query)
        self.write(query)

    def insert_info(self, doctors_info: list):
        for doctor_info in doctors_info:
            doctor_result = self.add_doctor(doctor_info)
            if doctor_result[1] == False:
                doctor_id = doctor_result[0]
                specialties_id = []
                for specialty in doctor_info["specialty"]:
                    specialties_id.append(self.add_specialty_if_not_exist(specialty))
                self.add_doctor_specialty(doctor_id, specialties_id)
                if doctor_info["rate_detail"] is not None and doctor_info["rate_detail"] != {}:
                    self.add_doctor_overall_review_detail(doctor_info["rate_detail"], doctor_id)
                for review in doctor_info["reviews"]:
                    reviewer_id = self.add_reviewer_if_not_exist(review)
                    self.add_review(review, reviewer_id, doctor_id)

    def calculate_doctor_rate_based_on_specialty(self):
        query = "SELECT" \
                "(sum(d.rate) / count(s.name)) as rate," \
                "s.name as specialty" \
                " FROM product_development.doctor as d" \
                " inner join product_development.doctor_specialty as ds on d.id = ds.doctor_id" \
                " inner join product_development.specialty as s on ds.specialty_id = s.id" \
                " where s.id IN (2,3,4,5,18,25,41)" \
                " group by specialty"

        result = self.read(query).fetchall()
        specialty = []
        rate = []
        for i in range(len(result)-1):
            rate.append(result[i][0])
            specialty.append(result[i][1])

        plt.bar(specialty, rate)
        plt.title("Average rating")
        plt.xlabel("Specialty")
        plt.ylabel("Rate")
        plt.ylim(0, 5)
        plt.show()
        return

    def calculate_number_of_doctor_overall_rate(self):
        query = "SELECT count(id) as count , rate FROM product_development.doctor group by rate order by rate"
        result = self.read(query).fetchall()

        number_of_doctor = []
        rate = []
        for i in range(0, len(result)-1):
            if result[i][1] is None:
                rate.append(0)
            else:
                rate.append(result[i][1])
            number_of_doctor.append(result[i][0])

        plt.bar(number_of_doctor, rate)
        plt.title("Average rating")
        plt.xlabel("Specialty")
        plt.ylabel("Rate")
        plt.ylim(0, 5)
        plt.show()
        return
