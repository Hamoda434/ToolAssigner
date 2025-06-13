import unittest
from ToolAssigner.matching import ToolMaterialMatcher

class TestToolMaterialMatcher(unittest.TestCase):
    def test_calculate_dot_product(self):
        tool = {"S":1,"A":2,"C":3}
        material = {'S': 3, 'A': 9, 'C': 2}
        result = ToolMaterialMatcher.calculate_dot_product(tool, material)
        expected = 27
        self.assertEqual(result, expected)

    def test_compute_material_fit_for_tool(self):
        tool_dict = {'T0': {'S': 2, 'A': 1, 'C': 5},
                     'T1': {'S': 4, 'A': 4, 'C': 3},
                     'T2': {'S': 2, 'A': 9, 'C': 2}}
        material_dict = {'M0': {'S': 10, 'A': 7, 'C': 1, 'tool_pref': ['T1', 'T2', 'T0']},
                         'M1': {'S': 4, 'A': 4, 'C': 9, 'tool_pref': ['T1', 'T0', 'T2']},
                         'M2': {'S': 9, 'A': 4, 'C': 9, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M3': {'S': 8, 'A': 10, 'C': 5, 'tool_pref': ['T1', 'T2', 'T0']},
                         'M4': {'S': 7, 'A': 6, 'C': 5, 'tool_pref': ['T1', 'T2', 'T0']},
                         'M5': {'S': 6, 'A': 2, 'C': 2, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M6': {'S': 6, 'A': 6, 'C': 10, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M7': {'S': 8, 'A': 9, 'C': 2, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M8': {'S': 9, 'A': 5, 'C': 10, 'tool_pref': ['T2', 'T0', 'T1']}}
        matcher = ToolMaterialMatcher(tool_dict, material_dict)
        matcher.compute_material_fit_for_tool()
        result = tool_dict
        expected = {'T0': {'S': 2, 'A': 1, 'C': 5, 'material_fit': {'M0': 32, 'M1': 57, 'M2': 67, 'M3': 51, 'M4': 45, 'M5': 24, 'M6': 68, 'M7': 35, 'M8': 73}},
                    'T1': {'S': 4, 'A': 4, 'C': 3, 'material_fit': {'M0': 71, 'M1': 59, 'M2': 79, 'M3': 87, 'M4': 67, 'M5': 38, 'M6': 78, 'M7': 74, 'M8': 86}},
                    'T2': {'S': 2, 'A': 9, 'C': 2, 'material_fit': {'M0': 85, 'M1': 62, 'M2': 72, 'M3': 116, 'M4': 78, 'M5': 34, 'M6': 86, 'M7': 101, 'M8': 83}}}
        self.assertEqual(result, expected)

    def test_init_material_dict_for_matching(self):
        tool_dict = {'T0': {'S': 2, 'A': 1, 'C': 5},
                     'T1': {'S': 4, 'A': 4, 'C': 3},
                     'T2': {'S': 2, 'A': 9, 'C': 2}}
        material_dict = {'M0': {'S': 10, 'A': 7, 'C': 1, 'tool_pref': ['T1', 'T2', 'T0']},
                         'M1': {'S': 4, 'A': 4, 'C': 9, 'tool_pref': ['T1', 'T0', 'T2']},
                         'M2': {'S': 9, 'A': 4, 'C': 9, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M3': {'S': 8, 'A': 10, 'C': 5, 'tool_pref': ['T1', 'T2', 'T0']},
                         'M4': {'S': 7, 'A': 6, 'C': 5, 'tool_pref': ['T1', 'T2', 'T0']},
                         'M5': {'S': 6, 'A': 2, 'C': 2, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M6': {'S': 6, 'A': 6, 'C': 10, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M7': {'S': 8, 'A': 9, 'C': 2, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M8': {'S': 9, 'A': 5, 'C': 10, 'tool_pref': ['T2', 'T0', 'T1']}}
        matcher = ToolMaterialMatcher(tool_dict, material_dict)
        matcher.init_material_dict_for_matching()
        result = material_dict
        expected = {'M0': {'S': 10, 'A': 7, 'C': 1, 'tool_pref': ['T1', 'T2', 'T0'], 'next_tool_pref': 0},
                    'M1': {'S': 4, 'A': 4, 'C': 9, 'tool_pref': ['T1', 'T0', 'T2'], 'next_tool_pref': 0},
                    'M2': {'S': 9, 'A': 4, 'C': 9, 'tool_pref': ['T2', 'T0', 'T1'], 'next_tool_pref': 0},
                    'M3': {'S': 8, 'A': 10, 'C': 5, 'tool_pref': ['T1', 'T2', 'T0'], 'next_tool_pref': 0},
                    'M4': {'S': 7, 'A': 6, 'C': 5, 'tool_pref': ['T1', 'T2', 'T0'], 'next_tool_pref': 0},
                    'M5': {'S': 6, 'A': 2, 'C': 2, 'tool_pref': ['T2', 'T0', 'T1'], 'next_tool_pref': 0},
                    'M6': {'S': 6, 'A': 6, 'C': 10, 'tool_pref': ['T2', 'T0', 'T1'], 'next_tool_pref': 0},
                    'M7': {'S': 8, 'A': 9, 'C': 2, 'tool_pref': ['T2', 'T0', 'T1'], 'next_tool_pref': 0},
                    'M8': {'S': 9, 'A': 5, 'C': 10, 'tool_pref': ['T2', 'T0', 'T1'], 'next_tool_pref': 0}}
        self.assertEqual(result, expected)

    def test_init_tool_dict_for_matching(self):
        tool_dict = {'T0': {'S': 2, 'A': 1, 'C': 5},
                     'T1': {'S': 4, 'A': 4, 'C': 3},
                     'T2': {'S': 2, 'A': 9, 'C': 2}}
        material_dict = {'M0': {'S': 10, 'A': 7, 'C': 1, 'tool_pref': ['T1', 'T2', 'T0']},
                         'M1': {'S': 4, 'A': 4, 'C': 9, 'tool_pref': ['T1', 'T0', 'T2']},
                         'M2': {'S': 9, 'A': 4, 'C': 9, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M3': {'S': 8, 'A': 10, 'C': 5, 'tool_pref': ['T1', 'T2', 'T0']},
                         'M4': {'S': 7, 'A': 6, 'C': 5, 'tool_pref': ['T1', 'T2', 'T0']},
                         'M5': {'S': 6, 'A': 2, 'C': 2, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M6': {'S': 6, 'A': 6, 'C': 10, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M7': {'S': 8, 'A': 9, 'C': 2, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M8': {'S': 9, 'A': 5, 'C': 10, 'tool_pref': ['T2', 'T0', 'T1']}}
        matcher = ToolMaterialMatcher(tool_dict, material_dict)
        matcher.init_tool_dict_for_matching()
        result = tool_dict
        expected = {'T0': {'S': 2, 'A': 1, 'C': 5, 'assigned_materials': []},
                    'T1': {'S': 4, 'A': 4, 'C': 3, 'assigned_materials': []},
                    'T2': {'S': 2, 'A': 9, 'C': 2, 'assigned_materials': []}}
        self.assertEqual(result, expected)

    def test_tool_material_testing(self):
        tool_dict = {'T0': {'S': 2, 'A': 1, 'C': 5},
                     'T1': {'S': 4, 'A': 4, 'C': 3},
                     'T2': {'S': 2, 'A': 9, 'C': 2}}
        material_dict = {'M0': {'S': 10, 'A': 7, 'C': 1, 'tool_pref': ['T1', 'T2', 'T0']},
                         'M1': {'S': 4, 'A': 4, 'C': 9, 'tool_pref': ['T1', 'T0', 'T2']},
                         'M2': {'S': 9, 'A': 4, 'C': 9, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M3': {'S': 8, 'A': 10, 'C': 5, 'tool_pref': ['T1', 'T2', 'T0']},
                         'M4': {'S': 7, 'A': 6, 'C': 5, 'tool_pref': ['T1', 'T2', 'T0']},
                         'M5': {'S': 6, 'A': 2, 'C': 2, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M6': {'S': 6, 'A': 6, 'C': 10, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M7': {'S': 8, 'A': 9, 'C': 2, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M8': {'S': 9, 'A': 5, 'C': 10, 'tool_pref': ['T2', 'T0', 'T1']}}
        matcher = ToolMaterialMatcher(tool_dict, material_dict)
        matcher.tool_material_matching()
        result = tool_dict
        expected = {'T0': {'S': 2, 'A': 1, 'C': 5, 'material_fit': {'M0': 32, 'M1': 57, 'M2': 67, 'M3': 51, 'M4': 45, 'M5': 24, 'M6': 68, 'M7': 35, 'M8': 73}, 'assigned_materials': [('M2', 67), ('M1', 57), ('M5', 24)]},
                    'T1': {'S': 4, 'A': 4, 'C': 3, 'material_fit': {'M0': 71, 'M1': 59, 'M2': 79, 'M3': 87, 'M4': 67, 'M5': 38, 'M6': 78, 'M7': 74, 'M8': 86}, 'assigned_materials': [('M3', 87), ('M0', 71), ('M4', 67)]},
                    'T2': {'S': 2, 'A': 9, 'C': 2, 'material_fit': {'M0': 85, 'M1': 62, 'M2': 72, 'M3': 116, 'M4': 78, 'M5': 34, 'M6': 86, 'M7': 101, 'M8': 83}, 'assigned_materials': [('M7', 101), ('M6', 86), ('M8', 83)]}}
        self.assertEqual(result, expected)

    def test_identical_fits_and_prefs(self):
        tool_dict = {'T0': {'S': 1, 'A': 2, 'C': 3},
                     'T1': {'S': 1, 'A': 2, 'C': 3},
                     'T2': {'S': 1, 'A': 2, 'C': 3},
                     'T3': {'S': 1, 'A': 2, 'C': 3},
                     'T4': {'S': 1, 'A': 2, 'C': 3}}
        material_dict = {'M0': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M1': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M2': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M3': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M4': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M5': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M6': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M7': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M8': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M9': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M10': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M11': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M12': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M13': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']},
                         'M14': {'S': 1, 'A': 2, 'C': 3, 'tool_pref': ['T0', 'T1', 'T2', 'T3', 'T4']}}
        matcher = ToolMaterialMatcher(tool_dict, material_dict)
        matcher.tool_material_matching()
        result = tool_dict
        expected = {'T0': {'S': 1, 'A': 2, 'C': 3, 'material_fit': {'M0': 14, 'M1': 14, 'M2': 14, 'M3': 14, 'M4': 14, 'M5': 14, 'M6': 14, 'M7': 14, 'M8': 14, 'M9': 14, 'M10': 14, 'M11': 14, 'M12': 14, 'M13': 14, 'M14': 14}, 'assigned_materials': [('M0', 14), ('M1', 14), ('M2', 14)]},
                    'T1': {'S': 1, 'A': 2, 'C': 3, 'material_fit': {'M0': 14, 'M1': 14, 'M2': 14, 'M3': 14, 'M4': 14, 'M5': 14, 'M6': 14, 'M7': 14, 'M8': 14, 'M9': 14, 'M10': 14, 'M11': 14, 'M12': 14, 'M13': 14, 'M14': 14}, 'assigned_materials': [('M3', 14), ('M4', 14), ('M5', 14)]},
                    'T2': {'S': 1, 'A': 2, 'C': 3, 'material_fit': {'M0': 14, 'M1': 14, 'M2': 14, 'M3': 14, 'M4': 14, 'M5': 14, 'M6': 14, 'M7': 14, 'M8': 14, 'M9': 14, 'M10': 14, 'M11': 14, 'M12': 14, 'M13': 14, 'M14': 14}, 'assigned_materials': [('M6', 14), ('M7', 14), ('M8', 14)]},
                    'T3': {'S': 1, 'A': 2, 'C': 3, 'material_fit': {'M0': 14, 'M1': 14, 'M2': 14, 'M3': 14, 'M4': 14, 'M5': 14, 'M6': 14, 'M7': 14, 'M8': 14, 'M9': 14, 'M10': 14, 'M11': 14, 'M12': 14, 'M13': 14, 'M14': 14}, 'assigned_materials': [('M9', 14), ('M10', 14), ('M11', 14)]},
                    'T4': {'S': 1, 'A': 2, 'C': 3, 'material_fit': {'M0': 14, 'M1': 14, 'M2': 14, 'M3': 14, 'M4': 14, 'M5': 14, 'M6': 14, 'M7': 14, 'M8': 14, 'M9': 14, 'M10': 14, 'M11': 14, 'M12': 14, 'M13': 14, 'M14': 14}, 'assigned_materials': [('M12', 14), ('M13', 14), ('M14', 14)]}}
        self.assertEqual(result, expected)

    def test_one_tool_no_materials(self):
        tool_dict = {'T0': {'S': 7, 'A': 7, 'C': 10}}
        material_dict = {}
        matcher = ToolMaterialMatcher(tool_dict, material_dict)
        matcher.tool_material_matching()
        result = tool_dict
        expected = {'T0': {'S': 7, 'A': 7, 'C': 10, 'material_fit': {}, 'assigned_materials': []}}
        self.assertEqual(result, expected)

    def test_one_tool_multiple_materials(self):
        tool_dict = {'T0': {'S': 2, 'A': 1, 'C': 5}}
        material_dict = {'M0': {'S': 6, 'A': 2, 'C': 2, 'tool_pref': ['T0']},
                         'M1': {'S': 6, 'A': 6, 'C': 10, 'tool_pref': ['T0']},
                         'M2': {'S': 8, 'A': 9, 'C': 2, 'tool_pref': ['T0']},
                         'M3': {'S': 9, 'A': 5, 'C': 10, 'tool_pref': ['T0']}}
        matcher = ToolMaterialMatcher(tool_dict, material_dict)
        matcher.tool_material_matching()
        result = tool_dict
        expected = {'T0': {'S': 2, 'A': 1, 'C': 5, 'material_fit': {'M0': 24, 'M1': 68, 'M2': 35, 'M3': 73}, 'assigned_materials': [('M3', 73), ('M1', 68), ('M2', 35), ('M0', 24)]}}
        self.assertEqual(result, expected)

    def test_equal_fit_and_pref(self):
        tool_dict = {'T0': {'S': 5, 'A': 0, 'C': 0}, 'T1': {'S': 0, 'A': 0, 'C': 5}}
        material_dict = {'M0': {'S': 0, 'A': 0, 'C': 5, 'tool_pref': ['T0', 'T1']},
                         'M1': {'S': 5, 'A': 0, 'C': 0, 'tool_pref': ['T1', 'T0']}}
        matcher = ToolMaterialMatcher(tool_dict, material_dict)
        matcher.tool_material_matching()
        result = tool_dict
        expected = {'T0': {'S': 5, 'A': 0, 'C': 0, 'material_fit': {'M0': 0, 'M1': 25}, 'assigned_materials': [('M0', 0)]}, 'T1': {'S': 0, 'A': 0, 'C': 5, 'material_fit': {'M0': 25, 'M1': 0}, 'assigned_materials': [('M1', 0)]}}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
