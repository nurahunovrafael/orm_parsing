from peewee import *
from datetime import datetime

user = 'rafael_nurahunov'
password = 'cRR8yqq1'
db_name = 'kenesh'

db = MySQLDatabase(user = user, password = password, database = db_name )

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Deputy(BaseModel):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(max_length=100)
    number = CharField(max_length=100)
    created_at = DateTimeField(
        default = datetime.now()
    )
    bio = TextField()

    class Meta:
        db_table = 'deputy_data'
        order_by = ('created_at', )

try:
    # db.connect()
    Deputy.create_table()
except InternalError as px:
        print(str(px))
