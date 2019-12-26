package {{base.package}}.core.repository;

import {{base.package}}.core.entity.{{data.entityName}}Entity;
import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface {{data.entityName}}EntityRepository extends PagingAndSortingRepository<{{data.entityName}}Entity, Long> {

}
