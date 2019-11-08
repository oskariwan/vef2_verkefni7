{% extends "base-karfa.html" %}
{% block title %} yfirlit pönturnar {% endblock %}

{% block content %}
    <h3>{{ self.title() }}</h3>
    <div>
        <table>
            <tr>
                <td>
                    Nafn:
                </td>
                <th>
                    {{ name }}
                </th>
            </tr>
            <tr>
                <td>
                    tölvupóst:
                </td>
                <th>
                    {{ email }}
                </th>
            </tr>
            <tr>
                <td>
                    símanúmer
                </td>
                <th>
                    {{ phone }}
                </th>
            </tr>
            <tr>
                    <td>
                        heildarverð
                    </td>
                    <th>
                        {{ price }}
                    </th>
                </tr>
                <tr>
                    <td>
                        <a href="/karfa" class="butt">aftur í körfuna</a>
                    </td>
                    <td>
                        <a href="/logout" class="butt">útskráning</a>
                    </td>
                </tr>
        </table>
    </div>
{% endblock %}