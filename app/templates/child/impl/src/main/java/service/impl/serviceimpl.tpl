package {{base.package}}.impl.service.impl;

import {{base.package}}.impl.service.{{data.entityName}}ServiceExt;
import {{base.package}}.impl.repository.{{data.entityName}}EntityRepositoryExt;
import org.springframework.stereotype.Service;

import javax.inject.Inject;

@Service
public class {{data.entityName}}ServiceImplExt implements {{data.entityName}}ServiceExt {

    private {{data.entityName}}EntityRepositoryExt repository;

    @Inject
    public {{data.entityName}}ServiceImplExt({{data.entityName}}EntityRepositoryExt repository) {
        this.repository = repository;
    }
}
