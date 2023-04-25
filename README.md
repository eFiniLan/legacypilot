# Legacypilot

This software includes contributions from [dragonpilot](https://github.com/dragonpilot-community/dragonpilot/tree/beta2) and [openpilot](https://github.com/commaai/openpilot).

NOTICE: legacypilot is not affiliated with comma.ai and is not an official comma.ai product. legacypilot is released under the terms of the MIT License. See the LICENSE file for more details.


## About

legacypilot is a side project that enables comma.ai EON and Comma Two devices to use the dragonpilot. This project was started after comma.ai deprecated support for the EON in version 0.7.9 and for Comma Two in version 0.8.13.1, in order to provide continued access to these devices.

legacypilot combines the Nuclear Grade Model with the latest openpilot (almost) codebase to create a hybrid solution. With the legacypilot project, we have stripped out nearly 99% of the dragonpilot code.


## Why use legacypilot

I have decided to make this side project open source for users who wish to:

* Port unsupported vehicles
* Evaluate end-to-end lateral and longitudinal control on previously unsupported vehicles
* Understand the limitations of legacy devices
* Experience pure openpilot (without the modifications of dragonpilot)
* Make their own EON/C2 fork without spending hundreds of hours reverting and testing code.

By making this project open source, I hope to alleviate some of the frustration and complaints about not being able to access the source code. However, I still encourage users to consider purchasing a [comma 3](https://shop.comma.ai) for the best and up-to-date openpilot experience.


## Limitations

* CAN-FD and BODY features are not supported due to outdated libraries in EON/C2 firmware.
* The driving AI model remains in version 0.8.16, as porting TinyGrad/PyOpenCL requires significant effort.
* The driver monitoring AI model remains in version 0.8.13.
* Navigation On Openpilot (NOO) is not supported, as it requires a newer driving model that is not currently available in legacypilot.
* Services are not optimized for resource usage, and using all services may result in overheating issues.
* Language files can only be generated in a PC due to missing Qt5 tools.

In summary, legacypilot is based on Openpilot 0.8.16 with the latest vehicle model support from the Openpilot master branch.

However, please note that this build is still in the experimental phase and may not be suitable for use as a daily driver. We recommend using the openpilot mastertwo branch for your daily driving needs.

Please see README_openpilot.md for the original readme.
