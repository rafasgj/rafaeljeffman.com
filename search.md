---
title: Procura
layout: section
lang: pt
sections: []
---

<div id="#search">
    <form id="search-form" action="/search" method="get">
        <input id="search-input" class="search-input" type="text" name="search" placeholder="Procura" />
        <input type="hidden" name="lang" value="{{ page.lang }}" />
        <button id="search-submit"><span class="fa fa-search"></span></button>
    </form>
</div>

## Resultados da Procura

{% include search_code.html %}
