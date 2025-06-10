import logging
logger = logging.getLogger("tool_parser")


def open_file_read(filepath):
    """
    Opens provided file for reading.
    """
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        logger.warning("Input file not found.")

def parse_lines(content):
    """
    Parses each line of an opened file.
    Returns a comma-seperated list of lines if content can be parsed.
    Returns None is content cannot be parsed
    """
    try:
        return content.splitlines()
    except ValueError:
        logger.warning("Provided input cannot be parsed into lines.")
        return

def tool_dict_builder(parsed_content):
    """
    Builds a dictionary of tools present in the parsed_content
    - tool_dict key = tool_name (ex. T1)
    - tool_dict value = sub_dict of tool_name's attributes
    (ex. {'S': '2', 'A': '1', 'C': '1'})

    Returns a dict of tools if input is valid.
    Returns None if Error is raised due to malformed input
    (ex. empty tool_name, missing required attribute)

    """
    tool_dict = {}
    for line in parsed_content:
        if not line.startswith('T'):
            continue

        split_line = line.split()

        if len(split_line) < 2:
            raise ValueError(f"Tool name is empty in '{line}'.")

        tool_name = split_line[1]
        sub_dict = {}

        try:
            for item in split_line[2:5]:
                if ":" not in item:
                    raise ValueError(f"Missing ':' in '{item}' in '{line}'")
                attribute, value  = item.split(':')
                if not attribute:
                    raise ValueError(f"Missing attribute in '{line}'")
                if not value:
                    raise ValueError(f"Missing value in '{line}'")
                sub_dict[attribute] = value

            if not all(attr in sub_dict for attr in ("S", "A", "C")):
                raise ValueError(f"Missing minimum required attributes (S,A,C) in '{line}'")

            tool_dict[tool_name] = sub_dict

        except ValueError as e:
            logger.warning(f"{e}")
            return None

    return tool_dict

def material_dict_builder(parsed_content):
    pass
