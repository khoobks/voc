from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class DictTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = {}
            x.attr = 42
            print('Done.')
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = {}
            print(x.attr)
            print('Done.')
            """)

    def test_creation(self):
        # Empty dict
        self.assertCodeExecution("""
            x = {}
            print(x)
            """)

        self.assertCodeExecution("""
            x = {'a': 1}
            print(x)
            """)

    def test_getitem(self):
        # Simple existent key
        self.assertCodeExecution("""
            y = 37
            x = {'a': 1, 'b': 2, 'c': y}
            print('a' in x)
            print('a' not in x)
            print(x['a'])
            """)

        # Simple non-existent key
        self.assertCodeExecution("""
            x = {'a': 1, 'b': 2}
            print('c' in x)
            print('c' not in x)
            print(x['c'])
            """)

    def test_clear(self):
        # Clear a dictionary
        self.assertCodeExecution("""
            x = {'a': 1, 'b': 2}
            print('a' in x)
            print(x.clear())
            print('a' not in x)
            print(x)
            """)

        # Clear an already empty dict
        self.assertCodeExecution("""
            x = {}
            print('a' not in x)
            print(x.clear())
            print('a' not in x)
            print(x)
            """)

    def test_builtin_constructor(self):
        # Construct a dictionary using the dict builtin
        self.assertCodeExecution("""
            x = dict()
            print(x)
            print('a' in x)

            # List of tuples
            x = dict([('a', 1), ('b', 2)])
            print('a' in x)
            print(x['a'])
            print('c' in x)

            # List of lists
            x = dict([['a', 3], ['b', 4]])
            print('a' in x)
            print(x['a'])
            print('c' in x)

            # Tuple of lists
            x = dict((['a', 5], ['b', 6]))
            print('a' in x)
            print(x['a'])
            print('c' in x)

            # Tuple of tuples
            x = dict((('a', 5), ('b', 6)))
            print('a' in x)
            print(x['a'])
            print('c' in x)
        """)

    def test_builtin_non_2_tuples(self):
        # One of the elements isn't a 2-tuple
        self.assertCodeExecution("""
            x = dict([('a', 1), ('b', 2, False)])
            """)

    def test_builtin_non_sequence(self):
        # One of the elements isn't a sequence
        self.assertCodeExecution("""
            x = dict([('a', 1), False, ('b', 2)])
            """)


class UnaryDictOperationTests(UnaryOperationTestCase, TranspileTestCase):
    values = ["{}", "{'a': 1, 'b': 'value', 'c': 1.2345}"]


class BinaryDictOperationTests(BinaryOperationTestCase, TranspileTestCase):
    values = ["{}", "{'a': 1, 'b': 'value', 'c': 1.2345}"]

    not_implemented = [
        'test_add_bytearray',
        'test_add_bytes',
        'test_add_class',
        'test_add_complex',
        'test_add_frozenset',

        'test_and_bytearray',
        'test_and_bytes',
        'test_and_class',
        'test_and_complex',
        'test_and_frozenset',

        'test_eq_bytearray',
        'test_eq_bytes',
        'test_eq_class',
        'test_eq_complex',
        'test_eq_frozenset',

        'test_floor_divide_bytearray',
        'test_floor_divide_bytes',
        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_ge_bytearray',
        'test_ge_bytes',
        'test_ge_class',
        'test_ge_complex',
        'test_ge_frozenset',

        'test_gt_bytearray',
        'test_gt_bytes',
        'test_gt_class',
        'test_gt_complex',
        'test_gt_frozenset',

        'test_le_bytearray',
        'test_le_bytes',
        'test_le_class',
        'test_le_complex',
        'test_le_frozenset',

        'test_lshift_bytearray',
        'test_lshift_bytes',
        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_frozenset',

        'test_lt_bytearray',
        'test_lt_bytes',
        'test_lt_class',
        'test_lt_complex',
        'test_lt_frozenset',

        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_frozenset',
        'test_multiply_list',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_ne_bytearray',
        'test_ne_bytes',
        'test_ne_class',
        'test_ne_complex',
        'test_ne_frozenset',

        'test_or_bytearray',
        'test_or_bytes',
        'test_or_class',
        'test_or_complex',
        'test_or_frozenset',

        'test_power_bytearray',
        'test_power_bytes',
        'test_power_class',
        'test_power_complex',
        'test_power_frozenset',

        'test_rshift_bytearray',
        'test_rshift_bytes',
        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_frozenset',

        'test_subscr_bytearray',
        'test_subscr_bytes',
        'test_subscr_class',
        'test_subscr_complex',
        'test_subscr_frozenset',

        'test_subtract_bytearray',
        'test_subtract_bytes',
        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_frozenset',

        'test_true_divide_bytearray',
        'test_true_divide_bytes',
        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_frozenset',

        'test_xor_bytearray',
        'test_xor_bytes',
        'test_xor_class',
        'test_xor_complex',
        'test_xor_frozenset',
    ]


class InplaceDictOperationTests(InplaceOperationTestCase, TranspileTestCase):
    values = ["{}", "{'a': 1, 'b': 'value', 'c': 1.2345}"]

    not_implemented = [
        'test_add_bytearray',
        'test_add_bytes',
        'test_add_class',
        'test_add_complex',
        'test_add_frozenset',

        'test_and_bool',
        'test_and_bytearray',
        'test_and_bytes',
        'test_and_class',
        'test_and_complex',
        'test_and_dict',
        'test_and_float',
        'test_and_frozenset',
        'test_and_int',
        'test_and_list',
        'test_and_none',
        'test_and_set',
        'test_and_str',
        'test_and_tuple',

        'test_floor_divide_bytearray',
        'test_floor_divide_bytes',
        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_lshift_bool',
        'test_lshift_bytearray',
        'test_lshift_bytes',
        'test_lshift_class',
        'test_lshift_complex',
        'test_lshift_dict',
        'test_lshift_float',
        'test_lshift_frozenset',
        'test_lshift_int',
        'test_lshift_list',
        'test_lshift_none',
        'test_lshift_set',
        'test_lshift_str',
        'test_lshift_tuple',

        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_frozenset',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_class',
        'test_multiply_complex',
        'test_multiply_frozenset',

        'test_or_bool',
        'test_or_bytearray',
        'test_or_bytes',
        'test_or_class',
        'test_or_complex',
        'test_or_dict',
        'test_or_float',
        'test_or_frozenset',
        'test_or_int',
        'test_or_list',
        'test_or_none',
        'test_or_set',
        'test_or_str',
        'test_or_tuple',

        'test_power_bool',
        'test_power_bytearray',
        'test_power_bytes',
        'test_power_class',
        'test_power_complex',
        'test_power_dict',
        'test_power_float',
        'test_power_frozenset',
        'test_power_int',
        'test_power_list',
        'test_power_none',
        'test_power_set',
        'test_power_str',
        'test_power_tuple',

        'test_rshift_bool',
        'test_rshift_bytearray',
        'test_rshift_bytes',
        'test_rshift_class',
        'test_rshift_complex',
        'test_rshift_dict',
        'test_rshift_float',
        'test_rshift_frozenset',
        'test_rshift_int',
        'test_rshift_list',
        'test_rshift_none',
        'test_rshift_set',
        'test_rshift_str',
        'test_rshift_tuple',

        'test_subtract_bytearray',
        'test_subtract_bytes',
        'test_subtract_class',
        'test_subtract_complex',
        'test_subtract_frozenset',

        'test_true_divide_bytearray',
        'test_true_divide_bytes',
        'test_true_divide_class',
        'test_true_divide_complex',
        'test_true_divide_frozenset',

        'test_xor_bool',
        'test_xor_bytearray',
        'test_xor_bytes',
        'test_xor_class',
        'test_xor_complex',
        'test_xor_dict',
        'test_xor_float',
        'test_xor_frozenset',
        'test_xor_int',
        'test_xor_list',
        'test_xor_none',
        'test_xor_set',
        'test_xor_str',
        'test_xor_tuple',
    ]
