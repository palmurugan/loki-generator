package {{base.package}}.core.service.impl;

import com.loki.common.service.impl.GenericService;
import {{base.package}}.core.entity.{{data.entityName}}Entity;
import {{base.package}}.dto.{{data.entityName}}DTO;
import {{base.package}}.core.mapper.{{data.entityName}}Mapper;
import {{base.package}}.core.repository.{{data.entityName}}EntityRepository;
import {{base.package}}.core.service.{{data.entityName}}Service;
import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Service;

@Service
public class {{data.entityName}}ServiceImpl extends GenericService<{{data.entityName}}DTO, {{data.entityName}}Entity, Long> implements {{data.entityName}}Service {

    private {{data.entityName}}EntityRepository repository;

    private {{data.entityName}}Mapper mapper;

    public {{data.entityName}}ServiceImpl({{data.entityName}}EntityRepository repository, {{data.entityName}}Mapper mapper) {
        super(repository, mapper);
    }
}
