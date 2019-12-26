{%- macro sentence_case(text) %}{{ text[0]|upper}}{{text[1:] }}{% endmacro -%}
package {{base.package}}.core.entity;

import com.loki.common.entity.BaseEntity;

import javax.persistence.*;

@Entity
@Table(name = "{{data.entityName | lower}}")
public class {{data.entityName}}Entity extends BaseEntity {

    {%- for attribute in data.attributes %}
    @Column(name = "{{attribute.name | lower}}"{% if attribute.unique == 'true' %}, unique = true{% endif %}{% if attribute.nullable == 'true' %}, nullable = true{% endif %})
    private {{attribute.type}} {{attribute.name}};
    {% endfor %}

    {%- for attribute in data.attributes %}
    public {{attribute.type}} get{{sentence_case(attribute.name)}}() {
        return {{attribute.name}};
    }

    public void set{{sentence_case(attribute.name)}}({{attribute.type}} {{attribute.name}}) {
        this.{{attribute.name}} = {{attribute.name}};
    }
    {% endfor %}
}
