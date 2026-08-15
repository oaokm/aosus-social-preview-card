#!/usr/aosusSocialPreviewCardVenv/bin/python

import os, subprocess
COMMANDLINECURRENTPATH = os.getcwd()

from utils import (
    extractArticleID
)

from aosus_extracter import aosusExtracter
from social_card import html_to_image
import argparse, argcomplete
from body import htmlBody
from config import config

os.chdir(os.path.dirname(os.path.realpath(__file__)))

parser = argparse.ArgumentParser(description="", prog='Fasel-hd cli')

#* Generate Card section
generate = parser.add_argument_group('Generate Card Options')

generate.add_argument('-gen', "--generate", help="generate social preview card", type=str, metavar='<AOSUS URL>')


#* TCP/IP section
tcp = parser.add_argument_group('TCP/IP Options')

tcp.add_argument("--tcp_status",help="show tcp/ip status", action='store_true')
tcp.add_argument("--tcp_start",help="start tcp/ip server", action='store_true')
tcp.add_argument("--tcp_stop",help="stop tcp/ip server", action='store_true')



parser.add_argument("-v", '-V', "--version", action="version", version="1.0.0")

argcomplete.autocomplete(parser)
args = parser.parse_args()


if args.generate:
    id = extractArticleID(args.generate)
    cardPath = os.path.join(config.aosus_social_preview_card_dir_path, id+'.png')
    if not os.path.exists(cardPath):
        htmlBody(htmlTemplate='aosusTest', data=aosusExtracter(args.generate)._extractArtcleData()).setHTML()
        try:
            html_to_image(
                html_path='./htmlTemplate/aosusTest/test.html',
                output_path=cardPath
                )
        except AttributeError:
            print('this is not a aosus url!')
    else:
        print(f'already exists -> {cardPath} ')

elif args.tcp_start:
    subprocess.run('./tcp_start.sh')


elif args.tcp_status:
    subprocess.run('./tcp_status.sh')


elif args.tcp_stop:
    subprocess.run('./tcp_stop.sh')
