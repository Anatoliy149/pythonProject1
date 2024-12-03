SELECT p.name, SUM(quantity) as total_quantity
FROM products p
	JOIN order_items oi USING(product_id)
	JOIN orders o USING(order_id)
WHERE o.status = 'fullfilled'
GROUP BY p.name
ORDER BY total_quantity DESC
LIMIT 5