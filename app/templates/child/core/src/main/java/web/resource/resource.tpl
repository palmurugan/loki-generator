package {{base.package}}.core.web.resource;

import com.loki.common.web.resource.BaseRestResource;
import {{base.package}}.dto.{{data.entityName}}DTO;
import {{base.package}}.core.service.{{data.entityName}}Service;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.inject.Inject;

@RestController
@RequestMapping(value = "/{{data.entityName | lower}}")
public class {{data.entityName}}Resource extends BaseRestResource<{{data.entityName}}DTO, Long> {

    private {{data.entityName}}Service service;

    @Inject
    public {{data.entityName}}Resource({{data.entityName}}Service service) {
        super(service);
    }
}
