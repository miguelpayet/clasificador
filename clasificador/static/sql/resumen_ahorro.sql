SELECT EXTRACT(MONTH from g.fecha_proceso) mes, EXTRACT(YEAR from g.fecha_proceso) año, 
    g.moneda, c.nombre, sum(g.debe) debe, sum(g.haber) haber 
FROM gasto g 
LEFT OUTER JOIN yapero y ON (g.descripcion LIKE %s AND SUBSTRING(g.descripcion, 13, 6  = y.numero)) 
LEFT OUTER JOIN clase c ON (g.idclase = c.id) 
WHERE g.idcuenta = %s AND EXTRACT(MONTH FROM g.fecha_proceso) = %s AND EXTRACT(YEAR FROM g.fecha_proceso) = %s 
GROUP BY EXTRACT(MONTH from g.fecha_proceso), EXTRACT(YEAR from g.fecha_proceso), g.moneda, c.nombre 
ORDER BY (SUM(g.debe) IS NOT NULL AND SUM(g.debe) <> 0) DESC, (SUM(g.haber) IS NOT NULL AND SUM(g.haber) <> 0) DESC,  
   c.nombre
