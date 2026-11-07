# Bark

A real visual game creation editor built on **PenguinMod**, **TurboWarp** and **Scratch**. Bark retains the upstream SVG block editor, scripting VM/compiler, paint editor, sound editor, sprites, clones, variables, lists, advanced custom blocks and project formats.

**Website:** https://kevinkevinsonbooyah.github.io/Bark/  
**Repository:** https://github.com/KevinKevinsonBooyah/Bark

## Bark changes

- Dark by default, Bark toolbar, paw icon and original dog sprite with a generated sound.
- Run/stop, device saves, a saved-project list, .pmp export and 12-second recovery snapshots after edits. The recovery prompt preserves the previous session until you recover it or save another project. Export is the portable backup; clearing browser storage deletes device saves. Device saves with the same project title replace the previous save of that title.
- Three editable examples: Bouncing Bark, Broadcast Party, Follow Your Finger.
- Workspace search, undo/redo controls, help and reduced-motion preference.
- Responsive editor, stage/sprite toggles, portrait rotation prompt, safe-area padding, and scrolling short-screen custom-block dialogs with the preview kept visible.
- On touch devices, the existing palette-collapse addon uses category taps. The inherited Blockly engine supplies touch dragging, nesting, panning and context menus.
- Stable five-finger slots independent of browser touch identifiers; touch cancellation releases the affected finger. Editor touches do not become stage touches.
- Upstream sharing, analytics and automatic log-capture removed; cloud variables require an explicitly provided server.

## What is verified

The production Webpack build succeeds. The headless tests exercise the real VM/compiler: green-flag execution, repeat and movement in compiled/interpreted modes; custom number parameters and a real return (`7 + 8 = 15`); custom color/return serialization and reload; executable branch parameters; broadcast-and-wait across sprites; list operations; and independent multitouch positions/releases.

The browser supplied for this development session cannot initialize WebGL and displays the upstream browser compatibility screen. **Visual rendering, sound output, drag/snapping, mobile gestures, modal fit, browser storage recovery and fullscreen behavior have not been end-to-end verified.** The automated runtime tests do not pretend to test those. A WebGL-capable browser is required.

This is a working PenguinMod-based editor build, not a claim that every requested feature is independently finished or tested. The full upstream block library is retained, including compiler-only advanced control blocks. An exhaustive per-block behavioral audit, touch pinch-zoom validation, custom-parameter reordering validation, broad mobile-device QA and long-project performance measurements remain outstanding. Some advanced blocks (including returning functions) depend on the compiler. Do not disable it for these projects.

Microphone and clipboard access depend on browser permissions. Optional extensions and remote asset libraries need network access. There is no Bark account, cloud save or public project-hosting service. Importing a PenguinMod project does not make its extra blocks compatible with standard Scratch.

## Reproduce the build

Requires Node 22, Python 3 and Git.

```sh
node scripts/bootstrap.cjs
cd engine
npm ci --ignore-scripts --legacy-peer-deps
node scripts/runtime-tests.cjs
NODE_ENV=production ROOT=/Bark/ NODE_OPTIONS="--openssl-legacy-provider --max-old-space-size=6144" npx webpack --bail
```

The repository stores the Bark source changes as `bark.patch` against the exact open-source GUI revision in `upstream.json`. The bootstrap materializes all editor source in `engine/`; the normalized manifest and lockfile pin dependencies to source archives and avoid obsolete Git prepare scripts. Edit the materialized source normally and update the patch for a release. The Pages workflow runs tests, builds and includes the corresponding source download.

## GitHub Pages

The workflow builds on `main` and deploys to `/Bark/`. If GitHub rejects automatic Pages enablement, the owner must open **Settings → Pages → Source → GitHub Actions** once, then rerun the failed deployment job. Build artifacts are retained even if Pages is not yet enabled. The URL above should only be described as live after the deploy job succeeds and its content is checked.

## License and credits

GPL-3.0. See [LICENSE](LICENSE) and [THIRD_PARTY.md](THIRD_PARTY.md). Original PenguinMod, TurboWarp, Scratch and Scratch Addons credit and licensing notices remain in the materialized source. Bark is independently modified and is not an official release of those projects.
