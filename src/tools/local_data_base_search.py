import pymysql,datetime
class LocalDatabaseSearch:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def query_spouse_and_age_difference(self, name):
        # 连接到MySQL数据库
        connection = pymysql.connect(host=self.host,
                                     user=self.user,
                                     password=self.password,
                                     database=self.database,
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # 查询指定名人及其配偶的出生年份
                query = """
                SELECT name, spouse_name, birth_year, spouse_birth_year
                FROM celebrities
                WHERE name = %s
                """
                cursor.execute(query, (name,))
                result = cursor.fetchone()

                if result:
                    spouse_name = result['spouse_name']
                    birth_year = result['birth_year']
                    spouse_birth_year = result['spouse_birth_year']
                    age_difference = abs(birth_year - spouse_birth_year)
                    return {"配偶": spouse_name, "年龄差": age_difference}
                else:
                    return {"error": "没有找到该名人的信息。"}
        finally:
            connection.close()

    def query_spouse_age(self, name):
        # 假设你的数据库连接设置保持不变...
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # 查询指定名人及其配偶的出生年份
                query = """
                SELECT spouse_birth_year
                FROM celebrities 
                WHERE name = %s
                """
                cursor.execute(query, (name,))
                result = cursor.fetchone()

                if result:
                    current_year = datetime.datetime.now().year
                    spouse_age = current_year - result['spouse_birth_year']
                    return {"配偶年龄": spouse_age}
                else:
                    return {"error": "没有找到该名人的配偶信息。"}
        finally:
            connection.close()

    def run(self, query,query_type):
        if query_type == "age_difference":
            '''该方法用查询配偶以及于计算年龄差'''
            return self.query_spouse_and_age_difference(query)
        elif query_type == "age":
            '''该方法用于查询配偶以及计算配偶年龄'''
            return self.query_spouse_age(query)