#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zencoding
import sys
from zen_editor import ZenEditor
import reflect

editor = ZenEditor()
try:
	args = sys.argv[2:]
except:
	args = []
	
zencoding.run_action(sys.argv[1], editor, *args)
