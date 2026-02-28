import oracledb

connection = oracledb.connect(
    user="your_username",
    password="your_password",
    dsn="your_dsn"
)
cursor = connection.cursor()

print('\n1.Sifarisler,Ad,Seher:')
cursor.execute('''
SELECT s.sifaris_id, m.ad, m.seher
FROM sifaris s 
INNER JOIN musterii m ON s.musteri_id = m.musteri_id
''')
rows=cursor.fetchall()
for row in rows:
    print(f"Sifaris ID: {row[0]}, Ad: {row[1]}, Seher: {row[2]}")

print('\n2. Sifarisi olmayanlar:')
cursor.execute('''
SELECT m.AD 
FROM musterii m 
LEFT JOIN sifaris s ON m.musteri_id = s.musteri_id
WHERE s.sifaris_id IS NULL
''')
rows=cursor.fetchall()
for row in rows:
    print(f"Musteri: {row[0]}")

print('\n3. 1000-den cox xercleyenler:')
cursor.execute('''
    SELECT m.ad, s.mebleg
    FROM musterii m 
    JOIN sifaris s ON m.musteri_id = s.musteri_id
    WHERE s.mebleg > 1000
''')
rows=cursor.fetchall()
for row in rows:
    print(f"Musteri: {row[0]}, Mebleg: {row[1]}")

print('\n4. Müştərilərin ümumi xərci:')
cursor.execute('''
    SELECT m.ad, SUM(NVL(s.MEBLEG, 0)) 
    FROM musterii m 
    LEFT JOIN sifaris s ON m.musteri_id = s.musteri_id 
    GROUP BY m.ad
''')
rows=cursor.fetchall()
for row in rows:
    print(f'Ad: {row[0]}, Umumi xerc: {row[1]}')

cursor.close()
connection.close()