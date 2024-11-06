import psycopg2

conn = psycopg2.connect(dbname="mortgage", host="localhost", user="admin", password="root", port="5432")

cursor = conn.cursor()
 
cursor.execute("INSERT INTO public.calc_choose (id, title, description, image) VALUES(1, 'Аннуитетные платежи', 'Спланируйте оплату ипотеки равными платежами', 'http://172.18.0.4:9000/images/аннуитетные_платежи.png')")
cursor.execute("INSERT INTO public.calc_choose (id, title, description, image) VALUES(2, 'Дифференцированные платежи', 'Спланируйте оплату ипотеки уменьшающимися платежами', 'http://172.18.0.4:9000/images/дифф_платежи.png')")
cursor.execute("INSERT INTO public.calc_choose (id, title, description, image) VALUES(3, 'Страхование ипотеки', 'Рассчитайте ежемесячные платежи за страховку ипотеки', 'http://172.18.0.4:9000/images/страхование.jpg')")
 
conn.commit()   # реальное выполнение команд sql1
 
cursor.close()

conn.close()