# Bark source and attribution

Bark modifies PenguinMod's editor. It is not an official PenguinMod, TurboWarp or Scratch release and is not affiliated with the Scratch Foundation. Original authorship and license notices are retained.

- PenguinMod GUI: https://github.com/PenguinMod/penguinmod.github.io — GPL-3.0, pinned in upstream.json.
- PenguinMod Blocks, Paint, VM, Render, Audio, Storage, SVG renderer and related libraries: exact archive URLs and commits are in upstream-dependencies.json and engine-package-lock.json. Each package's LICENSE and source headers govern its files; metadata in older package.json files is not a substitute for those licenses.
- TurboWarp: https://github.com/TurboWarp — upstream compiler, editor and runtime work retained with its notices.
- Scratch: https://github.com/scratchfoundation — original editor, VM, renderer, audio, storage and Blockly-derived block system; original notices retained.
- Scratch Addons contributors: bundled addon manifests retain their credits and source headers.

Bark's modifications, original dog vector, generated sound, examples, build recipe and tests are distributed under GPL-3.0. The complete GUI source is obtained by `node scripts/bootstrap.cjs`; it applies the human-readable bark.patch to the exact upstream commit. No upstream source is obfuscated by Bark. The built site also offers `source/bark-source.tar.gz`, containing the materialized GUI source, dependency lockfile and build configuration. Install dependencies from their pinned public source archives to rebuild. The repository includes the full GPL-3.0 license.

The public asset libraries and optional extensions are external providers. They have their own availability and license terms. Core new projects and bundled examples contain local assets. Bark removes upstream Google Analytics, automatic log capture and the community upload button. No Bark account service or cloud-variable backend is configured.
