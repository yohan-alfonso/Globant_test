#pre reqisitos:

#-Run
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# -Then run the following command in the folder where you downloaded: get-pip.py
# python get-pip.py
# then install sql  pip install mysqlclient


import csv
from sqlalchemy import create_engine, select
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry, relationship, Session

# Define the database credentials
user = 'root'
password = 'yohan'
host = '127.0.0.1'
port = 3306
database = 'test_globant'

# Create a connection to the MySQL database
engine = create_engine(f'mysql://{user}:{password}@{host}:{port}/{database}')

mapper_registry = registry()
Base = mapper_registry.generate_base()

class employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    datetime = Column(String(20))
    department_id = Column(Integer, ForeignKey('departments.id'))  # ForeignKey reference
    job_id = Column(Integer, ForeignKey('jobs.id'))  # ForeignKey reference
    
    department = relationship("departments", back_populates="employees")  # Define the relationship
    job = relationship("jobs", back_populates="employees")  # Define the relationship
    
    def __repr__(self):
        return "<employees(id='{0}', name='{1}', datetime='{2}', department_id='{3}', job_id='{4}')>".format(
            self.id, self.name, self.datetime, self.department_id, self.job_id
        )

class departments(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    department = Column(String(50))
    
    employees = relationship("employees", back_populates="department")  # Define the relationship
        
    def __repr__(self):
        return "<departments(id='{0}', department='{1}')>".format(self.id, self.department)

class jobs(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    job = Column(String(50))

    employees = relationship("employees", back_populates="job")  # Define the relationship

    def __repr__(self):
        return "<jobs (id='{0}', job='{1}')>".format(self.id, self.job)   

Base.metadata.create_all(engine)
Base = mapper_registry.generate_base()

# Define your table classes here (same as before)

Base.metadata.create_all(engine)

# Function to insert data from employees.csv
# Function to insert data from employees.csv
def insert_employees_from_csv(file_path):
    with Session(engine) as session:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convert department_id to an integer or use None if it's an empty string or not a valid integer
                department_id = int(row['department_id']) if row['department_id'].isdigit() else None
                
                # Convert job_id to an integer or use None if it's an empty string or not a valid integer
                job_id = int(row['job_id']) if row['job_id'].isdigit() else None
                
                employee = employees(
                    name=row['name'],
                    datetime=row['datetime'],
                    department_id=department_id,
                    job_id=job_id
                )
                session.add(employee)
            session.commit()



# Function to insert data from departments.csv
# Function to insert data from employees.csv
def insert_departments_from_csv(file_path):
    with Session(engine) as session:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                department = departments(
                    department=row['department']
                )
                session.add(department)
            session.commit()


# Function to insert data from jobs.csv
def insert_jobs_from_csv(file_path):
    with Session(engine) as session:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                job = jobs(
                    job=row['job']
                )
                session.add(job)
            session.commit()

# Insert data from CSV files
# Insert data from CSV files
insert_departments_from_csv('./data/departments.csv')
insert_jobs_from_csv('./data/jobs.csv')
insert_employees_from_csv('./data/hired_employees.csv')





