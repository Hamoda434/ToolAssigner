import logging
logger = logging.getLogger(__name__)

class ToolMaterialMatcher:
    def __init__(self, tool_dict, material_dict):
        """
        Initializes class with given tool_dict and material_dict
        """
        self.tool_dict = tool_dict
        self.material_dict = material_dict

    @staticmethod
    def calculate_dot_product(tool, material):
        """
        Takes given tool and given material and calculates dot product
        Returns calculated dot product
        """
        a = [tool["S"], tool["A"], tool["C"]]
        b = [material["S"], material["A"], material["C"]]
        dot_product = sum(x * y for x, y in zip(a, b))
        return dot_product

    def compute_material_fit_for_tool(self):
        """
        Adds a list of descending sorted tuples to each tool in tool_dict under key "Fit".
        Sorted tuples represent dot product to respective material.
        (ex. 'material_fit': [('M6', 188), ('M3', 171), ('M5', 161), ('M11', 154),...])
        """
        for tool_key in self.tool_dict.keys():
            fit = []
            tool = self.tool_dict[tool_key]
            for material_key in self.material_dict.keys():
                material = self.material_dict[material_key]
                dot_product = self.calculate_dot_product(tool, material)
                fit.append((material_key, dot_product))
            fit.sort(key=lambda x: x[1], reverse=True)
            tool["material_fit"] = fit
        print(self.tool_dict)


    def tool_material_matching_init(self):
        self.compute_material_fit_for_tool()
        self.init_material_dict_for_matching()
        self.init_tool_dict_for_matching()


    def init_material_dict_for_matching(self):
        #this will initialize for each m in matching_dict:
        for material_key in self.material_dict.keys():
            self.material_dict[material_key]['next_tool'] = 0
            self.material_dict[material_key]['assigned_tool'] = None

    def init_tool_dict_for_matching(self):
        #this will initialize for each t in matching_dict:
        for tool_key in self.tool_dict.keys():
            self.tool_dict[tool_key]['assigned_materials'] = []

    def tool_material_matching(self):
        self.tool_material_matching_init()
        print(self.material_dict)
        print(self.tool_dict)
        #This will run the actual algo, and this is called by main.py
        pass
