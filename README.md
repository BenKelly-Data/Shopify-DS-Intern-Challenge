# Shopify-DS-Intern_Challenge
A place to share my answers to Shopify's questions!


**1.**

a) When summary statistics like a mean seem odd, the first thing to check in the data is the prevalence of outliers. Aside from removing outliers to get a better understanding of most of the data, there are a few metrics that limit the influence of outliers.

b) If I were allowed to remove outliers (as I do in the .py file) I would present a corrected mean since that is what stakeholders are probably most familiar with. I would also mention the shops with shop_id 42 and 78 reporting much larger order values and either sell vastly different items or are experiencing some sort of error with recording sales. However, if the outliers were to be included, I would present the median, though an argument could be made for the very similar geometric mean. 

c) The median average order value is $284, and the mean with outliers removed is $302.58 (median is identical). 


**2.**

a) 
SELECT Orders.ShipperID, COUNT(Orders.ShipperID), Shippers.ShipperName

FROM Orders

LEFT JOIN Shippers WHERE Orders.ShipperID = Shippers.ShipperID

GROUP BY Orders.ShipperID;

Speedy Express shipped 54 orders in total.

b)
SELECT Orders.EmployeeID, COUNT(Orders.EmployeeID) as Tally, Employees.LastName
FROM Orders
LEFT JOIN Employees ON Orders.EmployeeID=Employees.EmployeeID
GROUP BY Orders.EmployeeID
ORDER BY Tally DESC;

Peacock had the most orders at 40.

c)
WITH cust AS (SELECT CustomerID,Country FROM Customers WHERE Country='Germany') 
SELECT OrderDetails.ProductID, SUM(Quantity) AS Tally
FROM   cust JOIN Orders ON cust.CustomerID = Orders.CustomerID
JOIN OrderDetails ON OrderDetails.OrderID = Orders.OrderID
GROUP BY ProductID
ORDER BY Tally DESC;

ProductID 40 sold the most units at 160 in Germany.
