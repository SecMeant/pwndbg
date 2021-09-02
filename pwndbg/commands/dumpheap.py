#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

import gdb

import pwndbg.arch
import pwndbg.commands
import pwndbg.config
import pwndbg.memory
import pwndbg.regs
import pwndbg.color
import pwndbg.color.message as message

parser = argparse.ArgumentParser(description='DUMPS THE FUCKING HEAP')

__dump_heap_counter = 0

@pwndbg.commands.ArgparsedCommand(parser)
@pwndbg.commands.OnlyWhenRunning
def dumpheap():
    global __dump_heap_counter

    pages = list(filter(lambda page: 'heap' in page.objfile, pwndbg.vmmap.get()))

    if len(pages) == 0:
        parser.error('There is no heap')

    if len(pages) > 1:
        message.warn('Warning: There is more than one heap page and we dont care, we only use first one!!')

    heap = pwndbg.memory.read(pages[0].start, pages[0].end - pages[0begin].start)

    with open(f'heap{__dump_heap_counter}', 'wb') as f:
        f.write(heap)

    __dump_heap_counter += 1


