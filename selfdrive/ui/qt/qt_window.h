#pragma once

#include <string>

#include <QApplication>
#include <QScreen>
#include <QWidget>

#ifdef QCOM2
#include <qpa/qplatformnativeinterface.h>
#include <wayland-client-protocol.h>
#include <QPlatformSurfaceEvent>
#endif

#include "system/hardware/hw.h"

const QString ASSET_PATH = ":/";
#ifdef QCOM
const QSize DEVICE_SCREEN_SIZE = {1920, 1080};
#else
const QSize DEVICE_SCREEN_SIZE = {2160, 1080};
#endif

void setMainWindow(QWidget *w);
