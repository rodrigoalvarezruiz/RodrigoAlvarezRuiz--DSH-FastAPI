use carreraspi;
drop table users;

-- anios con mas carreras:

select raceId, year(date) as anio, count(raceId) as CantRaces
from races
group by anio
order by CantRaces desc;

-- RTA: 2021 con 23 carreras

-- Piloto con mayo cantidad de primeros puestos:

SELECT r.driverId, driverRef as Piloto, count(positionOrder) as Cantidad_de_Primeros_Puestos
FROM results as r
join pilotos as p on r.driverId=p.driverId
where positionOrder = 1
group by r.driverId;

-- hamilton con 95

-- Nombre del circuito más corrido:

SELECT count(raceId) as cant, circuitId, name
FROM races
group by circuitId
order by cant desc;

-- Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British

select sum(r.points) as puntos, p.driverRef, r.driverId
from results r
join pilotos p on (p.driverId = r.driverId)
join constructores c on (c.constructorId = r.constructorId)
where c.nationality = 'American' or c.nationality = 'British'
group by r.driverId
order by puntos desc;

-- hamilton con 3778 puntos

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';

-- primary keys

alter table circuits add primary key(circuitId);
alter table constructores add primary key(constructorId);
alter table pilotos add primary key(driverId);
alter table races add primary key(raceId);
alter table results add primary key(resultId);