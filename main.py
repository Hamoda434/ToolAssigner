import sys, logging
from ToolAssigner.parser import ToolMaterialBuilder, open_file_read, parse_lines
from ToolAssigner.matching import ToolMaterialMatcher
from ToolAssigner.write_output import write_results_to_output

logging.basicConfig(level=logging.INFO, format='%(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

def tool_material_dict_builder():
    opened = open_file_read("input.txt")
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

    return tool_dict, material_dict

def tool_material_matching(tool_dict, material_dict):
    if len(material_dict) % len(tool_dict) != 0:
        raise ValueError("Number of provided tools must evenly divide the number of provided materials.")

    matcher = ToolMaterialMatcher(tool_dict, material_dict)
    matcher.tool_material_matching()
    #logger.info(tool_dict)

def output_match_results(tool_dict):
    write_results_to_output(tool_dict)

if __name__ == "__main__":
    try:
        built_tool_dict, built_material_dict = tool_material_dict_builder()
    except Exception as e:
        logger.error(f"Failed to build tool/material dictionaries: {e}")
        sys.exit(1)

    try:
        tool_material_matching(built_tool_dict, built_material_dict)
    except Exception as e:
        logger.error(f"Failed to match materials with tools: {e}")
        sys.exit(1)

    try:
        output_match_results(built_tool_dict)
    except Exception as e:
        logger.error(f"Failed to write results to output: {e}")
        sys.exit(1)