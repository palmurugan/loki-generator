## server port info
server.port=8080

## default connection pool
spring.datasource.hikari.connectionTimeout=20000
spring.datasource.hikari.maximumPoolSize=5

## PostgreSQL
spring.datasource.url=jdbc:postgresql://localhost:5432/test
spring.datasource.username=root
spring.datasource.password=root

#drop n create table again, good for testing, comment this in production
spring.jpa.hibernate.ddl-auto=create