"""Wrapper for nose2"""

import argparse
import glob
import os
import shlex
import subprocess


def main():
    parser = argparse.ArgumentParser(description='nose2 wrapper script',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('tests', nargs='*',
                        help='Only run specified tests. Ex. tests.test_example \
                        Ex. tests.test_example.ExampleTestCase \
                        Ex. tests.test_example.ExampleTestCase.test_env1_config')
    parser.add_argument('--testenv', '-te', default='DEFAULT',
                        help='Case sensitive section in test_settings.cfg')
    parser.add_argument('--attr', '-A', nargs='+', help='Select tests by attribute. \
                        Args are logically OR\'d. Arg with comma delimeter(s) is AND\'d. \
                        Ex. slow tags=tag2 Ex. slow,tags=tag2')
    parser.add_argument('--quiet', '-q', action='store_true', default=False)
    parser.add_argument('--collect_only', '-c', action='store_true',
                        default=False, help='Collect and output test names, don\'t run tests')
    parser.add_argument('--xml', action='store_true',
                        default=False, help='Write test results xUnit XML')
    args = parser.parse_args()

    os.environ['PY_TEST_ENV'] = args.testenv

    # cleanup previous run
    for f in glob.glob('reports/*.xml'):
        os.remove(f)
    for f in glob.glob('log/*'):
        os.remove(f)
    for f in glob.glob('screenshots/*'):
        os.remove(f)

    cmd = 'python -m nose2 --config framework/nose2.cfg'

    if args.tests:
        cmd += ' ' + ' '.join(args.tests)

    if not args.quiet:
        cmd += ' -v'

    if args.collect_only:
        cmd += ' --collect-only'

    if args.attr:
        cmd += ' -A ' + ' -A '.join(args.attr)

    if args.xml:
        cmd += ' --junit-xml'

    cp = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(cp.stdout.decode('utf-8'))


if __name__ == "__main__":
    main()
