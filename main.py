import sys
import logging
from ToolAssigner.parser import open_file_read, parse_lines, tool_dict_builder, material_dict_builder


logger = logging.getLogger(__name__)

def tool_material_dict_builder():
    opened = open_file_read("input.txt")
    if not opened:
        raise FileNotFoundError("Could not find open provided input file.")

    parsed_content = parse_lines(opened)
    if not parsed_content:
        raise ValueError("Could not parse provided input file.")
    print(parsed_content)

    tool_dict = tool_dict_builder(parsed_content)
    if not tool_dict:
        raise ValueError("Could not build a full tool dictionary.")
    print(tool_dict)

    material_dict = material_dict_builder(parsed_content)
    if material_dict is None:
        raise ValueError("Could not build a full material dictionary.")
    print(material_dict)

    return tool_dict, material_dict

def tool_material_matching(tool_dict, material_dict):
    print(tool_dict)
    print(material_dict)


if __name__ == "__main__":
    try:
        built_tool_dict, built_material_dict = tool_material_dict_builder()
    except Exception as e:
        logger.error(f"Failed to build tool/material dictionaries: {e}")
        sys.exit(1)

    print(len(built_tool_dict))
    print(len(built_material_dict))

    if len(built_material_dict) % len(built_tool_dict) != 0:
        logger.error("The number of provided tools must divide evenly "
                     "into the number of provided materials.")
        sys.exit(1)

    tool_material_matching(built_tool_dict, built_material_dict)
