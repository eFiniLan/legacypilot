import os
from typing import cast

from openpilot.system.hardware.base import HardwareBase
from openpilot.system.hardware.tici.hardware import Tici
from openpilot.system.hardware.eon.hardware import Android
from openpilot.system.hardware.pc.hardware import Pc

TICI = os.path.isfile('/TICI')
AGNOS = os.path.isfile('/AGNOS')
EON = os.path.isfile('/EON')
PC = not (EON or TICI)


if TICI:
  HARDWARE = cast(HardwareBase, Tici())
elif EON:
  HARDWARE = cast(HardwareBase, Android())
else:
  HARDWARE = cast(HardwareBase, Pc())
