CREATE DATABASE carreraspi;


use carreraspi;
drop table resultados;

DROP TABLE IF EXISTS `results`;
CREATE TABLE IF NOT EXISTS `results` (
  	`resultId` 			int(11),
    `raceId` 			int(11),
	`driverId` 			int(11),
    `constructorId` 	int(11),
  	`grid` 				int(11),
    `positionOrder`		int(11),
     `points`			float,
     `laps`				int(11),
     `statusId`			int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
    
SET SESSION sql_mode = '';

LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\resultados.csv"
INTO TABLE `results` 
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

DROP INDEX driverId ON pilotos;