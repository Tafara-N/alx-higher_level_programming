-- A script that creates the MySQL server user user_0d_1
--  has all privileges on the said MySQL server
--  password is set to user_0d_1_pwd

SET GLOBAL validate_password.policy=LOW;
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost';
SET GLOBAL validate_password.policy=MEDIUM;
FLUSH PRIVILEGES;

