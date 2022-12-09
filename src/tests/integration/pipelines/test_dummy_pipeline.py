from logging import Logger

from gaia.pipelines.dummy_pipeline import dummy_pipeline


def test_dummy_pipeline(test_logger: Logger) -> None:
    dummy_pipeline(logger=test_logger)

    assert True
