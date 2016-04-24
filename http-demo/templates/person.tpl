{% extends "index.tpl" %}
{% block body %}
<ul>
    {% for person in people %}
    <li>{{ person.first_name}} {{ person.last_name }}, ID: {{ person.id }}</li>
    {% else  %}
    <li> No people! </li>
    {% endfor %}
</ul>
{% endblock %}
