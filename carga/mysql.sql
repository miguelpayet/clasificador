drop table gasto;

create table gasto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cuenta varchar(20),
    fecha_proceso date,
    fecha_consumo date,
    descripcion varchar(40),
    ciudad varchar(15),
    pais varchar(3),
    tipo varchar(10),
    moneda varchar(3),
    debe double,
    haber double,
    clase varchar(40)
)

drop table yapero;

create table yapero(
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero varchar(9),
    nombre varchar(40)
)