import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#создание записей

for i in range(10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i+1}", f"example{i+1}@gmail.com", f"{(i+1)*10}", "1000"))

#обновление данных записей

for i in range(10):
    if (i+1) % 2 != 0:
        cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i+1))

#удаление записей

count = 0
while count < 10:
    cursor.execute('DELETE FROM Users WHERE id = ?', (count+1,))
    count = count + 3

cursor.execute(" SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст:{user[2]} | Баланс: {user[3]}')



connection.commit()
connection.close()