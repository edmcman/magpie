#!/usr/bin/env python3
"""
Simple metric that measures the size of hello.cpp file.
Returns the file size in bytes as the fitness value.
For size optimization, magpie will try to minimize this value.
"""

from gradio_client import Client

def f():

    client = Client("https://ejschwartz-decompilation-metrics.hf.space/")
    result = client.predict(
            target_bytes="b8 2a 00 00 00 c3",
            source=open("hello.cpp", "r").read(),
            compiler="g++",
            flags="-O2",
            disasm_arch="i386",
            disasm_options="x86-64",
            api_name="/predict"
    )
    import pprint
    #pprint.pprint(result)
    return result[3]

if __name__ == "__main__":
    size = f()
    print(f"MAGPIE_FITNESS: {size}")
