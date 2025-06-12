import sys, logging
logging.basicConfig(level=logging.INFO, format='%(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

class ToolMaterialMatcher:
    def __init__(self, tool_dict, material_dict):
        """
        Initializes class with given tool_dict and material_dict
        """
        self.tool_dict = tool_dict
        self.material_dict = material_dict
        self.unmatched_material_stack = list(reversed(self.material_dict.keys()))

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
        Under key "material_fit" adds a list of descending sorted tuples to each tool in tool_dict".
        Sorted tuples represent dot product to respective material.
        (ex. 'material_fit': [('M6', 188), ('M3', 171), ('M5', 161), ('M11', 154),...])
        """
        for tool_key in self.tool_dict.keys():
            fit = {}
            tool = self.tool_dict[tool_key]
            for material_key in self.material_dict.keys():
                material = self.material_dict[material_key]
                dot_product = self.calculate_dot_product(tool, material)
                fit[material_key] = dot_product
            tool["material_fit"] = fit

    def init_material_dict_for_matching(self):
        """
        For each material in material_dict, adds a 'next_tool_pref' key and initializes
        its value to 0.

        'next_tool_pref' represents the index of tool it prefers to be assigned
        to according to its 'tool_pref' value.
        (ex.'M0' :{{'tool_pref': ['T2', 'T0', 'T1']} {'next_tool_pref': 0} }
            'M0' prefers to be assigned to T2)
        """
        for material_key in self.material_dict.keys():
            self.material_dict[material_key]['next_tool_pref'] = 0

    def init_tool_dict_for_matching(self):
        """
        For each tool in tool_dict, adds an 'assigned_materials' key and initializes
        its value to an empty list [].

        'assigned_materials' keeps track of materials currently assigned to the tool,
        formatted as (material, dot product relative to tool)
        (ex. T0: {'assigned_materials': [('M2', 128), ('M4', 122), ('M5', 161), ('M11', 154)]}
        """
        for tool_key in self.tool_dict.keys():
            self.tool_dict[tool_key]['assigned_materials'] = []

    def tool_material_matching_init(self):
        """
        Called by tool_material_matching before the main matching algorithm is run.
        Prepares tool_dict and material_dict for the matching algorithm.
        """
        self.compute_material_fit_for_tool()
        self.init_material_dict_for_matching()
        self.init_tool_dict_for_matching()

    def sort_tool_assignments(self):
        """
        Sorts each tool's assignments in desc. order based on dot product.
        """
        for tool_key in self.tool_dict.keys():
            self.tool_dict[tool_key]['assigned_materials'].sort(key=lambda x: x[1], reverse=True)

    def tool_material_matching(self):
        """
        Runs the Gale–Shapley (aka Stable Matching) algorithm to match tools
        and materials in a manner such that no material could be moved to a
        different tool that a material would prefer more *and* be a better fit
        for the tool than any material already scheduled on it.

        Material(s) take on the role of "Proposer", tool(s) take on the role of
        "Acceptor"

        Each tool's 'assigned_materials' key contains a desc. sorted list of their
        finalized matches after the algorithm is completed.
        """
        self.tool_material_matching_init()

        capacity = len(self.material_dict)//len(self.tool_dict)

        while self.unmatched_material_stack:
            current_material_key = self.unmatched_material_stack.pop()
            #logger.info(current_material_key)

            proposed_index = self.material_dict[current_material_key]['next_tool_pref']
            proposed_match_tool_key = self.material_dict[current_material_key]['tool_pref'][proposed_index]
            # logger.info(proposed_match_tool_key)

            tool_curr_matches = self.tool_dict[proposed_match_tool_key]['assigned_materials']
            dot_product = self.tool_dict[proposed_match_tool_key]['material_fit'][current_material_key]

            if len(tool_curr_matches) < capacity:
                tool_curr_matches.append((current_material_key, dot_product))

            else:
                worst_curr_match = min(tool_curr_matches, key=lambda x: x[1])
                if dot_product > worst_curr_match[1]:
                    tool_curr_matches.remove(worst_curr_match)
                    worst_match_key = worst_curr_match[0]

                    self.material_dict[worst_match_key]['next_tool_pref'] += 1
                    self.unmatched_material_stack.append(worst_curr_match[0])

                    tool_curr_matches.append((current_material_key, dot_product))
                else:
                    self.material_dict[current_material_key]['next_tool_pref'] += 1
                    self.unmatched_material_stack.append(current_material_key)

        self.sort_tool_assignments()
        """
        #Final Results:
        for tool_key in self.tool_dict.keys():
            logger.info(self.tool_dict[tool_key]['assigned_materials'])
        """


