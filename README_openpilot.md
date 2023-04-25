


What is legacypilot?
------
Legacypilot is part of the dragonpilot project.

Since comma.ai deprecated support for the EON in version 0.7.9 and for Comma Two in version 0.8.13.1, the dragonpilot team has been working to enable these older devices to run on the latest openpilot version.

However, since version 0.8.16, the comma.ai team has migrated the driving machine learning module to run on the tingrad framework, which is not easy to run on the old devices.

dragonpilot on legacy devices combines the [Nuclear Grade Model](https://github.com/commaai/openpilot/tree/2f46fe5d856be0637cb55e460ea3f2d34be1703c/selfdrive/modeld/models) with the latest (almost) codebase to create a hybrid solution. With the legacypilot project, we have stripped out nearly 99% of the dragonpilot code.

I have decided to open up this side project for users who wish to:

* Port unsupported vehicles
* Evaluate end-to-end lateral and longitudinal control on previously unsupported vehicles
* Understand the limitations of legacy devices
* Experience pure openpilot (without the poison of dragonpilot)

We still encourage users to get a [comma 3](https://comma.ai/shop) for the best and up to date openpilot experience.


LIMITATION
------
* CAN-FD VEHICLES WILL NOT WORK: This is because the library in EON/C2 is outdated and cannot build Red Panda firmware.
* BODY WILL NOT WORK: This is also due to the library in EON/C2 being unable to build its firmware.
* DRIVING AI MODEL REMAINS IN 0.8.16: Porting TinyGrad/PyOpenCL onto EON/C2 requires significant effort, and we are still investigating workarounds.
* DRIVER MONITORING AI MODEL REMAINS IN 0.8.13.
* NOO (Navigation On Openpilot) WILL NOT WORK: NOO requires a newer driving model to work with the nav model. Until we address this issue, it will not work.
* SERVICES ARE NOT OPTIMIZED: New driving model uses more resources, having every service may result in overheating issues.

**In summary, consider this as Openpilot 0.8.16 with the latest vehicle model support from the Openpilot master branch.**

**The build is very rough, we recommend using the [openpilot mastertwo branch](https://github.com/commaai/openpilot/tree/commatwo_master) as daily driver.**



![](https://i.imgur.com/b0ZyIx5.jpg)

Table of Contents
=======================

* [What is openpilot?](#what-is-openpilot)
* [Running in a car](#running-on-a-dedicated-device-in-a-car)
* [Running on PC](#running-on-pc)
* [Community and Contributing](#community-and-contributing)
* [User Data and comma Account](#user-data-and-comma-account)
* [Safety and Testing](#safety-and-testing)
* [Directory Structure](#directory-structure)
* [Licensing](#licensing)

---

What is openpilot?
------

[openpilot](http://github.com/commaai/openpilot) is an open source driver assistance system. Currently, openpilot performs the functions of Adaptive Cruise Control (ACC), Automated Lane Centering (ALC), Forward Collision Warning (FCW), and Lane Departure Warning (LDW) for a growing variety of [supported car makes, models, and model years](docs/CARS.md). In addition, while openpilot is engaged, a camera-based Driver Monitoring (DM) feature alerts distracted and asleep drivers. See more about [the vehicle integration](docs/INTEGRATION.md) and [limitations](docs/LIMITATIONS.md).

<table>
  <tr>
    <td><a href="https://youtu.be/NmBfgOanCyk" title="Video By Greer Viau"><img src="https://i.imgur.com/1w8c6d2.jpg"></a></td>
    <td><a href="https://youtu.be/VHKyqZ7t8Gw" title="Video By Logan LeGrand"><img src="https://i.imgur.com/LnBucik.jpg"></a></td>
    <td><a href="https://youtu.be/VxiR4iyBruo" title="Video By Charlie Kim"><img src="https://i.imgur.com/4Qoy48c.jpg"></a></td>
    <td><a href="https://youtu.be/-IkImTe1NYE" title="Video By Aragon"><img src="https://i.imgur.com/04VNzPf.jpg"></a></td>
  </tr>
  <tr>
    <td><a href="https://youtu.be/iIUICQkdwFQ" title="Video By Logan LeGrand"><img src="https://i.imgur.com/b1LHQTy.jpg"></a></td>
    <td><a href="https://youtu.be/XOsa0FsVIsg" title="Video By PinoyDrives"><img src="https://i.imgur.com/6FG0Bd8.jpg"></a></td>
    <td><a href="https://youtu.be/bCwcJ98R_Xw" title="Video By JS"><img src="https://i.imgur.com/zO18CbW.jpg"></a></td>
    <td><a href="https://youtu.be/BQ0tF3MTyyc" title="Video By Tsai-Fi"><img src="https://i.imgur.com/eZzelq3.jpg"></a></td>
  </tr>
</table>


Running on a dedicated device in a car
------

To use openpilot in a car, you need four things
* A supported device to run this software: a [comma three](https://comma.ai/shop/products/three).
* This software. The setup procedure of the comma three allows the user to enter a URL for custom software.
The URL, openpilot.comma.ai will install the release version of openpilot. To install openpilot master, you can use installer.comma.ai/commaai/master, and replacing commaai with another GitHub username can install a fork.
* One of [the 200+ supported cars](docs/CARS.md). We support Honda, Toyota, Hyundai, Nissan, Kia, Chrysler, Lexus, Acura, Audi, VW, and more. If your car is not supported but has adaptive cruise control and lane-keeping assist, it's likely able to run openpilot.
* A [car harness](https://comma.ai/shop/products/car-harness) to connect to your car.

We have detailed instructions for [how to mount the device in a car](https://comma.ai/setup).

Running on PC
------

All openpilot services can run as usual on a PC without requiring special hardware or a car. You can also run openpilot on recorded or simulated data to develop or experiment with openpilot.

With openpilot's tools, you can plot logs, replay drives, and watch the full-res camera streams. See [the tools README](tools/README.md) for more information.

You can also run openpilot in simulation [with the CARLA simulator](tools/sim/README.md). This allows openpilot to drive around a virtual car on your Ubuntu machine. The whole setup should only take a few minutes but does require a decent GPU.

A PC running openpilot can also control your vehicle if it is connected to a [webcam](https://github.com/commaai/openpilot/tree/master/tools/webcam), a [black panda](https://comma.ai/shop/products/panda), and a [harness](https://comma.ai/shop/products/car-harness).

Community and Contributing
------

openpilot is developed by [comma](https://comma.ai/) and by users like you. We welcome both pull requests and issues on [GitHub](http://github.com/commaai/openpilot). Bug fixes and new car ports are encouraged. Check out [the contributing docs](docs/CONTRIBUTING.md).

Documentation related to openpilot development can be found on [docs.comma.ai](https://docs.comma.ai). Information about running openpilot (e.g. FAQ, fingerprinting, troubleshooting, custom forks, community hardware) should go on the [wiki](https://github.com/commaai/openpilot/wiki).

You can add support for your car by following guides we have written for [Brand](https://blog.comma.ai/how-to-write-a-car-port-for-openpilot/) and [Model](https://blog.comma.ai/openpilot-port-guide-for-toyota-models/) ports. Generally, a car with adaptive cruise control and lane keep assist is a good candidate. [Join our Discord](https://discord.comma.ai) to discuss car ports: most car makes have a dedicated channel.

Want to get paid to work on openpilot? [comma is hiring](https://comma.ai/jobs/).

And [follow us on Twitter](https://twitter.com/comma_ai).

User Data and comma Account
------

By default, openpilot uploads the driving data to our servers. You can also access your data through [comma connect](https://connect.comma.ai/). We use your data to train better models and improve openpilot for everyone.

openpilot is open source software: the user is free to disable data collection if they wish to do so.

openpilot logs the road-facing cameras, CAN, GPS, IMU, magnetometer, thermal sensors, crashes, and operating system logs.
The driver-facing camera is only logged if you explicitly opt-in in settings. The microphone is not recorded.

By using openpilot, you agree to [our Privacy Policy](https://comma.ai/privacy). You understand that use of this software or its related services will generate certain types of user data, which may be logged and stored at the sole discretion of comma. By accepting this agreement, you grant an irrevocable, perpetual, worldwide right to comma for the use of this data.

Safety and Testing
----

* openpilot observes ISO26262 guidelines, see [SAFETY.md](docs/SAFETY.md) for more details.
* openpilot has software-in-the-loop [tests](.github/workflows/selfdrive_tests.yaml) that run on every commit.
* The code enforcing the safety model lives in panda and is written in C, see [code rigor](https://github.com/commaai/panda#code-rigor) for more details.
* panda has software-in-the-loop [safety tests](https://github.com/commaai/panda/tree/master/tests/safety).
* Internally, we have a hardware-in-the-loop Jenkins test suite that builds and unit tests the various processes.
* panda has additional hardware-in-the-loop [tests](https://github.com/commaai/panda/blob/master/Jenkinsfile).
* We run the latest openpilot in a testing closet containing 10 comma devices continuously replaying routes.

Directory Structure
------
    .
    ├── cereal              # The messaging spec and libs used for all logs
    ├── common              # Library like functionality we've developed here
    ├── docs                # Documentation
    ├── opendbc             # Files showing how to interpret data from cars
    ├── panda               # Code used to communicate on CAN
    ├── third_party         # External libraries
    └── system              # Generic services
        ├── camerad         # Driver to capture images from the camera sensors
        ├── clocksd         # Broadcasts current time
        ├── hardware        # Hardware abstraction classes
        ├── logcatd         # systemd journal as a service
        ├── loggerd         # Logger and uploader of car data
        ├── proclogd        # Logs information from /proc
        ├── sensord         # IMU interface code
        └── ubloxd          # u-blox GNSS module interface code
    └── selfdrive           # Code needed to drive the car
        ├── assets          # Fonts, images, and sounds for UI
        ├── athena          # Allows communication with the app
        ├── boardd          # Daemon to talk to the board
        ├── car             # Car specific code to read states and control actuators
        ├── controls        # Planning and controls
        ├── debug           # Tools to help you debug and do car ports
        ├── locationd       # Precise localization and vehicle parameter estimation
        ├── manager         # Daemon that starts/stops all other daemons as needed
        ├── modeld          # Driving and monitoring model runners
        ├── monitoring      # Daemon to determine driver attention
        ├── navd            # Turn-by-turn navigation
        ├── test            # Unit tests, system tests, and a car simulator
        └── ui              # The UI

Licensing
------

openpilot is released under the MIT license. Some parts of the software are released under other licenses as specified.

Any user of this software shall indemnify and hold harmless Comma.ai, Inc. and its directors, officers, employees, agents, stockholders, affiliates, subcontractors and customers from and against all allegations, claims, actions, suits, demands, damages, liabilities, obligations, losses, settlements, judgments, costs and expenses (including without limitation attorneys’ fees and costs) which arise out of, relate to or result from any use of this software by user.

**THIS IS ALPHA QUALITY SOFTWARE FOR RESEARCH PURPOSES ONLY. THIS IS NOT A PRODUCT.
YOU ARE RESPONSIBLE FOR COMPLYING WITH LOCAL LAWS AND REGULATIONS.
NO WARRANTY EXPRESSED OR IMPLIED.**

---

<img src="https://d1qb2nb5cznatu.cloudfront.net/startups/i/1061157-bc7e9bf3b246ece7322e6ffe653f6af8-medium_jpg.jpg?buster=1458363130" width="75"></img> <img src="https://cdn-images-1.medium.com/max/1600/1*C87EjxGeMPrkTuVRVWVg4w.png" width="225"></img>

[![openpilot tests](https://github.com/commaai/openpilot/workflows/openpilot%20tests/badge.svg?event=push)](https://github.com/commaai/openpilot/actions)
[![codecov](https://codecov.io/gh/commaai/openpilot/branch/master/graph/badge.svg)](https://codecov.io/gh/commaai/openpilot)
