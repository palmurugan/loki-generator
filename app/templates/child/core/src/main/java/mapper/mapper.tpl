package {{base.package}}.core.mapper;

import com.loki.common.mapper.GenericMapper;
import {{base.package}}.core.entity.{{data.entityName}}Entity;
import {{base.package}}.dto.{{data.entityName}}DTO;
import org.mapstruct.Mapper;

@Mapper(componentModel = "spring")
public interface {{data.entityName}}Mapper extends GenericMapper<{{data.entityName}}DTO, {{data.entityName}}Entity> {

}
