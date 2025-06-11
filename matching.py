import logging
logger = logging.getLogger(__name__)

class ToolMaterialMatcher:
    def __init__(self, tool_dict, material_dict):
        """
        Initializes class with given tool_dict and material_dict
        """
        self.tool_dict = tool_dict
        self.material_dict = material_dict

    def calculate_dot_product(self, tool, material):
        """
        Takes given tool and given material and calculates dot product
        Returns calculated dot product
        """
        a = [tool["S"], tool["A"], tool["C"]]
        b = [material["S"], material["A"], material["C"]]
        dot_product = sum(x * y for x, y in zip(a, b))
        return dot_product

    def add_tool_fit_to_material(self):
        """
        Adds a list of descending sorted tuples to each material dict under key "Fit".
        Sorted tuples represent dot product to respective tool.
        (ex. 'Fit': [('T0', 104), ('T2', 83), ('T1', 17)])
        """
        for material_key in self.material_dict.keys():
            fit = []
            material = self.material_dict[material_key]

            for tool_key in self.tool_dict.keys():
                tool = self.tool_dict[tool_key]
                dot_product = self.calculate_dot_product(tool, material)
                fit.append((tool_key, dot_product))

            fit.sort(key=lambda x: x[1], reverse=True)
            material["Fit"] = fit

        print(self.material_dict)


