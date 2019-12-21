package {{base.package}}.repository;

import {{base.package}}.entity.{{data.entityName}}Entity;
import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface {{data.entityName}}EntityRepository extends PagingAndSortingRepository<{{data.entityName}}Entity, Long> {

}
