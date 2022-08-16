select order_id, count(product_id) as product_count
from bigcommerce_productorderdetails
group by order_id, product_id
having(count(product_id)) > 1
order by  product_count desc ;

/* orders only */
select tbl.order_id, count(tbl.product_count) from (
	select order_id, count(product_id) as product_count
	from bigcommerce_productorderdetails
	group by order_id, product_id
	having(count(product_id)) > 1
	) as tbl
group by order_id
order by count desc