from itertools import count
from fastapi import APIRouter
from config.db import conn
from models.models import t_pilotos, t_races, t_results, t_constructores
from sqlalchemy import  select, func, desc
from sqlalchemy.sql import text

user = APIRouter()


@user.get('/aniomascarreras')
def get_races():
    return conn.execute(select(func.count(t_races.c.raceId).label('Cantidad_de_Carreras'),
    t_races.c.year).group_by(t_races.c.year).order_by(desc('Cantidad_de_Carreras')).limit(1)).fetchall()


@user.get('/mejorpiloto')
def get_maswins():
    return conn.execute(select(t_results.c.driverId, t_pilotos.c.driverRef.label('Piloto'),
    func.count(t_results.c.positionOrder).label('Cantida_de_Primeros_Puestos')).
    join(t_pilotos, t_results.c.driverId==t_pilotos.c.driverId).where(t_results.c.positionOrder==1).
    group_by(t_results.c.driverId).order_by(desc('Cantida_de_Primeros_Puestos'))).first()


@user.get('/circuitomasrecorrido')
def get_circuitopopular():
    return conn.execute(select(t_races.c.name, t_races.c.circuitId, func.count(t_races.c.raceId).label('Veces_Recorrido')).
    group_by(t_races.c.circuitId).order_by(desc('Veces_Recorrido'))).first()


@user.get('/pilotoconmaspuntos')
def get_maspuntos():
    return conn.execute(select(t_pilotos.c.driverRef, t_results.c.driverId, func.sum(t_results.c.points).label('Puntos')).
    join(t_pilotos, t_results.c.driverId==t_pilotos.c.driverId).join(t_constructores, t_results.c.constructorId==t_constructores.c.constructorId).
    where(t_constructores.c.nationality=='American' or t_constructores.c.nationality=='British').group_by(t_results.c.driverId).
    order_by(desc('Puntos'))).first()