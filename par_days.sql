CREATE TABLE flights (
    cust_id INT,
    flight_id VARCHAR(10),
    origin VARCHAR(50),
    destination VARCHAR(50)
);

INSERT INTO flights (cust_id, flight_id, origin, destination) VALUES
(1, 'flight1', 'Delhi', 'Hyderabad'),
(1, 'flight2', 'Hyderabad', 'Kochi'),
(1, 'flight3', 'Kochi', 'Mangalore'),
(2, 'flight1', 'Mumbai', 'Ayodhya'),
(2, 'flight2', 'Ayodhya', 'Gorakhpur');

---
select cust_id, first(origin), last(destination)
from flights
group by cust_id;


select a.*, b.*
from flights a inner join flights b
on a.destination = b.origin