import sys, logging

from ToolAssigner.parser import ToolMaterialBuilder, open_file_read, parse_lines
from ToolAssigner.matching import ToolMaterialMatcher
from ToolAssigner.write_output import write_results_to_output

logging.basicConfig(level=logging.INFO, format='%(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

def tool_material_dict_builder(input_filename):
    """
    Given a file name 'input_filename', parses the content found within data/input/'input_filename'
    and construct a tool_dict and material_dict based off the file's contents.

    Raises Errors if file is not found, can't be opened, or tool_dict/material_dict cannot
    be constructed from the file's contents
    """

    opened = open_file_read(input_filename)
    parsed_content = parse_lines(opened)

    builder = ToolMaterialBuilder()

    tool_dict = builder.tool_dict_builder(parsed_content)
    if not tool_dict:
        raise ValueError("Could not build a full tool dictionary.")
    #logger.info(tool_dict)

    material_dict = builder.material_dict_builder(parsed_content)
    if material_dict is None:
        raise ValueError("Could not build a full material dictionary.")
    #logger.info(material_dict)

    builder.validate_material_tool_prefs(material_dict, tool_dict.keys())

    return tool_dict, material_dict

def tool_material_matching(tool_dict, material_dict):
    """
    Given a tool_dict and material_dict tuns the Gale–Shapley (aka Stable Matching) algorithm
    to pair tools and materials into a stable match.

    Raises ValueError if number of tools in tool_dict cannot evenly divide number of materials
    in material_dict
    """

    if len(material_dict) % len(tool_dict) != 0:
        raise ValueError("Number of provided tools must evenly divide the number of provided materials.")

    matcher = ToolMaterialMatcher(tool_dict, material_dict)
    matcher.tool_material_matching()
    #logger.info(tool_dict)

def output_match_results(input_filename, tool_dict):
    """
    Given a file name 'input_filename', writes the match results found in a given tool_dict
    to data/output/'input_filename'_output.txt
    """
    write_results_to_output(input_filename, tool_dict)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.error("Usage: python -m ToolAssigner.main <filename>")
        logger.error("Place your input files inside data/input/")
        sys.exit(1)

    input_filename = sys.argv[1]
    try:
        built_tool_dict, built_material_dict = tool_material_dict_builder(input_filename)
    except Exception as e:
        logger.error(f"Failed to build tool/material dictionaries: {e}")
        sys.exit(1)

    try:
        tool_material_matching(built_tool_dict, built_material_dict)
    except Exception as e:
        logger.error(f"Failed to match materials with tools: {e}")
        sys.exit(1)

    try:
        output_match_results(input_filename, built_tool_dict)
    except Exception as e:
        logger.error(f"Failed to write results to output: {e}")
        sys.exit(1)