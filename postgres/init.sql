CREATE USER flasker;
CREATE DATABASE flaskdb;
GRANT ALL PRIVILEGES ON DATABASE flaskdb TO flasker;
ALTER USER flasker with PASSWORD 'qaz';
ALTER DATABASE flaskdb OWNER TO flasker;