<?xml version="1.0"?>
<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"
         xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>{{data.package}}</groupId>
        <artifactId>{{data.artifactId}}</artifactId>
        <version>0.0.1-SNAPSHOT</version>
    </parent>
    <groupId>{{data.package}}.dto</groupId>
    <artifactId>{{data.artifactId}}-dto</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>{{data.artifactId}}-dto</name>
    <url>http://maven.apache.org</url>

    <properties>
        <validation-api.version>2.0.1.Final</validation-api.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>javax.validation</groupId>
            <artifactId>validation-api</artifactId>
            <version>${validation-api.version}</version>
        </dependency>
        <dependency>
            <groupId>com.loki.common</groupId>
            <artifactId>common-service</artifactId>
        </dependency>
    </dependencies>
</project>
