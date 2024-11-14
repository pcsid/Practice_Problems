SELECT C.mac_address, COUNT(S.title) AS streams, SUM(S.traffic) AS total_traffic
FROM clients C
INNER JOIN streams S ON C.id = S.client_id
WHERE S.quality <> "240p" AND S.quality <> "360p" AND S.quality <> "480p" 
GROUP BY C.mac_address
ORDER BY total_traffic DESC;