# Creating the tables 

```sql
CREATE OR REPLACE TABLE swimmers(s_id integer primary key, 
firstname varchar(40), 
lastname varchar(40),
jcclass varchar(20),
hometown varchar(100),
school_district varchar(200),
email varchar(100),
roster varchar(20)
);
create sequence swimmerid start 10;

CREATE OR REPLACE TABLE meets(m_id integer primary key, 
meet_location varchar(200), 
meet_type varchar(40),
meet_date varchar(20),
meet_time varchar(20),
landmarkconf varchar(20)
);
create sequence meetid start 100;

CREATE OR REPLACE TABLE events(e_id integer primary key, 
event_name varchar(200),
event_type varchar(40),
event_order integer
);
create sequence eventid start 1000;

CREATE OR REPLACE TABLE swimmerstats(id integer primary key, 
s_id integer,
m_id integer,
e_id integer,
tm_minutes integer,
tm_seconds integer,
tm_hundredth_seconds integer,
meet_place varchar(20),
FOREIGN KEY (s_id) references swimmers(s_id),
FOREIGN KEY (m_id) references meets(m_id),
FOREIGN KEY (e_id) references events(e_id),
);
create sequence sstatid start 1; 
```
# Inserting Data

```sql
/* Swimmers Table */
insert into swimmers values(nextval('swimmerid'),'Betty','Backstroker','FR','Huntingdon,PA','Huntingdon Area','betty@swim.cc','women');

```
# Joining tables 
