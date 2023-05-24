{% extends 'flatpages/default.html' %}
{% load censor_filter %}
{% block title %}
<tr><h3> Всего News = {{ news|length }}</h3></tr>
{% endblock title %}
{% block content %}
<h1 class="text-center">Новости<span class="text- fs-6 fst-normal" >Всего публикаций:{{ page_obj.paginator.count }}</span></h1>
{% if is_not_subscriber %}
    <p class="text-center"><a href="{}"class="btn btn-secondary btn-sm">Подписаться</a> </p>
{% endif %}
<hr>
<ul class="list-group list-group-flush">
    {% for newspost in category_list %}
    <li class="list-group-item">
        <small class="fw-bold">{{ newspost.date|'d m y' }}</small>
        <a href="{%url 'news_edit' newspost.id %}">{{ new.post.title }}</a>
        <small class="text-muted">(Автор:-{{ newspost.author }})</small><br>
        <small class="fw-bold"> Категории:
            {% for category in newspost.category.all %}
                <a href="{% url"category_list" category.id %}" {{ category }}
            {% endfor %}
        </small>
        <p>{{ newspost.text|truncatechars:216 }}</p>
    </li>
{% endfor %}
</ul>

{% if is_paginated %}
<nav aria-label="...">
    <ul class="pagination pagination-sm justify-content-center">
    {% if page_obj.has_previous %}
        <li class="page-item"><a class="page-link" href="?page=1">Начало></a></li>
        <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}"><<<</a></li>

    {% endif %}


    {% for num in page_obj.paginator.page_range %}
        {% if page_obj.number == num %}
             <li class="page-item active"><a class="page-link">{{ num }}</a></li>
        {% elif num > page_obj.number|add:"-3" and num < page_obj.number|add:"3"  %}
             <li class="page-item"><a class="page-link" href="?page={{ num }}">{{ num }}</a></li>
        {% endif %}
    {% endfor %}

    {% if page_obj.has_next %}
        <li class="page-item"><a class="page-link " href="?page={{ page_obj.next_page_number }}">>>></a></li>
        <li class="page-item"><a class="page-link " href="?page={{ page_obj.paginator.num_pages }}">Конец</a></li>
    {% endif %}
</ul>
<nav>
{% endif %}
{% endblock content %}





