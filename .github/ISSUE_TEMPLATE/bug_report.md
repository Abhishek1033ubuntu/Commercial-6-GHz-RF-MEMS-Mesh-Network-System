---
name: Bug report
about: Create a report to help us improve the firmware driver or hardware layout
title: '[BUG] '
labels: ''
assignees: ''
---

**Describe the bug**
A clear and concise description of what the bug is.

**Hardware / Firmware Context**
- PCB Revision: Rev 1.1 (Rogers RO4350B)
- Kernel Version: OpenWrt 23.05 / Linux 6.1
- RF-MEMS IC: Menlo Micro MM5130

**To Reproduce**
Steps to reproduce the behavior:
1. Load driver `insmod mems_mesh_driver.ko`
2. Trigger sector change...
3. See error

**Expected behavior**
Cold-switching queue pause should complete within <10 µs.
