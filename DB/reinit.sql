\encoding UTF8

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

\i init.sql
\i seed_from_json.sql
