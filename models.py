from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date,FileType

class UserData(Model):
    id = Column(Integer, primary_key=True)
    first_name =  Column(String(1500),nullable=False)
    middle_name =  Column(String(1500),nullable=False)
    last_name = Column(String(1500),nullable=False)



    Langulages = Column(String(1500),nullable=False)
    exp_year = Column(String(1500),nullable=False)
    designation = Column(String(1500),nullable=False)
    exp_in = Column(String(1500),nullable=False)
    # image = Column(String(1500),nullable=False)

