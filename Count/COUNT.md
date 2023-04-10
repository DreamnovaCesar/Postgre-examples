This SQL query is used to count the number of customers by the number of orders they have placed. Here's an explanation of how it works:

First, a subquery is used to group the orders table by customer_id and count the number of orders placed by each customer. This subquery returns two columns: customer_id and orders.

```SQL
SELECT customer_id, count(order_id) as orders
FROM orders
GROUP BY 1
The subquery is then used as a table (aliased as "a") in the outer query. The outer query groups the result of the subquery by the number of orders ("orders") and counts the number of customers in each group using the count() function. The result set includes two columns: orders and num_customers.
```

```SQL
SELECT orders, count(*) as num_customers
FROM
(
SELECT customer_id, count(order_id) as orders
FROM orders
GROUP BY 1
) a
GROUP BY 1
For example, let's say we have the following data in our "orders" table:
```
order_id	customer_id
1	1
2	2
3	1
4	3
5	1
6	2
7	1
Running the above query will result in the following output:

orders	num_customers
1	1
2	2
3	1
This output shows that there is one customer who has placed one order, two customers who have placed two orders, and one customer who has placed three orders.