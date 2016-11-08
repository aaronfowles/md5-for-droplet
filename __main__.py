#! /usr/bin/python

from subprocess import check_output
import os
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Obtain md5 hash from id_rsa.pub')
    parser.add_argument('-f','--file',help='Full path to id_rsa.pub. E.g. /<path>/id_rsa.pub', required=True)
    args = vars(parser.parse_args())
    fpath = args['file']
    fs = fpath
    key = None
    fopen = None
    for f in fs:
        try:
            fopen = fpath
        except:
            pass
        finally:
            if (fopen == None):
                sys.stderr.write('No ssh key found at this location')
                sys.exit(1)
    md5_output = check_output(['ssh-keygen','-E','md5','-lf',fopen])
    start_point = md5_output.index(':')
    md5_output = md5_output[start_point+1:md5_output.index(' ',start_point+1)]
    sys.stdout.write(md5_output)
    sys.exit(0)
