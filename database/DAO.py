from database.DB_connect import DBConnect
from model.country import Country


class DAO:

    @staticmethod
    def getAllNodes(anno):
        conn = DBConnect.get_connection()
        if conn is None:
            return []

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT c.CCode AS id, c.StateAbb AS abb, c.StateNme AS name
                   FROM country c, (
                       SELECT state1no AS CCode
                       FROM contiguity
                       WHERE year <= %s
                       UNION
                       SELECT state2no AS CCode
                       FROM contiguity
                       WHERE year <= %s
                   ) stati
                   WHERE c.CCode = stati.CCode
                   ORDER BY c.StateNme"""

        cursor.execute(query, (anno, anno))

        for row in cursor:
            result.append(Country(row["id"], row["abb"], row["name"]))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getAllEdges(anno):
        conn = DBConnect.get_connection()
        if conn is None:
            return []

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT c1.CCode AS id1, c1.StateAbb AS abb1, c1.StateNme AS name1, c2.CCode AS id2, c2.StateAbb AS abb2, c2.StateNme AS name2
                            FROM contiguity co, country c1, country c2
                            WHERE co.state1no = c1.CCode
                            AND co.state2no = c2.CCode
                            AND co.year <= %s
                            AND co.conttype = 1 """

        cursor.execute(query, (anno,))

        for row in cursor:
            stato1 = Country(row["id1"], row["abb1"], row["name1"])
            stato2 = Country(row["id2"], row["abb2"], row["name2"])
            result.append((stato1, stato2))

        cursor.close()
        conn.close()

        return result
