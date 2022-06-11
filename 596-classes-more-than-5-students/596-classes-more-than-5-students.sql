/* Write your PL/SQL query statement below */
select class
From courses
group by class
having count (distinct student) >=5