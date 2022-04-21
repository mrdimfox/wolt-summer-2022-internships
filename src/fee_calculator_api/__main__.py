from logging import config as log_config, getLogger
import json
from pathlib import Path
import uvicorn

from fee_calculator_api.api import api


def _setup_logging():
    log_config_path = Path(__file__).with_name("logger.json")
    with log_config_path.open() as config_file:
        log_config.dictConfig(json.load(config_file))


if __name__ == "__main__":
    _setup_logging()
    log = getLogger("fee_calculator_api")

    log.warning(
        "Start application in development mode! "
        "Use external uvicorn call to run it in production."
    )

    uvicorn.run(
        api,  # type: ignore
        host="0.0.0.0",
        port=5000,
        log_level="info",
    )
