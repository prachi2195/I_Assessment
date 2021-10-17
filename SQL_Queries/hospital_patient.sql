create schema hospital;
use hospital;

drop table if exists patients;
CREATE TABLE if not exists `patients` (
  `Name` varchar(255) NOT NULL,
  `cust_ID` int(18) NOT NULL,
  `Open_date` date NOT NULL,
  `Consult_dt` date,
  `VAC_Type` char(5) Default "None",
  `Dr_Name` varchar(45) DEFAULT NULL,
  `State` char(5) DEFAULT NULL,
  `Country` char(5),
  `PostCode` int(5),
  `DOB` date DEFAULT NULL,
  `Active` char(3),
  PRIMARY KEY (`Name`)
);
describe patients;
SELECT * FROM hospital.patients;

select * from table_au;
select * from table_ind;
select * from table_phil;
select * from table_uk;
select * from table_usa;