import os
from typing import cast

from system.hardware.base import HardwareBase
from system.hardware.tici.hardware import Tici
from system.hardware.eon.hardware import Android
from system.hardware.pc.hardware import Pc

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
