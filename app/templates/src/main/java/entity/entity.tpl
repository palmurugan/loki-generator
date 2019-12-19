package com.loki.user.domain;

import com.loki.common.model.Auditing;

import javax.persistence.*;

@Entity
@Table(name = "{{data.entityName | lower}}")
public class {{data.entityName}} extends Auditing<Long> {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id", unique = true, nullable = false)
    private Long id;

    {%- for attribute in data.attributes %}
    @Column(name = "{{attribute.name}}"{% if attribute.unique == 'true' %}, unique = true{% endif %}{% if attribute.nullable == 'true' %}, nullable = true{% endif %})
    private {{attribute.type}} {{attribute.name}};
    {% endfor %}
}
