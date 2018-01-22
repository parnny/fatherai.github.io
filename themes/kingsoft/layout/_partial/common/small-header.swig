<!-- 页头 -->
<header class="page__small-header page__header--small">
    <nav class="page__navbar">
        <div class="page__container navbar-container">
            <a class="page__logo" href="{{ url_for('/') }}" title="{{ get_setting('title') }}" alt="{{ get_setting('title') }}">
                <img src="{{ get_setting('logo') }}" alt="{{ get_setting('title') }}">
            </a>

            <nav class="page__nav">
                <ul class="nav__list clearfix">
                    {% for item in get_setting('menu') %}
                        {% set name = __('menu.' + loop.key) %}
                        {% set link = item %}
                        {% set icon = null %}
                        
                        {% if item.name.length > 1 %}
                            {% set name = item.name %}
                        {% endif %}
                        {% if item.link.length > 1 %}
                            {% set link = item.link %}
                        {% endif %}
                        {% if item.icon.length > 1 %}
                            {% set icon = item.icon %}
                        {% endif %}
                        <li class="nav__item">
                            <a href="{{ link }}" alt="{{ name }}" title="{{ name }}">
                                {% if icon != null %}
                                    <i class="iconfont {{ icon }}" style="font-size:32px"></i>
                                {% else %}
                                    {{ name }}
                                {% endif %}
                            </a>
                        </li>
                    {% endfor %}
                </ul>
            </nav>

            <button class="page__menu-btn" type="button">
                <i class="iconfont icon-menu"></i>
            </button>
        </div>
    </nav>
</header>