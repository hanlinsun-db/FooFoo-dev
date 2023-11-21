# Databricks notebook source
# MAGIC %sql
# MAGIC -- Create a temporary table for the number of queries executed by each user
# MAGIC CREATE OR REPLACE TEMPORARY VIEW user_durations AS
# MAGIC SELECT user_name, COUNT(*) AS num_queries
# MAGIC FROM system.query.history
# MAGIC WHERE start_time >= DATE_SUB(CURRENT_TIMESTAMP(), ${test})
# MAGIC GROUP BY user_name;
# MAGIC
# MAGIC -- Create a parameterized SQL statement with a named parameter for the limit number
# MAGIC SELECT user_name, num_queries
# MAGIC FROM user_durations
# MAGIC ORDER BY num_queries DESC
# MAGIC LIMIT ${limit};

# COMMAND ----------

dbutils.widgets.text("limit", "")
dbutils.widgets.text("test", "")
