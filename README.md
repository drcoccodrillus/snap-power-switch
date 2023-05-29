# PowerSwitch

Reboot or shutdown Ubuntu Core systems using curl.


## Utilities
This snap provides a simple set of API to reboot or shutdown an Ubuntu Core system using curl.

***

## Snap building
The snap can be built using snapcraft. The snapcraft.yaml file is located in the snap directory. To build the snap, use the following command:

`snapcraft`

Remember to put yourself in the snap-power-switch directory before running the command.

## Snap installation
The installation process is pretty straight forward and you can install the snap in two different ways:
- From the snap store
- From a local file

The easiest way is to install the snap from the snap store. To do so, use the following command:

`snap install powerswitch`


If you prefer to install the snap from a local file, follow the instructions below.

For installing the snap in devmode from a local file, use the following command:

`snap install powerswitch_0.1_amd64.snap --dangerous --devmode`

For installing the snap in confined mode from a local file, use the following command:

`snap install powerswitch_0.1_amd64.snap --dangerous`

## Snap configuration
After installing the snap, you need to connect the snap to the following interfaces:
- `snap connect powerswitch:shutdown`

## Usage
Using the snap is pretty straight forward. 

System reboot: curl `http://target-ip-address:3500/reboot`

System shutdown: curl `http://target-ip-address:3500/poweroff`
