package {{base.package}}.service.impl;

import com.loki.common.service.impl.GenericService;
import {{base.package}}.entity.{{data.entityName}}Entity;
import {{base.package}}.repository.{{data.entityName}}EntityRepository;
import {{base.package}}.service.{{data.entityName}}Service;
import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Service;

@Service
public class {{data.entityName}}ServiceImpl extends GenericService<{{data.entityName}}Entity, Long> implements {{data.entityName}}Service {

    private {{data.entityName}}EntityRepository repository;

    public {{data.entityName}}ServiceImpl({{data.entityName}}EntityRepository repository) {
        super(repository);
    }
}
