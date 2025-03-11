SELECT g.id, g.fecha_proceso, g.descripcion, coalesce(y.nombre, '') yapero, g.moneda, g.debe, g.haber , g.idclase
FROM gasto g 
LEFT OUTER JOIN cuenta c ON g.idcuenta = c.id
LEFT OUTER JOIN yapero y ON (g.descripcion LIKE  %s AND SUBSTRING(g.descripcion, 13, 6) = y.numero)
WHERE g.idcuenta = %s AND EXTRACT(MONTH FROM g.fecha_proceso) = %s AND EXTRACT(YEAR FROM g.fecha_proceso) = %s
ORDER BY g.fecha_proceso
