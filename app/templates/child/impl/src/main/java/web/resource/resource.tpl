package {{base.package}}.impl.web.resource;

import {{base.package}}.impl.service.{{data.entityName}}ServiceExt;
import org.springframework.web.bind.annotation.RestController;

import javax.inject.Inject;

@RestController
public class {{data.entityName}}ResourceExt {

    private {{data.entityName}}ServiceExt service;

    @Inject
    public {{data.entityName}}ResourceExt({{data.entityName}}ServiceExt service) {
        this.service = service;
    }
}
