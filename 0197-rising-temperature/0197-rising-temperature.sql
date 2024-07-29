# Write your MySQL query statement below
select w1.id
from Weather as w1
join Weather as w2
on DATE_SUB(w1.recordDate, INTERVAL 1 DAY) =w2.recordDate
where w1.temperature>w2.temperature