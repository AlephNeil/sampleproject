from pegger import getReport
from sys import argv
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('extension')
    ap.parse_args(argv)

if __name__=='__main__':
    main()