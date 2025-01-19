# Skandia prubea técnica 
## Ejercicio 1: SQL 
Para importar el archivo EXCEL a una base SQL utilice un [script](Ejercicio_1/import_Excel_to_SQL.py) de python, lo que me permite automatizar este proceso. 
Para obener los puntos solicitados utilice la siguiente [consulta](Ejercicio_1/query.sql):

```sql
SELECT 
    c."Customer" AS cliente,
    COUNT(s."SalesOrderLineKey") AS numero_ordenes,
    SUM(s."Sales Amount") AS monto_total
FROM "Sales_data" s
JOIN "Customer_data" c ON s."CustomerKey" = c."CustomerKey"
WHERE s."CustomerKey" != -1  -- Excluye datos no aplicables
GROUP BY c."Customer"
ORDER BY monto_total DESC
LIMIT 10;

```
El resultado obtenido fue el siguiente: <br />
<img src="img/Resultado1.jpg" alt="Resultado 1" />


## Ejercicio 2: Power Automate
