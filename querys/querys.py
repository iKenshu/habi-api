query_all = """
SELECT DISTINCT pt.address, pt.city, pt.price, pt.description, s.name
FROM habi_db.property as pt
LEFT JOIN (
	SELECT property_id, status_id, max(update_date) AS last_update
	FROM habi_db.status_history
	GROUP BY property_id
) AS sh ON sh.property_id = pt.id
LEFT JOIN (
	SELECT id, name
	FROM habi_db.status
) AS s ON s.id = sh.status_id
WHERE pt.address  IS NOT NULL 
AND s.name  IN ("en_venta", "pre_venta", "vendido")
AND pt.description  IS NOT NULL
AND pt.description != ""
AND s.name IS NOT NULL
AND sh.property_id IS NOT NULL
"""
