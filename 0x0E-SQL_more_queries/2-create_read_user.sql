-- Create user and table
CREATE DATABASE hbtn_0d_2;
CREATE USER 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
