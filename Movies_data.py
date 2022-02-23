
import sqlite3
conn =sqlite3.connect("mov.db")


conn.execute('create table Movies(id int primary key,name text not null,actor text not null,actress text not null,director text not null,release_year int)')
# User Input Data
m_name=input("Enter the Movie Name:")

m_actor=input("Enter the Actor Name:")
m_actress=input("Enter the Actress Name:")
m_director=input("Enter the Director Name:")
m_release_year=input("Enter the Release_year:")

#Insert In Database
conn.execute("insert into Movies (name,actor,actress,director,release_year) values(?,?,?,?,?)",(m_name,m_actor,m_actress,m_director,m_release_year))

conn.commit()
print("Show Data")
select_actor=input("Enter the Actor Name:")
All_Movie=conn.execute("select * from Movies where actor='%s',(select_actor)")
for row in All_Movie:
	print("name {},Actor Name {},Actress Name{},Director Name{},Release_year".format(row[0],row[1],row[2],row[3],row[4]))





