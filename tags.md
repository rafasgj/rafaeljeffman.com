---
title: Tags
layout: section
sections: []
---
{% assign page_list = site.pages | where_exp: "item", "item.title != nil" | where_exp: "item", "item.date != nil" | where_exp: "item", "item.tags != nil" | sort: "date" | reverse  %}

<ul class="tags">
{% assign page_tags = page_list | map: "tags" | join: ", " | downcase | split: ", " | sort_natural | uniq %}
{% for tag in page_tags %}
<li><a href="javascript:filter_tag('{{ tag | downcase | replace: " ", "-" | prepend: "data-" }}')" class="page-tags">{{ tag }}</a></li>
{% endfor %}
</ul>

<ul class="target-pages">
{% for linkto in page_list %}
  <li{% for tag in linkto.tags %} {{ tag | downcase | replace: " ", "-" | prepend: "data-" }}{% endfor %}>
     <div id="post_title">
        <a href="{{ linkto.url }}">{{ linkto.title | strip | markdownify | remove: '<p>' | remove: '</p>' }}</a> <div class="last-update">{{ linkto.date }}</div> {% if linkto.lang %}<div class="lang-code">({{ linkto.lang }})</div>{% endif %}
    </div>
     {% if linkto.abstract %}<div id="abstract">{{ linkto.abstract | markdownify | remove: "<p>" | remove: "</p>" }}</div>{% endif %}
     <div style="margin-bottom: 15px; margin-right: 5em; text-align:right">{% for t in linkto.tags %}<span class="page-tags" style="font-size:16px !important">{{ t }}</span>{% endfor %}</div>
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
