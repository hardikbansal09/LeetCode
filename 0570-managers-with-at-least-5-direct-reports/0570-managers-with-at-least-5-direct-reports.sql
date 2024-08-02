select e.name    
from Employee as e
join (
    select managerId
    from Employee
    where managerId is not null
    group by managerId
    having count(*)>=5
)m on e.id=m.managerId;