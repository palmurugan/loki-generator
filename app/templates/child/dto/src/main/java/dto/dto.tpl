{%- macro sentence_case(text) %}{{ text[0]|upper}}{{text[1:] }}{% endmacro -%}
package {{base.package}}.dto;

import com.loki.common.dto.BaseDTO;

public class {{data.entityName}}DTO extends BaseDTO {

    {%- for attribute in data.attributes %}
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
