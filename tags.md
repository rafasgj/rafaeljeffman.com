---
title: Tags
layout: section
sections: []
---

<style>
.page-tags {
    border-radius: 25px 5px;
    color: #f0f0f0;
    background-color: #a39;
    font-weight: bolder;
    text-align: center;
    padding: 5px 15px;
    margin: 3px 0px;
    font-size: 20px;
    text-decoration: none;
    white-space: nowrap;
    line-height: 20px;
    font-family: "Yanone Kaffeesatz";
    font-weight: 600;
}

ul.tags > li {
    list-style: none;
    display: inline-block;
    margin: 7px auto;
    line-height: 20px;
}

ul.tags {
    margin: 0 auto;
    text-align: center;
    margin: 0;
    padding: 20px;
    border: #555 solid thin;
}

ul.target-pages > li {
    list-style: none;
    margin-bottom: 10px;
}
</style>

{% assign page_list = site.pages | where_exp: "item", "item.title != nil" | where_exp: "item", "item.date != nil" | where_exp: "item", "item.layout != 'section'" | where_exp: "item", "item.tags != nil" | sort: "date" | reverse  %}

<ul class="tags">
{% assign page_tags = page_list | map: "tags" | join: ", " | downcase | split: ", " | sort | uniq %}
{% for tag in page_tags %}
<li><a href="javascript:filter_tag('{{ tag | downcase | replace: " ", "-" | prepend: "data-" }}')" class="page-tags">{{ tag }}</a></li>
{% endfor %}
</ul>

<ul class="target-pages">
{% for linkto in page_list %}
  <li{% for tag in linkto.tags %} {{ tag | downcase | replace: " ", "-" | prepend: "data-" }}{% endfor %}>
     <a href="{{ linkto.url }}">{{ linkto.title | strip | markdownify | remove: '<p>' | remove: '</p>' }}</a>
     <div id="last-update">{{ linkto.date }}</div>
     {% if linkto.lang %}<div id="lang-code">({{ linkto.lang }})</div>{% endif %}<div style="margin-bottom: 5px; margin-left: 1em;">{% for t in linkto.tags %}<span class="page-tags">{{ t }}</span>{% endfor %}</div>
  </li>
{% endfor %}

</ul>

<script>
function filter_tag(tag) {
    $(`.target-pages > li`).hide()
    $(`.target-pages > li[${tag}]`).show()
}

$('.target-pages > li').hide()
</script>
