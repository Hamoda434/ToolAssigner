import sys

from ToolAssigner.parser import open_file_read, parse_lines, tool_dict_builder, material_dict_builder
import logging

logger = logging.getLogger(__name__)

def toolAssigner():
    opened = open_file_read("input.txt")
    if not opened:
        logger.error("Could not find and/or open provided input file.")
        sys.exit(1)

    parsed_content = parse_lines(opened)
    if not parsed_content:
        logger.error("Could not parse provided input file.")
        sys.exit(1)
    #print(parsed_content)
    tool_dict = tool_dict_builder(parsed_content)
    if not tool_dict:
        logger.error("Could not build a full tool dictionary.")
        sys.exit(1)
    #print(tool_dict)
    material_dict = material_dict_builder(parsed_content)
    if not material_dict:
        logger.error("Could not build a full material dictionary.")
        sys.exit(1)
    #print(material_dict)

if __name__ == "__main__":
    toolAssigner()