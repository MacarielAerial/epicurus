from bs4 import Tag


def find_tag_title(tag: Tag) -> bool:
    if all([tag.name == "h1", "class" in tag.attrs, "id" in tag.attrs]):
        if all(
            [
                tag["class"] == ["documentTitle", "truncatedDocumentTitle"],
                tag["id"] == "documentTitle",
            ]
        ):
            return True
        else:
            return False
    else:
        return False


def find_tag_body(tag: Tag) -> bool:
    if all([tag.name == "text", "htmlcontent" in tag.attrs, "wordcount" in tag.attrs]):
        if tag["htmlcontent"] == "true":
            return True
        else:
            return False
    else:
        return False


def find_tag_non_null_paragraph(tag: Tag) -> bool:
    if tag.name == "p":
        if len(tag.text) != 0:
            return True
        else:
            return False
    else:
        return False
