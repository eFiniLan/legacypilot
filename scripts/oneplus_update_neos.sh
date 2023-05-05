#!/usr/bin/bash

if [ -z "$BASEDIR" ]; then
  BASEDIR="/data/openpilot"
fi

source "$BASEDIR/launch_env.sh"
echo "Installing NEOS update"
NEOS_PY="$BASEDIR/system/hardware/eon/neos.py"
MANIFEST="$BASEDIR/system/hardware/eon/oneplus.json"
$NEOS_PY --swap-if-ready $MANIFEST
$BASEDIR/system/hardware/eon/updater $NEOS_PY $MANIFEST
