# Bark

An original browser block-coding studio with a brown theme, connected puzzle blocks, and a solid white starting stage.

Open **https://kevinkevinsonbooyah.github.io/Bark/**.

The editor, runtime, renderer, project format, and costume studio are implemented in this repository. The deployed app does not use PenguinMod, Scratch VM, Blockly, a CDN, or an external runtime. Earlier versions remain in Git history.

## Editing

Drag a block itself from the palette onto the canvas. Drop near a connection to snap it into a stack or a loop mouth. Drag an existing block to detach it with everything below it. Stacks can be placed anywhere; positions are saved. Drag reporters into white or Boolean sockets, and drag them back out. Pan blank space and use the zoom controls. Tap-to-add remains available for phones. Select a block to duplicate, move, delete, or reorder it; undo restores edits.

The catalogue includes events, motion, looks, sound, control, sensing, operators, variables, lists, and custom blocks. `BLOCKS.md` lists every available definition. Expandable operator blocks have plus/minus inputs, and the expandable if block has additional else-if branches.

Make a Block supports named number/text, Boolean, branch, and label inputs; colors; ending blocks; return values; and run-without-refresh. Use a named parameter reporter or Run branch inside its definition. Finite warp code executes without intermediate redraws; waits and the safety budget still yield. Reporter functions must finish without waiting.

## Costumes and sounds

The costume studio follows the supplied reference's arrangement: costume thumbnails, two toolbar rows, fill/outline controls, a tool rail, checkerboard canvas, and zoom/bitmap controls. It includes brush, eraser, shapes, text, selection, marquee, movement, resize, rotation, grouping, layer order, flips, center, clipboard operations, and brush-point reshape. Imported images become selectable objects. Merge, Mask, Subtract, and grayscale Filter rasterize their selected results; undo can restore the vectors.

Sounds can be uploaded and previewed, with runtime playback, offsets, fade-out, volume, pitch, and stereo pan. The default Bark sound is synthesized. Microphone sensing is opt-in in the Sounds panel. Clipboard operations depend on browser permission. Named solid-color backdrops are managed beside the stage.

## Mobile and saving

Code, Play, Costumes, and Sprites have separate phone views. Touch pointers drive block dragging and drawing; on-screen arrow and Space controls support keyboard projects. Toolbars scroll on narrow screens and costumes initially fit the available space. Fresh projects start with a white 480×360 stage. Run uses a copy of saved starting state.

Projects autosave locally. Export `.bark` files for backups. Bark's own format is not compatible with `.sb3` or `.pmp` projects. There is no account service: logged-in reports false and username is blank unless set in project data. Sprite collision is approximate; color sensing samples rendered pixels. The costume tools are an original implementation, not feature-for-feature PenguinMod paint parity: paths do not have Bézier handles, bitmap fill is object recoloring, and Boolean paint operations flatten their output. Regular expressions intentionally exclude groups, counted repetitions, and backreferences.

## Development and validation

No npm installation is needed. Use Node 20+:

```sh
npm test
node build.mjs
python3 -m http.server 8000 --directory dist
```

GitHub Actions tests, builds, and deploys `dist/` to Pages. `editor.html` is an alias for old bookmarks. The test suite covers 35 interpreter and model scenarios, including nested reporters, loop control, custom return/branch inputs, cloning, broadcasts, lists, sound completion hooks, warp scheduling, and saved workspace coordinates. Browser checks cover free placement, stack snapping, nested reporter drops, editing, costume drawing/grouping, and phone layouts at 390×844, 320×568, and 844×390. These are viewport checks, not testing on every physical phone.
