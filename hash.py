#!/usr/bin/python3

import json
import os
import hashlib

PLUGIN_VERSION="1"

HEARTBEAT="true"

FILE_NAME=""

HASH_TYPE=""

def get_data(FILE_NAME,HASH_TYPE):
    data={}
    data['plugin_version']=PLUGIN_VERSION
    data['heartbeat_required']=HEARTBEAT
    try:
        fname=FILE_NAME.split('/')
        data["file_name"]=fname[-1]
        if HASH_TYPE=="blake2b":
            data["hashing"]=hashlib.blake2b(open(FILE_NAME,'rb').read()).hexdigest()
        elif HASH_TYPE=="blake2s":
            data["hashing"]=hashlib.blake2s(open(FILE_NAME,'rb').read()).hexdigest()
        elif HASH_TYPE=="md5":
            data["hashing"]=hashlib.md5(open(FILE_NAME,'rb').read()).hexdigest()
        elif HASH_TYPE=="sha1":
            data["hashing"]=hashlib.sha1(open(FILE_NAME,'rb').read()).hexdigest()
        elif HASH_TYPE=="sha224":
            data["hashing"]=hashlib.sha224(open(FILE_NAME,'rb').read()).hexdigest()
        elif HASH_TYPE=="sha256":
            data["hashing"]=hashlib.sha256(open(FILE_NAME,'rb').read()).hexdigest()
        elif HASH_TYPE=="sha384":
            data["hashing"]=hashlib.sha384(open(FILE_NAME,'rb').read()).hexdigest()
        elif HASH_TYPE=="sha3_224":
            data["hashing"]=hashlib.sha3_224(open(FILE_NAME,'rb').read()).hexdigest()
        elif HASH_TYPE=="sha3_256":
            data["hashing"]=hashlib.sha3_256(open(FILE_NAME,'rb').read()).hexdigest()
        elif HASH_TYPE=="sha3_384":
            data["hashing"]=hashlib.sha3_384(open(FILE_NAME,'rb').read()).hexdigest()
        elif HASH_TYPE=="sha3_512":
            data["hashing"]=hashlib.sha3_512(open(FILE_NAME,'rb').read()).hexdigest()
        elif HASH_TYPE=="sha512":
            data["hashing"]=hashlib.sha3_512(open(FILE_NAME,'rb').read()).hexdigest()

        name,extension=os.path.splitext(FILE_NAME)
        data["file_type"]=extension
        data["file_size"]=os.stat(FILE_NAME).st_size
        pass
    except Exception as e:
        data["status"]=0
        data["msg"]=str(e)
    return data

if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--filename',help="file to monitor",type=str)
    parser.add_argument('--hashtype',help="type of the hash",type=str)
    args=parser.parse_args()

    if args.filename:
        FILE_NAME=args.filename
    if args.hashtype:
        HASH_TYPE=args.hashtype
    data=get_data(FILE_NAME,HASH_TYPE)
    print(json.dumps(data,indent=4))
        



    
