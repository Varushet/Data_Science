--1
SELECT * 
FROM customers
WHERE country = "Brazil";

--2
SELECT *
FROM employees
WHERE title = "Sales Support Agent";

--3
select *
from tracks
where Composer = 'AC/DC'

--4
select CustomerId, FirstName, LastName, Country
from customers
where Country != 'USA'

--5
SELECT FirstName || " " || LastName as FullName,
City || ", " || State || ", " || Country as Location,
Email
FROM employees
WHERE Title = "Sales Support Agent";

--6
select distinct BillingCountry
from invoices

--7
select State, count(CustomerId) as N_Clients
from customers
group by state

--8
select InvoiceId, count(InvoiceId) as N_Articles
from invoice_items
where InvoiceId in (37)

--9
select Composer, count(Composer) as N_Song
from tracks
where Composer in ('AC/DC')

--10
select InvoiceId, count(InvoiceId) as N_Articles
from invoice_items
group by InvoiceId

--11
select InvoiceId, BillingCountry, count(BillingCountry) as N_Country
from invoices
group by BillingCountry

--12
select strftime('%Y', InvoiceDate) as Anno, count(BillingCountry)
from invoices
where Anno in ('2009', '2011')
GROUP BY Anno

--13
select strftime('%Y', InvoiceDate) as Anno, count(BillingCountry)
from invoices
where Anno between '2009' and '2011'
GROUP BY Anno

--14
select country, count(country) as N_Customer
from customers
WHERE country IN ("Spain","Brazil")

--15
select Name
from tracks t 
where name like "You%"

--SEGUNDA PARTE--

--1
select
c.firstname || " " || c.lastname as FullName,
i.InvoiceId,
i.InvoiceDate,
i.BillingCountry 
from invoices as i
inner join customers as c on i.customerid = c.CustomerId 
where Country = "Brazil"

--2
select 
e.FirstName || " " || e.LastName as FullName,
i.InvoiceId
from employees e
inner join invoices i on e.Title = "Sales Support Agent"

--3
SELECT
c.firstname || " " || c.lastname AS ClientName,
c.country AS ClientCountry,
e.firstname || " " || e.lastname AS EmployeeName,
SUM(i.total) as Total
FROM invoices i
INNER JOIN customers c ON i.customerid = c.customerid
INNER JOIN employees e ON c.supportrepid = e.employeeid
GROUP BY ClientName 


--4
SELECT i.invoiceid,
i.trackid,
t.name AS SongName
FROM invoice_items i
INNER JOIN tracks t ON i.trackid = t.trackid

--5
SELECT
t.Name,
m.Name,
a.title,
g.Name
FROM tracks t
INNER JOIN albums a ON t.albumid = a.albumid
INNER JOIN genres g ON t.genreid = g.GenreId
INNER JOIN media_types m ON t.MediaTypeId = m.MediaTypeId

--6
SELECT
pt.playlistid,
p.name AS PlaylistName,
COUNT(pt.trackid) as N_Songs
FROM playlist_track pt
INNER JOIN playlists p ON p.PlaylistId = pt.playlistid
GROUP BY p.PlaylistId 

--7
SELECT
e.firstname || " " || e.lastname AS FullName,
SUM(i.total) as TotalSales
FROM invoices i
INNER JOIN customers c ON i.customerid = c.customerid
INNER JOIN employees e ON c.supportrepid = e.employeeid
GROUP BY FullName

--8
SELECT
e.firstname || " " || e.lastname AS EmployeeName,
SUM(i.total)
FROM invoices i
INNER JOIN customers c ON i.customerid = c.customerid
INNER JOIN employees e ON c.supportrepid = e.employeeid
WHERE strftime("%Y", i.invoicedate) = "2009"
GROUP BY EmployeeName

--9
SELECT
ar.artistid,
ar.Name as ArtistName,
SUM(i.total) AS TotalSales
FROM invoices i
INNER JOIN invoice_items ii ON i.invoiceid = ii.invoiceid
INNER JOIN tracks t ON ii.trackid = t.trackid
INNER JOIN albums a ON t.albumid = a.albumid
INNER JOIN artists ar ON a.artistid = ar.ArtistId
GROUP BY a.ArtistId
ORDER BY TotalSales DESC
LIMIT 3