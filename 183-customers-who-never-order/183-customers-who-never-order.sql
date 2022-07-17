# Write your MySQL query statement below

select customers.name as 'customers'
from customers
where customers.id not in
(
select customerId from orders
);