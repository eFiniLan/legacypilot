#include "selfdrive/loggerd/loggerd.h"

#include <sys/resource.h>

int main(int argc, char** argv) {
  if (Hardware::EON()) {
    setpriority(PRIO_PROCESS, 0, -20);
  }

  loggerd_thread();

  return 0;
}
