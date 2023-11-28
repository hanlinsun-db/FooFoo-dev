-- Create a temporary table for the number of queries executed by each user
CREATE OR REPLACE TEMPORARY VIEW test AS
SELECT user_name, COUNT(*) AS num_queries
FROM system.query.history
WHERE start_time >= DATE_SUB(CURRENT_TIMESTAMP(), 14)
GROUP BY user_name;

-- Find the top # users users with the most queries executed
SELECT user_name, num_queries
FROM test
ORDER BY num_queries DESC
LIMIT ${limit_param};