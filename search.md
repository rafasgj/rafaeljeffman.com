---
title: Pesquisa
layout: section
lang: pt
---

<div id="#search">
    <form id="search-form" action="/search" method="get">
        <input id="search-input" class="search-input" type="text" name="search" placeholder="Pesquisa" />
        <input type="hidden" name="lang" value="{{ page.lang }}" />
        <button id="search-submit"><span class="fa fa-search"></span></button>
    </form>
</div>

## Resultados da Pesquisa

{% include search_code.html %}
