{% extends "base-karfa.html" %}

{% block title %}
    vefverslun - innkaupakarfan
{% endblock %}

{% block content %}
    <div>
    {% if tom %}
        <h1> karfan er tóm</h1>
    {% else %}
    <h1> vörur í körfu: </h1>
    <h3><a href="/eyda">eyða körfu </a></h3>
    <table>
        <tr>
            <th colspan="2"> smelltu á vöru til að eyða úr körfuni </th>
        </tr>
        <tr>
            <td>vara:</td>
            <th>verð:</th>
        </tr>
    {% for i in k %}
        <tr>
            <td><a href="/eydavoru/{{ i[0] }}">{{ i[1]}}</a><td>
            <td><b> {{ i[3] }}</b></td>
        </tr>
    {% endfor %}
        <tr>
            <td> samtals: </td>
            <th> {{ samtals }} </th>
        </tr>
    </table>
    {% endif %}
    <form method="post" action="/result">
        <h3>viðskiptavinur</h3>
        <label>nafn:
            <input type="text" name="nafn" required placeholder="Name">
        </label>
        <label>tolvupost
            <input type="email" name="email" required placeholder="E-mail">
        </label>
        <label>símanúmer:
            <input type="text" name="simi" required pattern="^(354 )?\d{3}[ -]?\d[4]$" placeholder="1234567">
        </label>
        <input type="hidden" name="samtals" value="{{samtals}}">
        <input type="submit" value="kaupa vörur">
    </form>
    </div>
    <div class="ok"><a href="/">aftur i vörulistann</a></div> 
    {% endblock%}
           



        
        

