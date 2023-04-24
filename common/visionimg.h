#pragma once

#include "cereal/visionipc/visionbuf.h"

#ifdef QCOM
#include <GLES3/gl3.h>

#include <EGL/egl.h>
#define EGL_EGLEXT_PROTOTYPES
#include <EGL/eglext.h>
#undef Status

class EGLImageTexture {
 public:
  EGLImageTexture(const VisionBuf *buf);
  ~EGLImageTexture();
  GLuint frame_tex = 0;

  void *private_handle = nullptr;
  EGLImageKHR img_khr = 0;
};
#endif
