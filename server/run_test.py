import unittest

import argparse

from test.models_ut import TodoTestCase
from test.resources_e2e import TodoResourceTestCase

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'type',
        help='The test type[ut|fn].')

    args = parser.parse_args()

    if args.type == 'ut':
        ut = unittest.TestLoader().loadTestsFromTestCase(TodoTestCase)
        unittest.TextTestRunner(verbosity=2).run(ut)

    if args.type == 'fn':
        fn = unittest.TestLoader().loadTestsFromTestCase(TodoResourceTestCase)
        unittest.TextTestRunner(verbosity=2).run(fn)
