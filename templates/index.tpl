{% extends "base.html"%}

{% block title %}<title>vefverslun</title>{% endblock %}

{% block head %}
    {{ super() }}
    <style type="text/css">
    .important { color: #369; }
    </style>
    {% endblock %}

    {% block content %}
        <h1 class="litur">vörur:</h1>
        <section class="rapper">
            {% for i in v %}
                <div>
                    <h2>
                        {{ i[1] }}
                    </h2>
                    <img src="/static/{{ i[2] }}">
                    <h2>verð: <a href="/add/{{i[0]}}">{{i[3]}}</a></h2>
                </div>
            {% endfor %}
        </section>
    {% endblock %}