from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import List

import bs4
import dacite
import orjson
from bs4 import Tag

from epicurus.nodes.html_parsing import (
    find_tag_body,
    find_tag_non_null_paragraph,
    find_tag_title,
)

logger = logging.getLogger(__name__)


@dataclass
class HTMLContent:
    title: str
    body: str
    paragraphs: List[str]

    @classmethod
    def from_str_html(cls, str_html: str) -> HTMLContent:
        soup = bs4.BeautifulSoup(str_html, "html.parser")

        tag_title = soup.find(find_tag_title)

        if not isinstance(tag_title, Tag):
            raise TypeError
        else:
            title = tag_title.text

        tag_body = soup.find(find_tag_body)

        if not isinstance(tag_body, Tag):
            raise TypeError
        else:
            body = tag_body.text

        tags_paragraph = tag_body.find_all(find_tag_non_null_paragraph)

        paragraphs: List[str] = []
        for tag_paragraph in tags_paragraph:
            if not isinstance(tag_paragraph, Tag):
                raise TypeError
            else:
                paragraphs.append(tag_paragraph.text)

        html_content = cls(title=title, body=body, paragraphs=paragraphs)

        return html_content

    @classmethod
    def from_path_html(cls, path_html_content: Path) -> HTMLContent:
        with open(path_html_content, "r") as f:
            str_html_content = f.read()

            return cls.from_str_html(str_html=str_html_content)


@dataclass
class HTMLsContent:
    content: List[HTMLContent]

    @classmethod
    def from_strs_html(cls, strs_html: List[str]) -> HTMLsContent:
        logger.debug(
            f"Parsing {HTMLContent} objects from " f"{len(strs_html)} HTML strings"
        )

        content: List[HTMLContent] = [
            HTMLContent.from_str_html(str_html=str_html_content)
            for str_html_content in strs_html
        ]

        htmls_content = HTMLsContent(content=content)

        return htmls_content

    @classmethod
    def from_paths_html(cls, paths_html: List[Path]) -> HTMLsContent:
        logger.debug(f"Reading strings from {len(paths_html)} HTML files")

        strs_html: List[str] = []
        for path_html in paths_html:
            with open(path_html, "r") as f:
                str_html = f.read()

                strs_html.append(str_html)

        htmls_content = HTMLsContent.from_strs_html(strs_html=strs_html)

        return htmls_content

    @classmethod
    def from_dir_html(cls, path_dir_html: Path) -> HTMLsContent:
        paths_html: List[Path] = [path_html for path_html in path_dir_html.iterdir()]

        htmls_content = HTMLsContent.from_paths_html(paths_html=paths_html)

        return htmls_content


class HTMLsContentDataInterface:
    def __init__(self, filepath: Path) -> None:
        self.filepath = filepath

    def save(self, htmls_content: HTMLsContent) -> None:
        self._save(filepath=self.filepath, htmls_content=htmls_content)

    @staticmethod
    def _save(filepath: Path, htmls_content: HTMLsContent) -> None:
        filepath.parent.mkdir(parents=True, exist_ok=True)

        with open(filepath, "wb") as f:
            byte_json = orjson.dumps(htmls_content)

            f.write(byte_json)

            logger.info(f"Saved a {type(htmls_content)} object to {filepath}")

    def load(self) -> HTMLsContent:
        return self._load(filepath=self.filepath)

    @staticmethod
    def _load(filepath: Path) -> HTMLsContent:
        with open(filepath, "rb") as f:
            byte_json = f.read()
            dict_json = orjson.loads(byte_json)

            htmls_content = dacite.from_dict(data_class=HTMLsContent, data=dict_json)

            logger.info(f"Loaded a {type(htmls_content)} object from {filepath}")

            return htmls_content
