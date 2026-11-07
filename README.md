# Bark

A small, original block-coding studio for making animations and games. Open **https://kevinkevinsonbooyah.github.io/Bark/**.

Bark's editor, interpreter, renderer, project model, and costume tools are implemented here from scratch with browser APIs. No PenguinMod, Scratch VM, Blockly, WebGL, external runtime, build dependency, CDN, or account is required. The previous PenguinMod-based version remains in Git history; it is no longer used by the deployed app.

## Create

- Gold event hats start scripts on Run, a sprite tap, a key press, or a message.
- Add blocks by tapping the library, or drag their dotted handles into an insertion gap. Select a block to move, duplicate, or delete it. Loop and condition pockets accept nested blocks.
- White inputs accept values. Green reporter sockets support nested math, random numbers, variables, function input, comparisons, Boolean logic, timer, position, keyboard, touch, and approximate sprite collision sensing.
- Custom blocks have one parameter; define a named block and call it with a value. Use the function-input reporter inside its definition. Recursion and instruction limits keep scripts cooperative.
- Draw costumes using brush, eraser, line, rectangle, and ellipse tools. Multiple costumes, image import, duplication, transparent pixels, and undo are supported.
- Run executes a copy of your project. Stop restores starting positions. The white stage is 480×360, with centered x/y coordinates. Drag sprites on the stopped stage to place them.
- Phones have Code, Play, Costumes, and Sprites views. Both orientations are supported. Tap-to-place avoids precision dragging. Play includes arrow and Space controls.
- The current project autosaves in local storage. Export `.bark` JSON files to back up all scripts and costume assets. Storage failures are shown rather than silently claiming success.

## Develop

Requires Node 20+ for tests/build; no npm installation is needed.

```sh
npm test
node build.mjs
python3 -m http.server 8000 --directory dist
```

GitHub Actions runs the tests, builds static files, and deploys `dist/` to Pages. `editor.html` remains an alias for old bookmarks.

## Validation and limits

13 interpreter/model tests cover nested control flow, cancellation, arithmetic, events, broadcasts, custom inputs, pointer sensing, glides, costumes, sound scheduling, project roundtrip, validation, and recursion limits. Browser checks exercised editing inputs, nesting, running, phone tap placement, costume drawing, and layouts at 390×844, 844×390, and 320×568. These are browser viewport checks, not a claim of testing on every physical phone.

This is a new, smaller engine with its own project format. `.sb3` and `.pmp` imports are not supported. Custom blocks have one input and no return value; sound uses synthesized notes rather than recorded samples. Sprite collision uses approximate bounding circles. Imported project limits are 15 MB, 100 sprites, 100 costumes per sprite, and 2,500 code blocks. Device storage is browser-specific and may be cleared, so keep exports.
