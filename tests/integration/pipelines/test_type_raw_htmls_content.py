import tempfile
from pathlib import Path

from epicurus.pipelines.type_raw_htmls_content import type_raw_htmls_content
from tests.conftest import TestFixture


def test_type_raw_htmls_content(test_fixture: TestFixture, test_logging: None) -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        path_htmls_content = Path(tmp_dir) / "htmls_content.json"

        type_raw_htmls_content(
            path_dir_raw_htmls_content=test_fixture.path_dir_01_raw_content,
            path_htmls_content=path_htmls_content,
        )

        assert path_htmls_content.is_file()
