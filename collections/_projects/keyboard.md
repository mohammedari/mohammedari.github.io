---
layout: project-right # alternative layouts: project, project-left, project-right, project-top
title: "Keyboard Design"
description: "Designing a self-made computer keyboard kit to seek an end game one."
date: 2025-02-21
weight: 1
thumbnail: "/assets/images/gen/projects/keyboard/thumbnail.webp"
#categories: ["Keyboard"]
#client: ""
role: "Mechanical and Electrical Design; Software Development"
gallery:
  - image: "/assets/images/gen/projects/keyboard/thumbsplit60ble.webp"
    caption: "<strong>Thumbsplit 60 BLE:</strong> Fully wireless split keyboard that supports standard 104 layout keycaps using custom-design stabilizers."
  - image: "/assets/images/gen/projects/keyboard/thumbsplit58-ble.webp"
    caption: "<strong>Thumbsplit 58 BLE:</strong> Fully wireless split keyboard with enhanced switch height to support various keycaps with low profile swithes."
  - image: "/assets/images/gen/projects/keyboard/thumbsplit58-wired.webp"
    caption: "<strong>Thumbsplit 58 Wired:</strong> Wired split keyboard with enhanced switch height, wired variant of BLE version."
  - image: "/assets/images/gen/projects/keyboard/thumbsplit58.webp"
    caption: "<strong>Thumbsplit 58:</strong> My first designed wireless split keyboard with dongle layout."
---

I was originally fascinated by computer input devices and used a ThinkPad keyboard for many years. After suffering from tendonitis and shoulder pain, I became interested in split keyboards and ultimately designed my own in pursuit of the “endgame” keyboard.

I handle enclosure design using CAD, the electrical design of the internal PCB (including a wireless module), and firmware development based on open-source software such as [QMK](https://qmk.fm/) and [ZMK](https://zmk.dev/).

List of designed keyboards:

| Name                    | Release   | Repositories |
|-------------------------|-----------|--------------|
| Thumbsplit 60 BLE       | Jan. 2025 | [Firmware](https://github.com/mohammedari/thumbsplit60ble-zmk-config) |
| Thumbsplit 58 Wired/BLE | Nov. 2021 | [Wired Firmware](https://github.com/mohammedari/qmk_firmware/tree/oneoff/thumbsplit58w/keyboards/thumbsplit58w) [BLE Firmware](https://github.com/mohammedari/zmk/tree/oneoff/thumbsplit58ble/app/boards/arm/thumbsplit58ble) |
| Thumbsplit 58           | Dec. 2020 | [Hardware](https://github.com/mohammedari/thumbsplit58-hardware) [Dongle Firmware](https://github.com/mohammedari/thumbsplit58-firmware) [Firmware](https://github.com/mohammedari/qmk_firmware/tree/oneoff/thumbsplit58/keyboards/thumbsplit58) |
