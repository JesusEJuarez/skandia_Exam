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