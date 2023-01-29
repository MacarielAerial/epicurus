from __future__ import annotations

from pathlib import Path

from pytest import fixture

from epicurus.nodes.project_logging import default_logging


@fixture
def test_logging() -> None:
    default_logging()


@fixture
def test_fixture() -> TestFixture:
    return TestFixture()


class TestFixture:
    @property
    def path_own_file(self) -> Path:
        return Path(__file__)

    @property
    def path_dir_test(self) -> Path:
        return self.path_own_file.parent

    @property
    def path_dir_data(self) -> Path:
        return self.path_dir_test / "data"

    @property
    def path_dir_01_raw(self) -> Path:
        return self.path_dir_data / "01_raw"

    @property
    def path_dir_01_raw_content(self) -> Path:
        return self.path_dir_01_raw / "content"
