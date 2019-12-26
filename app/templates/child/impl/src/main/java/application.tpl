package {{base.package}};

import com.loki.common.config.AuditConfiguration;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Import;

@Import({AuditConfiguration.class})
@SpringBootApplication
public class {{data.name}}Application extends SpringBootServletInitializer {

    public static void main(String[] args) {
        SpringApplication.run({{data.name}}Application.class, args);
    }

}
