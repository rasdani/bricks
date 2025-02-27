from util.configs import build_extractor_function_config
from util.enums import State
from . import goodbye_extraction, INPUT_EXAMPLE


def get_config():
    return build_extractor_function_config(
        function=goodbye_extraction,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=58,
        tabler_icon="HandLittleFinger",
        min_refinery_version="1.7.0",
        state=State.PUBLIC,
    )
