import logging
from pathlib import Path

from epicurus.data_interfaces.htmls_content_data_interface import (
    HTMLsContent,
    HTMLsContentDataInterface,
)

logger = logging.getLogger(__name__)


def type_raw_htmls_content(
    path_dir_raw_htmls_content: Path, path_htmls_content: Path
) -> None:
    # Data Acess - Input
    htmls_content = HTMLsContent.from_dir_html(path_dir_html=path_dir_raw_htmls_content)

    # Data Access - Output
    htmls_content_data_interface = HTMLsContentDataInterface(
        filepath=path_htmls_content
    )
    htmls_content_data_interface.save(htmls_content)


if __name__ == "__main__":
    import argparse
    import logging

    from epicurus.nodes.project_logging import default_logging

    default_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(
        description="Parse raw HTML files of information content"
        " into their typed representation"
    )
    parser.add_argument(
        "-pdrhc",
        "--path_dir_raw_htmls_content",
        type=Path,
        required=True,
        help="Path from which a directory of raw HTML files is loaded",
    )
    parser.add_argument(
        "-phc",
        "--path_htmls_content",
        type=Path,
        required=True,
        help="Path to which a typed version of input HTML files is saved",
    )

    args = parser.parse_args()

    type_raw_htmls_content(
        path_dir_raw_htmls_content=args.path_dir_raw_htmls_content,
        path_htmls_content=args.path_htmls_content,
    )
