from sample import getReport
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('extension')
    args = ap.parse_args()
    print("\n".join(getReport(args.extension)))

if __name__=='__main__':
    main()