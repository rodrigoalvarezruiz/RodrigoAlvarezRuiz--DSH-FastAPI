# coding: utf-8
from sqlalchemy import Column, Float, Integer, Table, String
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine


t_circuits = Table(
    'circuits', meta,
    Column('circuitId', Integer),
    Column('circuitRef', String(255)),
    Column('name', String(255)),
    Column('location', String(255)),
    Column('country', String(255)),
    Column('lat', Float(asdecimal=True)),
    Column('lng', Float(asdecimal=True)),
    Column('alt', Integer),
    Column('url', String(255))
)


t_constructores = Table(
    'constructores', meta,
    Column('constructorId', Integer),
    Column('constructorRef', String(255)),
    Column('name', String(255)),
    Column('nationality', String(255)),
    Column('url', String(255))
)


t_pilotos = Table(
    'pilotos', meta,
    Column('driverId', Integer),
    Column('driverRef', String(255)),
    Column('number', String(255)),
    Column('code', String(255)),
    Column('dob', String(255)),
    Column('nationality', String(255)),
    Column('url', String(255)),
    Column('forename', String(255)),
    Column('surname', String(255))
)


t_races = Table(
    'races', meta,
    Column('raceId', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('circuitId', Integer),
    Column('name', String(255)),
    Column('date', String(255)),
    Column('time', String(255)),
    Column('url', String(255))
)


t_results = Table(
    'results', meta,
    Column('resultId', Integer),
    Column('raceId', Integer),
    Column('driverId', Integer),
    Column('constructorId', Integer),
    Column('grid', Integer),
    Column('positionOrder', Integer),
    Column('points', Float),
    Column('laps', Integer),
    Column('statusId', Integer)
)

meta.create_all(engine)