import mysql.connector


class Db:
    def __init__(self):

        # server connection
        try:
            self.connection = mysql.connector.connect(
                host="localhost", user="username", password="password", database="indigo"
            )
            self.my_cursor = self.connection.cursor()
            print("connection successful")
        except:
            print("connection not successful")

    def fetch_city_name(self):

        city = []
        self.my_cursor.execute(
            """
        SELECT DISTINCT(Destination) FROM indigo.flights
        UNION
        SELECT DISTINCT(Source) FROM indigo.flights"""
        )

        data = self.my_cursor.fetchall()
        for item in data:
            city.append(item[0])

        return city

    def fetch_all_cities(self, source, destination):
        if source == destination:
            return "Source and destination cannot be the same"
        else:
            self.my_cursor.execute(
                """SELECT Airline,Route,Dep_Time,Price
                                FROM indigo.flights
                                WHERE Source='{}' AND Destination='{}' 
                                """.format(
                    source, destination
                )
            )

        data = self.my_cursor.fetchall()

        return data

    def airline_freq(self):
        airline, freq = [], []
        self.my_cursor.execute(
            """SELECT Airline,COUNT(*) FROM indigo.flights
                               GROUP BY Airline
                              """
        )

        data = self.my_cursor.fetchall()

        for item in data:
            airline.append(item[0])
            freq.append(item[1])

        return airline, freq
