# -*- encoding: utf-8 -*-
import argparse
import logging
import sys
import transaction
from zope.component.hooks import getSite


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('scripts.example')

class Application(object):
    """
    Usage:
    ./bin/instance -O<plone_site_id> run scripts/example.py [--commit]
    """

    @classmethod
    def main(cls, args_):
        site = getSite()

        print "......."

        if args_.commit:
            print "commit transaction"
            transaction.commit()
        else:
            print "abort transaction (dry run)"
            transaction.abort()
        return 0

    @classmethod
    def run(cls):
        parser = argparse.ArgumentParser(description=cls.__doc__)
        parser.add_argument(
             '--commit',
             action='store_true',
        )
        sys.exit(cls.main(parser.parse_args(sys.argv[1:])))


if __name__ == "__main__":
    Application.run()

