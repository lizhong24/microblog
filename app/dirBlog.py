from app import db, models

u1 = models.User.query.get(1)

posts = u1.posts.all()

for p in posts:
    print(p.id, p.author.nickname, p.body)

u2 = models.User.query.get(2)
print(u2.posts.all())

models.User.query.order_by('nickname desc').all()
