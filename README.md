# Canteen_DB
- We develop a database system for the college campus eateries using SQL.
- The file Canteen_Database.sql contains a populated database. After downloading it, unsqueeze it and run main.py to use the database.

## DEMO
A demo video is attached showing all the usecases.

## Python Script Commands
To run the application, type `python 2.py` in the terminal.  
To import the SQL dumpfile:  
```mysql -u your_username -p your_database_name < path/to/database_dump.sql```

## Commands
### Retrievals
#### Selection
1. Command 1
Select all menu items at a given price.  
```select ItemName as Item, Quantity, Price, UnitsSold as 'Units Sold', CanteenID as Canteen```  
```from MENU_ITEMS```  
```where Price = {};```

3. Command 2
Select all the canteens which open before a particular time on a particular day of
the week.  
```1select CanteenID as Canteen, OpeningYear as 'Opening Year', Location, {}```  
```from CANTEEN```  
```where '{}' < {};```  

### Projection
1. Command 1
Return the names of all the menu items that have a price more than Rs ‘X’.  
```select ItemName, Price as Item```  
```from MENU_ITEMS```  
```where Price > {};```

2. Command 2
Return the names of customers who are older than ‘Y’ years of age.  
```select Cname as Name, TIMESTAMPDIFF(YEAR, CDOB, CURDATE()) as Age```  
```from CUSTOMER```  
```where TIMESTAMPDIFF(YEAR, CDOB, CURDATE()) > {};```  

#### Aggregate
1. Command 1
The MIN salary paid to the staff in a particular canteen.  
```SELECT MIN(Salary) AS 'Minimum Salary' FROM STAFF where CanID = {};```  
2. Command 2
The AVG cost of all menu items in a particular canteen.  
```SELECT AVG(Price) AS 'Average Cost' FROM MENU_ITEMS where CanteenID = {} ;```  

#### Searching
1. Command 1
Searches for staff with names beginning with a particular prefix.  
```SELECT Name FROM STAFF_DETAILS WHERE Name LIKE '{}%';```  
2. Command 2
Searches for Menu Items with names beginning with a particular prefix.  
```SELECT ItemName as Name FROM MENU_ITEMS WHERE ItemName LIKE '{}%';```  

### Analysis
1. Command 1
Find the top 5 selling items.  
```SELECT ItemName, Quantity, CanteenID, SUM(UnitsSold) AS TotalUnitsSold```  
```FROM MENU_ITEMS```   
```GROUP BY ItemName, Quantity, CanteenID```  
```ORDER BY TotalUnitsSold DESC LIMIT 5;```   
2. Command 2
Get customer spending analysis (total spend).  
```SELECT c.CustomerID, c.Cname, SUM(o.TotalPrice) AS TotalSpent \```  
```FROM CUSTOMER AS c \```  
```LEFT JOIN ORDER_TABLE AS o \```  
```ON c.CustomerID = o.CustomerID \```  
```GROUP BY c.CustomerID, c.Cname \```  
```ORDER BY TotalSpent DESC;```  
3. Command 3
Get the total revenue for each canteen.   
```SELECT C.CanteenID, SUM(O.TotalPrice) AS TotalRevenue```  
```FROM CANTEEN C```  
```JOIN ORDER_TABLE O ON C.CanteenID = O.CanteenPlaced```  
```GROUP BY C.CanteenID;```  

### Modifications
#### Insertion
1. Command 1
Insert a new customer.  
```INSERT INTO CUSTOMER (CustomerID, Cname, CDOB, CustomerRole) VALUES (%s, %s, %s, %s);```
2. Command 2
Insert a new canteen.  
```INSERT INTO CANTEEN (CanteenID, OpeningYear, Location) VALUES (%s, %s, %s);```

#### Delete
1. Command 1
Delete a Staff Member.  
```DELETE STAFF, STAFF_DETAILS```  
```FROM STAFF```  
```LEFT JOIN STAFF_DETAILS ON STAFF.Aadhar = STAFF_DETAILS.Aadhar```  
```WHERE STAFF.StaffID = {staff_id};```  

2. Command 2
Delete a Customer.  
```DELETE FROM CUSTOMER WHERE CustomerID = {customer_id};```

#### Update
1. Command 1
Update the price of a menu item.  
```UPDATE MENU_ITEMS SET Price = %s WHERE ItemName = %s;```
2. Command 2
Update the dependent of a staff member.  
```UPDATE STAFF SET CanID = %s WHERE StaffID = %s;```

