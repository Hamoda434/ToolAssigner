import logging
logger = logging.getLogger(__name__)

def open_file_read(filepath):
    """
    Opens provided file for reading.
    Raises exception if content can't be opened and/or found.
    """
    with open(filepath, 'r') as f:
        return f.read()

def parse_lines(content):
    """
    Parses each line of an opened file.
    Returns a comma-seperated list of lines if content can be parsed.
    Raises exception if content can't be parsed.
    """
    return content.splitlines()

class ToolMaterialBuilder:
    def __init__(self):
        """
        Initializes class ToolMaterialBuilder
        """

    @staticmethod
    def tool_dict_builder(parsed_content):
        """
        Builds a dictionary of tools present in the parsed_content
        - tool_dict key = tool_name (ex. T1)
        - tool_dict value = sub_dict of tool_name's attributes - S,A,C
        (ex. {'S': '2', 'A': '1', 'C': '1'})

        Returns a dict of tools if input is valid.
        Raises ValueError if there is malformed input.
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

            for item in split_line[2:]:
                if ":" not in item:
                    raise ValueError(f"Missing ':' in '{item}' in '{line}'")
                attribute, value = item.split(':')
                if not attribute:
                    raise ValueError(f"Missing attribute in '{line}'")
                if not value:
                    raise ValueError(f"Missing value in '{line}'")
                sub_dict[attribute] = int(value)

            required_attrs = ("S", "A", "C")
            if not all(attr in sub_dict for attr in required_attrs):
                raise ValueError(f"Missing required attributes (S,A,C) in '{line}'")

            tool_dict[tool_name] = sub_dict

        return tool_dict

    @staticmethod
    def material_dict_builder(parsed_content):
        """
        Builds a dictionary of materials present in the parsed_content
        - tool_dict key = material_name (ex. M1)
        - tool_dict value = sub_dict of tool_name's attributes - S,A,C,tool_pref(preferences)
        (ex. {'S': '4', 'A': '3', 'C': '7', 'tool_pref': ['T0', 'T2', 'T1']})

        Returns a dict of materials if input is valid.
        Raises ValueError if there is malformed input.
        (ex. empty material_name, missing required attribute)
        """
        material_dict = {}
        for line in parsed_content:
            if not line.startswith('M'):
                continue

            split_line = line.split()

            if len(split_line) < 2:
                raise ValueError(f"Material name is empty in '{line}'.")

            material_name = split_line[1]
            sub_dict = {}

            for item in split_line[2:]:
                if ":" in item:
                    attribute, value = item.split(':')
                    if not attribute:
                        raise ValueError(f"Missing attribute in '{line}'")
                    if not value:
                        raise ValueError(f"Missing value in '{line}'")
                    sub_dict[attribute] = int(value)
                elif ">" in item:
                    pref_order = item.split(">")
                    sub_dict["tool_pref"] = pref_order
                else:
                    raise ValueError(f"Missing ':' or '>' in '{item}' in '{line}'")

            required_attrs = ("S", "A", "C", "tool_pref")
            if not all(attr in sub_dict for attr in required_attrs):
                raise ValueError(f"Missing required attributes (S,A,C,tool_pref) in '{line}'")

            material_dict[material_name] = sub_dict

        return material_dict