

class Filter:
        def __init__(self):
                self.whitelist = whitelist(file)(file)

        def whitelist(file):
                add = "INSERT INTO whitelist (filter_name) VALUES (%s)"
                cur.execute(add, file)
                connection.close()
