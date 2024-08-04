SELECT 
    s.user_id,
    ROUND(
        COALESCE(
            NULLIF(
                SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) * 1.0 / NULLIF(COUNT(c.user_id), 0),
                0
            ),
            0
        ),
    2) AS confirmation_rate
FROM 
    Signups AS s
LEFT JOIN 
    Confirmations AS c
ON 
    s.user_id = c.user_id 
GROUP BY 
    s.user_id
ORDER BY 
    s.user_id;
