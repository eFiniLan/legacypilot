import os

from cereal import car
from openpilot.common.params import Params
from openpilot.system.hardware import PC, TICI, EON
from openpilot.selfdrive.manager.process import PythonProcess, NativeProcess, DaemonProcess

WEBCAM = os.getenv("USE_WEBCAM") is not None

def driverview(started: bool, params: Params, CP: car.CarParams) -> bool:
  return started or params.get_bool("IsDriverViewEnabled")

def notcar(started: bool, params: Params, CP: car.CarParams) -> bool:
  return started and CP.notCar

def iscar(started: bool, params: Params, CP: car.CarParams) -> bool:
  return started and not CP.notCar

def logging(started, params, CP: car.CarParams) -> bool:
  run = (not CP.notCar) or not params.get_bool("DisableLogging")
  return started and run

def ublox_available() -> bool:
  return True if EON else os.path.exists('/dev/ttyHS0') and not os.path.exists('/persist/comma/use-quectel-gps')

def ublox(started, params, CP: car.CarParams) -> bool:
  use_ublox = ublox_available()
  if use_ublox != params.get_bool("UbloxAvailable"):
    params.put_bool("UbloxAvailable", use_ublox)
  return started and use_ublox

def qcomgps(started, params, CP: car.CarParams) -> bool:
  return started and not ublox_available()

def always_run(started, params, CP: car.CarParams) -> bool:
  return True

def only_onroad(started: bool, params, CP: car.CarParams) -> bool:
  return started

def only_offroad(started, params, CP: car.CarParams) -> bool:
  return not started

procs = [
  NativeProcess("camerad", "selfdrive/camerad", ["./camerad"], driverview),
  NativeProcess("clocksd", "system/clocksd", ["./clocksd"], only_onroad),
  NativeProcess("logcatd", "system/logcatd", ["./logcatd"], only_onroad),
  NativeProcess("proclogd", "system/proclogd", ["./proclogd"], only_onroad),
  PythonProcess("logmessaged", "system.logmessaged", always_run),
  # PythonProcess("micd", "system.micd", callback=iscar),
  # PythonProcess("timezoned", "system.timezoned", enabled=not PC, offroad=True),

  DaemonProcess("manage_athenad", "selfdrive.athena.manage_athenad", "AthenadPid"),
  NativeProcess("dmonitoringmodeld", "selfdrive/hybrid_modeld", ["./dmonitoringmodeld"], driverview, enabled=(not PC or WEBCAM)),
  # NativeProcess("encoderd", "system/loggerd", ["./encoderd"]),
  # NativeProcess("stream_encoderd", "system/loggerd", ["./encoderd", "--stream"], onroad=False, callback=notcar),
  NativeProcess("loggerd", "selfdrive/loggerd", ["./loggerd"], logging),
  NativeProcess("modeld", "selfdrive/hybrid_modeld" if not Params().get_bool("dp_0813") else "selfdrive/legacy_modeld", ["./modeld"], only_onroad),
  # NativeProcess("mapsd", "selfdrive/navd", ["./mapsd"]),
  # NativeProcess("navmodeld", "selfdrive/modeld", ["./navmodeld"]),
  NativeProcess("sensord", "system/sensord", ["./sensord"], always_run if EON else only_onroad, enabled=not PC),
  NativeProcess("ui", "selfdrive/ui", ["./ui"], always_run, watchdog_max_dt=(5 if not PC else None)),
  NativeProcess("soundd", "selfdrive/ui/soundd", ["./soundd"], only_onroad),
  NativeProcess("locationd", "selfdrive/locationd", ["./locationd"], only_onroad),
  NativeProcess("boardd", "selfdrive/boardd", ["./boardd"], always_run, enabled=False),
  PythonProcess("calibrationd", "selfdrive.locationd.calibrationd", only_onroad),
  PythonProcess("torqued", "selfdrive.locationd.torqued", only_onroad),
  PythonProcess("controlsd", "selfdrive.controls.controlsd", only_onroad),
  PythonProcess("deleter", "selfdrive.loggerd.deleter", always_run),
  PythonProcess("dmonitoringd", "selfdrive.legacy_monitoring.dmonitoringd", driverview, enabled=(not PC or WEBCAM)),
  # PythonProcess("laikad", "selfdrive.locationd.laikad"),
  # PythonProcess("rawgpsd", "system.sensord.rawgps.rawgpsd", enabled=TICI, onroad=False, callback=qcomgps),
  # PythonProcess("navd", "selfdrive.navd.navd"),
  PythonProcess("pandad", "selfdrive.boardd.pandad", always_run),
  PythonProcess("paramsd", "selfdrive.locationd.paramsd", only_onroad),
  NativeProcess("ubloxd", "system/ubloxd", ["./ubloxd"], ublox, enabled=not PC),
  # PythonProcess("pigeond", "system.sensord.pigeond", enabled=TICI, onroad=False, callback=ublox),
  PythonProcess("plannerd", "selfdrive.controls.plannerd", only_onroad),
  PythonProcess("radard", "selfdrive.controls.radard", only_onroad),
  PythonProcess("thermald", "selfdrive.thermald.thermald", always_run),
  PythonProcess("tombstoned", "selfdrive.tombstoned", always_run, enabled=not PC),
  PythonProcess("updated", "selfdrive.updated", only_offroad, enabled=not PC),
  PythonProcess("uploader", "selfdrive.loggerd.uploader", only_offroad),
  # PythonProcess("statsd", "selfdrive.statsd", offroad=True),

  # debug procs
  NativeProcess("bridge", "cereal/messaging", ["./bridge"], notcar),
  # rick - webjoystick needs aiohttp, install additional modules manually: pip install aiohttp aiortc
  # PythonProcess("webjoystick", "tools.bodyteleop.web", onroad=False, callback=notcar),

  # EON only
  PythonProcess("rtshield", "selfdrive.rtshield", only_onroad, enabled=EON),
  PythonProcess("shutdownd", "system.hardware.eon.shutdownd", only_onroad, enabled=EON),
  PythonProcess("androidd", "system.hardware.eon.androidd", always_run, enabled=EON),
]

managed_processes = {p.name: p for p in procs}
