-- 14.1 Query a list of tenants who are renting more than one apartment
SELECT TenantName
FROM Tenants 
INNER JOIN
	(SELECT TenantID FROM AptTenants GROUP BY TenantID HAVING count(*) > 1) C
ON Tenants.TenantID = C.TenantID

-- 14.2. Query a list of all buildings and the number of open requests
SELECT BuildingName, ISNULL(Count, 0) as 'Count'
FROM Buildings
LEFT JOIN 
	(SELECT Apartments.BuildingID, count(*) as 'Count'
	FROM Requests INNER JOIN Apartments
	ON Requests.AptID = Apartments.AptID
	WHERE Requests.Status = 'OPEN'
	GROUP BY Apartments.BuildingID) ReqCounts
ON ReqCounts.BuildingID = Buildings.BuildingID
	