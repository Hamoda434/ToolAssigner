import sys,logging
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='%(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

def write_results_to_output(input_filename, tool_dict):
    """
    Creates file called <input_filename>_output.txt for writing.
    Raises exception if file can't be created and/or written on.
    """
    #logger.info(input_filename)
    #logger.info(tool_dict)

    ### Generated with ChatGPT ###
    current_file_dir = Path(__file__).resolve().parent  # -> ToolAssigner/
    data_dir = current_file_dir / "data"
    output_dir = data_dir / "output"

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Build input/output path names
    input_path = Path(input_filename)
    output_path = output_dir / f"{input_path.stem}_output.txt"
    ### END ###

    with open(output_path, "w") as f:
        for tool_key in tool_dict:
            f.write(tool_key + ": ")
            for match in tool_dict[tool_key]['assigned_materials']:
                material = match[0]
                dot_product = str(match[1])
                f.write(material+ "(" + dot_product +") ")
            f.write("\n")