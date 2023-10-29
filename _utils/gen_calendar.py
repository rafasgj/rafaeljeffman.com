"""create base for class plan"""

import sys
import yaml
import textwrap
from datetime import datetime, timedelta


def get_date(start, end, weekday):
    nextweek = timedelta(7)
    day = start + timedelta(weekday - start.weekday())
    while day < end:
        yield day
        day += nextweek


if len(sys.argv) < 5:
    print("usage: calendar.py DAY_OF_WEEK FROM TO TITLE")
    print("\n\tDAY_OF_WEEK\tMON, TUE, WED, THU, FRI, SAT, SUN")
    print("\tFROM\tStart day YYYY-MM-DD")
    print("\tTO\tEnd day: YYYY-MM-DD")
    sys.exit(1)

WEEKDAYS = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

HOLIDAYS = {}
if len(sys.argv) == 6:
    with open(sys.argv[5], "rt") as holidays:
        HOLIDAYS = {
            datetime.strptime(item["date"], "%Y-%m-%d"): [item["reason"]]
            for item in yaml.safe_load(holidays)
        }

target = WEEKDAYS.index(sys.argv[1])
start = datetime.strptime(sys.argv[2], "%Y-%m-%d")
end = datetime.strptime(sys.argv[3], "%Y-%m-%d")
title = sys.argv[4]

year = start.year
semester = 1 if start.month <= 7 else 2

preset_topics = {
    0: ["Apresentação da disciplina", "Revisão de conceitos básicos"],
    9: ["Prova **P1**"],
    -1: ["Substituição de grau"],
    -2: ["Divulgação de Resultados", "Revisão para a substituição de grau"],
    -3: ["Prova **P2**"],
}

base = {
    "title": title,
}

dates = list(get_date(start, end, target))
daycount = len(dates)

data = {
    "section": "LaSalle",
    "subtitle": f"Unilasalle - {year}/{semester}",
    "sections": [],
    "objectives": [],
    "requirements": [],
    "learning_units": [],
    "competences": [],
    "grading": {
        "g1": [
            {"label": "T1", "weight": 3.0},
            {"label": "E1", "weight": 3.0},
            {"label": "P1", "weight": 4.0},
        ],
        "g2": [
            {"label": "T2", "weight": 3.0},
            {"label": "E2", "weight": 3.0},
            {"label": "P2", "weight": 4.0},
        ],
    },
    "resources": {"online": [], "tools": [], "bibliography": []},
    "layout": "classplan",
    "year": int(year),
    "semester": int(semester),
    "strategy": "".join(
        textwrap.dedent(
            """
        Serão utilizadas aulas expositivas, exercícios práticos
        individuais ou em grupo, pesquisas e apresentação de conteúdos
        relacionados a disciplina.
        """
        ).splitlines()
    ),
    "calendar": [
        {
            "day": cal.strftime("%Y-%m-%d"),
            "lecture": cal not in HOLIDAYS,
            "topics": HOLIDAYS.get(cal)
            if cal in HOLIDAYS
            else preset_topics.get(i)
            if i in preset_topics
            else preset_topics.get(-1 * (daycount - i), [""]),
        }
        for i, cal in enumerate(dates)
    ],
}

data.update(base)

short_name = {
    "Linguagens Formais": "liguagens-formais",
    "Sistemas Distribuídos": "sistemas-distribuidos",
    "Complexidade de Algoritmos e Análise de Desempenho": "analise-algoritmos",
    "Compiladores": "compiladores",
}

# Create directories:
# - /teaching/lasalle/{year}/{semester}
# - /teaching/lasalle/{year}/{semester}/lectures/{short-name}
#
# Save data to "/teaching/lasalle/{year}/{semester}/{short-name}.md

print("---")
print(
    yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=78),
    end="---\n\n",
)
