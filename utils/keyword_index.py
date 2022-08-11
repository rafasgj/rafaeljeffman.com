"""Map keyword to documents"""

import os
import yaml
import textwrap


def get_doc_keywords(filename, lang_code):
    with open(filename, "r") as doc:
        try:
            data = yaml.load_all(doc, Loader=yaml.FullLoader)
            front_matter = next(data) or {}
        except:
            front_matter = {}
    if front_matter.get("lang", "pt") == code:
        return (front_matter.get("tags"), front_matter.get("title"))
    return (None, None)


def add_keywords_to_index(filename, index, lang_code):
    tags, title = get_doc_keywords(filename, lang_code)
    for tag in tags or []:
        if "/" in tag:
            raise ValueError(f"Character '/' not valid in a tag. File: {filename}")
        doc_list = index.setdefault(tag.lower(), [])
        doc_list.append((os.path.splitext(filename)[0], title))


def process_directory(dirname, index, lang_code):
    for entry in os.scandir(dirname):
        if entry.name.startswith("index"):
            continue
        if entry.is_file() and os.path.splitext(entry.name)[1] == ".md":
            add_keywords_to_index(
                os.path.join(dirname, entry.name), index, lang_code
            )
        if entry.is_dir():
            process_directory(
                os.path.join(dirname, entry.name), index, lang_code
            )


try:
    os.mkdir("index")
except FileExistsError:
    pass

with open("index/index.md", "w") as output:
    print("---\ntitle: Tags\nlayout: section\n---\n", file=output)
    print(
        textwrap.dedent(
            """
        <style>
        ul > li > a {
            border-radius: 15px 15px;
            background-color: #d92;
            color: #f0f0f0;
            font-weight: bolder;
            text-align: center;
            padding: 5px;
            font-size: 16px;
            text-decoration: none;
            white-space: nowrap;
            line-height: 20px;
        }
        ul > li {
            list-style: none;
            display: inline-block;
            padding: 5px;
            margin: 5px auto;
            line-height: 20px;
        }
        ul {
            margin: 0 auto;
            text-align: center;
        }
        </style>
        """
        ),
        file=output,
    )
    for lang, code in (("Português", "pt"), ("English", "en")):
        index = {}
        process_directory(".", index, code)
        if index:
            print("\n##", lang, file=output)
        for key in sorted(index.keys()):
            filelist = index[key]
            key_link = key.replace(" ", "_")
            print(f"* [{key}]({key_link})", file=output)
            with open(f"index/{key_link}.md", "w") as keyout:
                print(
                    f'---\ntitle: Tag "{key}"\nlayout: main\n---\n', file=keyout
                )
                for filename, title in filelist:
                    print(
                        f"* [{title}](/{os.path.splitext(filename)[0]})",
                        file=keyout,
                    )
