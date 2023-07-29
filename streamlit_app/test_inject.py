import db
p1 = '%chicken%'
q1 = "SELECT * from Recipe WHERE name LIKE %s"
q2 = 'INSERT INTO User (username, email, password, profilePicture) VALUES(%s, %s, %s, %s)'

res = db.query(q2, ['test_inject2', 'test_inject2', 'test_inject', 'test_inject'], insert=True)
print(res)