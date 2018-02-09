import time
import random
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()


if available_ports:
    synth_port = [i for i, name in enumerate(available_ports) if "FLUID" in name][0]
    midiout.open_port(synth_port)
else:
    midiout.open_virtual_port("virt_port")

# Changes the instrument
# midiout.send_message([0xC0, 2])

pentatonic = [0, 2, 4, 7, 9]
def expand_scale(scale, octaves):
    expanded = []
    for i in octaves:
        for note in scale:
            expanded.append((i*12) + note)
    return expanded

full_pent = expand_scale(pentatonic, range(3, 6))

src = """
// SPDX-License-Identifier: GPL-2.0
/*
 *  linux/kernel/sys.c
 *
 *  Copyright (C) 1991, 1992  Linus Torvalds
 */

#include <linux/export.h>
#include <linux/mm.h>
#include <linux/utsname.h>
#include <linux/mman.h>
#include <linux/reboot.h>
#include <linux/prctl.h>
#include <linux/highuid.h>
#include <linux/fs.h>
#include <linux/kmod.h>
#include <linux/perf_event.h>
#include <linux/resource.h>
#include <linux/kernel.h>
#include <linux/workqueue.h>
#include <linux/capability.h>
#include <linux/device.h>
#include <linux/key.h>
#include <linux/times.h>
#include <linux/posix-timers.h>
"""

# for note in full_pent:
for char in "Die! Die! I hate the world!!!!!!!!!! Die!!!!!!!!":
    note = full_pent[ord(char) % len(full_pent)]
    # note = ord(char)
    note_on = [0x90, note, 127]
    note_off = [0x80, note, 0]
    midiout.send_message(note_on)
    time.sleep(0.15)
    midiout.send_message(note_off)
    time.sleep(0.005)

del midiout
