from ToolAssigner.parser import open_file_read, parse_lines, tool_dict_builder, material_dict_builder

def toolAssigner():
    opened = open_file_read("input.txt")
    parsed_content = parse_lines(opened)
    print(parsed_content)
    tool_dict = tool_dict_builder(parsed_content)
    print(tool_dict)
    #material_dict = material_dict_builder(parsed_content)

if __name__ == "__main__":
    toolAssigner()