from db import create_conn
import pymysql
import pymysql.cursors
import pandas as pd

def query1():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT orders.id , category , sub_category , product_id , cost_price , list_price , quantity , discount_percent , total_price as total_revenue FROM orders inner join order_products on order_products.order_id = orders.id order by order_products.total_price DESC limit 10")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def query2():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT city, SUM(margin_price) AS total_profit_margin FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY city ORDER BY total_profit_margin DESC LIMIT 5;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def query3():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT category , sum(order_products.discount_percent) total_discount FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY category order by total_discount desc;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def query4():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT category, AVG(selling_price) AS average_sale_price FROM orders INNER JOIN order_products on order_products.order_id = orders.id GROUP BY category;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def query5():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT region, AVG(selling_price) AS average_sale_price FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY region ORDER BY average_sale_price DESC;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def query6():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT category, sum(profit_price) AS total_profit FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY category ORDER BY total_profit DESC;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def query7():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT segment, SUM(quantity) AS total_quantity FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY segment ORDER BY total_quantity DESC LIMIT 3;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def query8():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT region, AVG(discount_percent) AS average_discount_percentage FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY region;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def query9():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT category, sum(profit_price) AS total_profit FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY category limit 1;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def query10():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT YEAR(order_date) AS year, SUM(total_price) AS total_revenue FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY YEAR(order_date) ORDER BY year;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

# My Query
def myquery1():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT orders.id , category , sub_category , product_id , cost_price , list_price , quantity , discount_percent , total_price as total_revenue FROM orders inner join order_products on order_products.order_id = orders.id order by order_products.total_price DESC limit 5")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def myquery2():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT region, product_id, SUM(total_price) AS total_revenue FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY region ORDER BY total_revenue desc;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def myquery3():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT YEAR(order_date) AS year, MONTH(order_date) AS month, SUM(total_price) AS total_sales FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY YEAR(order_date), MONTH(order_date) ORDER BY total_sales desc;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def myquery4():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT category, MONTH(order_date) as month , sum(total_price) as total_revenue FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY category, month order by total_revenue, category desc;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def myquery5():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT product_id, YEAR(order_date) as year , sum(quantity) as total_quantity FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY year, product_id order by total_quantity desc limit 10;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def myquery6():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT category, MONTH(order_date) as month , sum(quantity) as total_quantity FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY month, category order by total_quantity desc;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def myquery7():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT YEAR(order_date) AS year, SUM(discount_percent) AS total_discount FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY YEAR(order_date) ORDER BY year;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def myquery8():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT country, SUM(margin_price) AS total_profit_margin FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY country ORDER BY total_profit_margin DESC;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def myquery9():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT state, SUM(cost_price) AS total_cost_price FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY state ORDER BY total_cost_price DESC;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()

def myquery10():
    try:
        db = create_conn()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT postel_code, SUM(total_price) AS total_revenue FROM orders inner join order_products on order_products.order_id = orders.id GROUP BY postel_code ORDER BY total_revenue DESC limit 10;")
        data = cursor.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db.commit()
        db.close()