# Creating the tables 

```sql
CREATE TABLE swimmers(s_id integer autoincrement primary key, 
firstname varchar(40), 
lastname varchar(40),
jcclass varchar(20),
hometown varchar(100),
school_district varchar(200),
email varchar(100),
roster varchar(20)
);

CREATE TABLE meets(m_id integer autoincrement primary key, 
meet_location varchar(200), 
meet_type varchar(40),
meet_date varchar(20),
meet_time varchar(20),
landmarkconf varchar(20)
);

CREATE TABLE events(e_id integer autoincrement primary key, 
event_name varchar(200),
event_type varchar(40),
event_order integer
);

CREATE TABLE swimmerstats(id integer autoincrement primary key, 
s_id references swimmers(id),
m_id references meets(id),
e_id references events(id),
tm_minutes integer,
tm_seconds integer,
tm_hundredth_seconds integer,
meet_place varchar(20)
);

```
# Joining tables 
