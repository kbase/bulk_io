#!/usr/bin/env python2.7
from __future__ import print_function # for python 2
from globus_sdk import TransferClient
import globus_sdk
import traceback
import argparse

parser = argparse.ArgumentParser(description='kbase share creator')
parser.add_argument('--share-dir', dest='sharedDir',
                 help='Directory to create a share on')
parser.add_argument('--share-name', dest='shareName', 
                 help='name for the share (must be unique among all globus shares)')

args = parser.parse_args()

tc = TransferClient() # uses transfer_token from the config file

shared_ep_data = {
  "DATA_TYPE": "shared_endpoint",
  "host_endpoint": 'e25a4bda-0636-11e6-a732-22000bf2d559',
  "host_path": args.sharedDir,
  "display_name": args.shareName,
  # optionally specify additional endpoint fields
  "description": "autocreated by kbase tool support"
}
tc.endpoint_autoactivate('e25a4bda-0636-11e6-a732-22000bf2d559', if_expires_in=3600)
create_result = tc.create_shared_endpoint(shared_ep_data)
endpoint_id = create_result["id"]
print("new endpoint id: ", endpoint_id)
