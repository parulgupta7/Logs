-- Droping already existing views with same names
DROP VIEW IF EXISTS author_view CASCADE;
DROP VIEW IF EXISTS author_view1 CASCADE;
DROP VIEW IF EXISTS author_view2 CASCADE;
DROP VIEW IF EXISTS author_view3 CASCADE;
DROP VIEW IF EXISTS error_view1 CASCADE;
DROP VIEW IF EXISTS error_view2 CASCADE;
DROP VIEW IF EXISTS error_view3 CASCADE;

-- Connect to news database
\c news;

-- Views required for implementation
create view author_view as select title,count(title) as views from log,articles where path=concat('/article/',articles.slug) group by title order by views desc;
create view author_view1 as select authors.id, articles.title from authors, articles where articles.author = authors.id;
create view author_view2 as select author_view1.id, author_view1.title, author_view.views from author_view1, author_view where author_view1.title = author_view.title;
create view error_view1 as select time::timestamp::date, count(status) as total from log group by time::timestamp::date order by time::timestamp::date;
create view error_view2 as select time::timestamp::date, count(status) as fault from log where status = '404 NOT FOUND' group by time::timestamp::date;
create view error_view3 as select error_view1.time, (fault::float * 100)/( total::float) as error_percent from error_view1, error_view2 where error_view1.time = error_view2.time;


