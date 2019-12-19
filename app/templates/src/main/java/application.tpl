package com.loki.user;

import com.loki.common.config.AuditConfiguration;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Import;

@Import({AuditConfiguration.class})
@SpringBootApplication
public class {{data.name}}Application {

    public static void main(String[] args) {
        SpringApplication.run(UserServiceApplication.class, args);
    }

}
