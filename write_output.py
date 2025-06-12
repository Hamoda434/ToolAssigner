import sys,logging
logging.basicConfig(level=logging.INFO, format='%(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

def write_results_to_output(tool_dict):
    """
    Creates file output.txt for writing.
    Raises exception if file can't be created and/or written on.
    """
    #logger.info(tool_dict)
    with open("output.txt", "w") as f:
        for took_key in tool_dict:
            f.write(took_key + ": ")
            for match in tool_dict[took_key]['assigned_materials']:
                material = match[0]
                dot_product = str(match[1])
                f.write(material+ "(" + dot_product +") ")
            f.write("\n")


