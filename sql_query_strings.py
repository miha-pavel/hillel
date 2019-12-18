from flask import abort


def unique_name_qs():
    return """
                SELECT DISTINCT count(FirstName)
                FROM customers;
            """


def profit_qs():
    return """
                SELECT ROUND(SUM(UnitPrice * Quantity), 2)
                FROM invoice_items;
            """


def all_customers_qs(country):
    return f"""
                SELECT *
                FROM customers
                WHERE Country =\'{country}\';
            """


def state_city_qs(city, state):
    query_string = f"""
                    SELECT *
                    FROM customers
                    WHERE City=\'{city}\' AND State=\'{state}\';
                """
    if not state:
        query_string = f"""
                        SELECT *
                        FROM customers
                        WHERE City=\'{city}\';
                    """
    if not city:
        abort(400)
    return query_string
