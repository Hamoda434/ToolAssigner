import unittest
from ToolAssigner.parser import ToolMaterialBuilder

class TestToolMaterialBuilder(unittest.TestCase):
    def test_tool_dict_builder(self):
        parsed_content = ['T T0 S:1 A:2 C:3',
                          'T T1 S:9 A:8 C:7',
                          'T T2 S:10 A:13 C:6']
        builder = ToolMaterialBuilder()
        result = builder.tool_dict_builder(parsed_content)
        expected = {'T0':{"S":1,"A":2,"C":3},
                    'T1':{"S":9,"A":8,"C":7},
                    'T2':{"S":10,"A":13,"C":6}}
        self.assertEqual(result, expected)

    def test_material_dict_builder(self):
        parsed_content = ['M M0 S:3 A:9 C:2 T2>T0>T1',
                          'M M1 S:4 A:3 C:7 T0>T2>T1',
                          'M M2 S:4 A:0 C:10 T0>T2>T1']
        builder = ToolMaterialBuilder()
        result = builder.material_dict_builder(parsed_content)
        expected = {'M0': {'S': 3, 'A': 9, 'C': 2, 'tool_pref': ['T2', 'T0', 'T1']},
                    'M1': {'S': 4, 'A': 3, 'C': 7, 'tool_pref': ['T0', 'T2', 'T1']},
                    'M2': {'S': 4, 'A': 0, 'C': 10, 'tool_pref': ['T0', 'T2', 'T1']}}
        self.assertEqual(result, expected)

    def test_no_tools(self):
        builder = ToolMaterialBuilder()
        parsed_content = []
        with self.assertRaises(ValueError):
            tool_dict = builder.tool_dict_builder(parsed_content)
            if not tool_dict:
                raise ValueError("Could not build a full tool dictionary.")

    def test_no_materials(self):
        builder = ToolMaterialBuilder()
        parsed_content = []
        result = builder.material_dict_builder(parsed_content)
        expected = {}
        self.assertEqual(result, expected)

    def test_valid_validate_material_tool_prefs(self):
        builder = ToolMaterialBuilder()
        material_dict = {'M0': {'S': 3, 'A': 9, 'C': 2, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M1': {'S': 4, 'A': 3, 'C': 7, 'tool_pref': ['T0', 'T2', 'T1']},
                         'M2': {'S': 4, 'A': 0, 'C': 10, 'tool_pref': ['T0', 'T2', 'T1']}}
        valid_tools = ['T0', 'T1', 'T2']
        try:
            builder.validate_material_tool_prefs(material_dict, valid_tools)
        except Exception as e:
            self.fail(f"Exception raised: {e}")

    def test_invalid_validate_material_tool_prefs(self):
        builder = ToolMaterialBuilder()
        material_dict = {'M0': {'S': 3, 'A': 9, 'C': 2, 'tool_pref': ['T2', 'T0', 'T1']},
                         'M1': {'S': 4, 'A': 3, 'C': 7, 'tool_pref': ['T0', 'T3', 'T1']},
                         'M2': {'S': 4, 'A': 0, 'C': 10, 'tool_pref': ['T0', 'T2', 'T1']}}
        valid_tools = ['T0', 'T1', 'T2']
        with self.assertRaises(ValueError):
            builder.validate_material_tool_prefs(material_dict, valid_tools)

    def test_malformed_tool_input(self):
        builder = ToolMaterialBuilder()
        parsed_content = ['T T0 S:1 A:2 C:3',
                          'T T1 S:9 A:8 C:7',
                          'T T2 S10 A:13 C:6']
        with self.assertRaises(ValueError):
            tool_dict = builder.tool_dict_builder(parsed_content)
            if not tool_dict:
                raise ValueError("Could not build a full tool dictionary.")

    def test_malformed_material_input(self):
        builder = ToolMaterialBuilder()
        parsed_content = ['M M0 S:3 A:9 C:2 T2>T0>T1',
                          'M M1 S:4 A:3 C:7 T0>T2>T1',
                          'M M2 S:4 A:0 C:10']
        with self.assertRaises(ValueError):
            material_dict = builder.material_dict_builder(parsed_content)
            if material_dict is None:
                raise ValueError("Could not build a full tool dictionary.")

if __name__ == '__main__':
    unittest.main()
