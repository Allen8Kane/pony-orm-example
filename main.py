from pony.orm import Database, PrimaryKey, Required, db_session, set_sql_debug
from pony.orm.core import desc, select
from pony.utils.utils import avg

# set_sql_debug(True)
db = Database(provider='sqlite', filename='database.db', create_db=True)


class User(db.Entity):
    _table_ = "Users"
    id = PrimaryKey(int, auto=True)
    first_name = Required(str)
    salary = Required(int)


db.generate_mapping(create_tables=True)

with db_session:
    users = select(sum(u.salary) for u in User)
    users.show()


# with db_session:
#     User(first_name="alex", salary=300)
#     User(first_name="bob", salary=400)
#     User(first_name="carl", salary=500)
#     User(first_name="david", salary=600)
#     User(first_name="evan", salary=700)
#     User(first_name="frank", salary=800)
#     db.commit()

# with db_session:
#     User(first_name="alex", salary=900)
#     User(first_name="bob", salary=1000)
#     User(first_name="carl", salary=1100)
#     User(first_name="david", salary=1200)
#     User(first_name="evan", salary=1300)
#     User(first_name="frank", salary=1400)
#     db.commit()
