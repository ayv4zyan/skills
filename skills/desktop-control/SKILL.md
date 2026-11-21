---
name: desktop-control
description: >
  Drive the user's real Hyprland desktop with genuine input: move and click the pointer, drag,
  scroll, type, and take screenshots. Use to verify GUI work in the real app (offscreen or
  synthetic test events can pass while the real app fails), to reproduce a reported UI bug, or to
  screenshot a running window.
---

# Desktop control

`desk` (in this skill's folder) sends **real** input: a virtual mouse on `/dev/uinput` that Hyprland
treats as hardware, keys through `wtype`, and screenshots through `grim`. Events take the same path
as the user's own mouse, so what you see is what they get. Run `<this folder>/desk help` for the
commands.

Needs: Hyprland with Lua dispatchers (0.56+), `python3`, `grim`, `wtype`, `magick` (for crops),
and write access to `/dev/uinput` (`getfacl /dev/uinput` should list the user). If any is missing,
tell the user what to install or grant instead of working around it.

## Steps

1. **Ask first.** The pointer is the user's: while `desk` runs, they must keep their hands off the
   mouse and keyboard and leave the target window uncovered. Ask for that, and wait for a yes. A
   window popping up over the test area or the cursor moving on its own means they're active:
   `desk stop` and ask again.
2. **Use your own test window.** Launch a separate instance of the app on a test file, with an
   isolated config so it can't overwrite the user's settings (e.g. last opened file):
   `XDG_CONFIG_HOME=<scratchpad>/config ./app <scratchpad>/test.file &`. Clicks land only inside
   that window; the user's own windows and files stay out of it.
3. `desk start` (saves the cursor and the focused window), then `read X Y W H < <(desk win 'TITLE-REGEX')` to get the
   window. Compute targets from it: screen coordinates are global logical pixels.
4. Act and **look**. Take a `desk shot before.png PATTERN`, do one action, take
   `desk shot after.png PATTERN`, then Read the images. Compare what changed against what should
   change. `cmp -s` tells "something changed" but not *what*: crop with `magick` to inspect a region.
   When you need to know *why*, add temporary `console.log`/`qDebug` to the app, read its stderr
   (`QT_FORCE_STDERR_LOGGING=1` for Qt), then remove the logging.
5. `desk stop` (restores the cursor and focus) and close the test window. Done when the screenshots show
   the intended behaviour for every case you changed, and the user's cursor is back.

## Gotchas

- **Qt on Wayland reports mouse wheels as a "touchpad" device** (type 4, `pixelDelta` 15 per notch,
  no scroll phase). A Qt Quick `WheelHandler` ignores it unless
  `acceptedDevices: PointerDevice.AllDevices`. QTest events default to "Mouse", so offscreen tests
  miss this. To catch it there, build the `QWheelEvent` with a `QPointingDevice` of type `TouchPad`.
- `desk wheel` takes the direction **as the app sees it**, and flips for you when Hyprland's
  `natural_scroll` is on.
- Hyprland 0.56+ uses Lua dispatchers: `hyprctl dispatch 'hl.dsp.cursor.move({x=1,y=2})'`.
  Old-style `dispatch movecursor X Y` fails, and with output sent to `/dev/null` it fails silently.
  Check what a dispatcher prints (`ok`).
- Warping the cursor sends the app no motion event; `desk` adds a 1 px wiggle so hover and enter
  fire.
- A uinput device created per action loses its first events; `desk` keeps one device alive between
  `start` and `stop`.
- Keys go to the **focused** window: `desk focus 'title:e2e.*'` before `desk key` / `desk type`.
  The regex must match the **whole** title or class (`title:^e2e` fails, `title:e2e.*` works).
