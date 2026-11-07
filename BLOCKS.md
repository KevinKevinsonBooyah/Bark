# Block catalogue

234 definitions. Inputs appear in braces. Labels are the editor’s vocabulary; see README for implementation limits.

## Events

- `start` — when ⚑ clicked (event/definition)
- `tap` — when this sprite clicked (event/definition)
- `key` — when {key} key pressed (event/definition)
- `receive` — when I receive {message} (event/definition)
- `broadcast` — broadcast {message}
- `stopclicked` — when ■ clicked (event/definition)
- `always` — always (event/definition)
- `whencondition` — when {condition} (event/definition)
- `keyhit` — when {key} key hit (event/definition)
- `wheel` — when mouse is scrolled {way} (event/definition)
- `backdrophat` — when backdrop switches to {name} (event/definition)
- `threshold` — when {sensor} > {value} (event/definition)
- `broadcastwait` — broadcast {message} and wait

## Motion

- `move` — move {steps} steps
- `turn` — turn ↻ {degrees} degrees
- `point` — point in direction {direction}
- `goto` — go to x {x} y {y}
- `glide` — glide {seconds} sec to x {x} y {y}
- `changex` — change x by {value}
- `changey` — change y by {value}
- `bounce` — if on edge, bounce
- `pointer` — go to touch / mouse
- `turnleft` — turn ↺ {degrees} degrees
- `gototarget` — go to {target}
- `changexy` — change by x {x} y {y}
- `glidetarget` — glide {seconds} secs to {target}
- `pointtarget` — point towards {target}
- `pointxy` — point towards x {x} y {y}
- `setx` — set x to {value}
- `sety` — set y to {value}
- `bouncetarget` — if touching {target}, bounce
- `rotation` — set rotation style {style}
- `stageedge` — move to stage {edge}
- `r_x` — x position (reporter)
- `r_y` — y position (reporter)
- `r_direction` — direction (reporter)

## Looks

- `say` — say {text}
- `sayfor` — say {text} for {seconds} sec
- `size` — set size to {value} %
- `grow` — change size by {value}
- `show` — show
- `hide` — hide
- `costume` — switch costume to {value}
- `next` — next costume
- `opacity` — set opacity to {value} %
- `think` — think {text}
- `thinkfor` — think {text} for {seconds} seconds
- `stopsay` — stop speaking
- `font` — set font to {font} with font size {size}
- `bubbleborder` — set border color to {color}
- `bubblewidth` — set text bubble border line width to {value}
- `r_bubblewidth` — bubble width (reporter)
- `r_bubbleheight` — bubble height (reporter)
- `backdrop` — switch backdrop to {name}
- `nextbackdrop` — next backdrop
- `stretch` — set stretch to x {x} y {y}
- `changestretch` — change stretch by x {x} y {y}
- `r_stretchx` — x stretch (reporter)
- `r_stretchy` — y stretch (reporter)
- `changeeffect` — change {effect} effect by {value}
- `seteffect` — set {effect} effect to {value}
- `tint` — set tint color to {color}
- `cleareffects` — clear graphic effects
- `r_effect` — {effect} effect (reporter)
- `r_tint` — tint color (reporter)
- `r_visible` — visible? (reporter)
- `showtarget` — show {target}
- `hidetarget` — hide {target}
- `r_targetvisible` — is {target} visible? (reporter)
- `layerfront` — go to {where} layer
- `layerchange` — go {where} {value} layers
- `layer` — go to layer {value}
- `layertarget` — go {where} {target}
- `r_layer` — layer (reporter)
- `r_costumenumber` — costume {what} (reporter)
- `r_backdropnumber` — backdrop {what} (reporter)
- `r_size` — size (reporter)
- `r_costumedimension` — {dimension} of {costume} (reporter)

## Control

- `wait` — wait {seconds} seconds
- `repeat` — repeat {times} times
- `forever` — forever
- `if` — if {condition} then
- `ifelse` — if {condition} then
- `until` — repeat until {condition}
- `stop` — stop this script
- `stopall` — stop all scripts
- `waitor` — wait {seconds} seconds or until {condition}
- `foreach` — for each {name} in {value}
- `forseconds` — for {seconds} seconds
- `breakloop` — escape loop
- `continueloop` — continue loop
- `switch` — switch {value}
- `case` — case {value}
- `default` — default
- `runbranch` — run branch {name}
- `inline` — run {name} inline
- `waituntil` — wait until {condition}
- `while` — while {condition}
- `allatonce` — all at once
- `as` — as {target}
- `try` — try to do
- `throw` — throw error {text}
- `r_error` — error (reporter)
- `stopother` — stop {what}
- `clonehat` — when I start as a clone (event/definition)
- `clone` — create clone of {target}
- `deleteclones` — delete clones of {target}
- `deleteclone` — delete this clone
- `r_isclone` — is clone? (reporter)
- `ifchain` — if {condition} then
- `nextcase` — run next case when {condition}

## Variables

- `set` — set {name} to {value}
- `change` — change {name} by {value}
- `r_variable` — {name} (reporter)
- `showvariable` — show variable {name}
- `hidevariable` — hide variable {name}

## Sound

- `tone` — play note {note} for {seconds} sec
- `playwait` — play sound {sound} until done
- `playsound` — start sound {sound}
- `stopsound` — stop sound {sound}
- `playoffsetwait` — play sound {sound} starting at {seconds} seconds until done
- `playoffset` — start sound {sound} starting at {seconds} seconds
- `playallsounds` — play all sounds
- `stopallsounds` — stop all sounds
- `fadeout` — set fade out to {seconds} seconds on {sound}
- `r_soundplaying` — is {sound} playing? (reporter)
- `r_soundlength` — length of {sound} (reporter)
- `changesoundeffect` — change {effect} effect by {value}
- `setsoundeffect` — set {effect} effect to {value}
- `clearsoundeffects` — clear sound effects
- `r_soundeffect` — {effect} effect (reporter)
- `changevolume` — change volume by {value}
- `volume` — set volume to {value} %
- `r_volume` — volume (reporter)

## My blocks

- `define` — define {name} with input {param} (event/definition)
- `call` — run {name} with {value}
- `return` — return {value}
- `r_customreturn` — {name} {value} (reporter)
- `r_param` — {name} (reporter)
- `setparam` — set {name} to {value}

## Sensing

- `r_touching` — touching {name} ? (reporter)
- `r_targettouching` — {target} touching {other} ? (reporter)
- `r_targettouchpoint` — {target} touching x {x} y {y} ? (reporter)
- `r_touchcolor` — touching color {color} ? (reporter)
- `r_colortouch` — color {first} is touching {second} ? (reporter)
- `r_targetcoord` — {axis} of touching {target} point (reporter)
- `r_distance` — distance to {target} (reporter)
- `r_distancepoints` — distance from {x} {y} to {x2} {y2} (reporter)
- `r_directionpoints` — direction to {x} {y} from {x2} {y2} (reporter)
- `ask` — ask {text} and wait
- `r_answer` — answer (reporter)
- `r_istext` — {value} is text? (reporter)
- `r_isnumber` — {value} is number? (reporter)
- `r_keydown` — key {name} pressed? (reporter)
- `r_keyhit` — key {name} hit? (reporter)
- `r_scrolling` — is mouse scrolling {way}? (reporter)
- `r_pressed` — mouse down? (reporter)
- `r_clicked` — mouse clicked? (reporter)
- `r_px` — mouse x (reporter)
- `r_py` — mouse y (reporter)
- `clipboard` — add {text} to clipboard
- `r_clipboard` — clipboard item (reporter)
- `dragmode` — set drag mode {mode}
- `r_draggable` — draggable? (reporter)
- `r_loudness` — loudness (reporter)
- `r_loud` — loud? (reporter)
- `resettimer` — reset timer
- `r_timer` — timer (reporter)
- `setproperty` — set {property} of {target} to {value}
- `r_property` — {property} of {target} (reporter)
- `r_date` — current {part} (reporter)
- `r_days` — days since 2000 (reporter)
- `r_mobile` — mobile? (reporter)
- `r_fingerdown` — finger {finger} down? (reporter)
- `r_fingertapped` — finger {finger} tapped? (reporter)
- `r_fingerx` — finger {finger} x (reporter)
- `r_fingery` — finger {finger} y (reporter)
- `r_username` — username (reporter)
- `r_loggedin` — logged in? (reporter)

## Operators

- `r_add` — {a} + {b} (reporter)
- `r_sub` — {a} − {b} (reporter)
- `r_mul` — {a} × {b} (reporter)
- `r_div` — {a} / {b} (reporter)
- `r_pow` — {a} ^ {b} (reporter)
- `r_root` — {a} √ {b} (reporter)
- `r_random` — pick random {a} to {b} (reporter)
- `r_clamp` — constrain {value} min {a} max {b} (reporter)
- `r_lerp` — interpolate {a} to {b} by {value} (reporter)
- `r_gt` — {a} > {b} (reporter)
- `r_gte` — {a} ≥ {b} (reporter)
- `r_lt` — {a} < {b} (reporter)
- `r_lte` — {a} ≤ {b} (reporter)
- `r_eq` — {a} = {b} (reporter)
- `r_neq` — {a} ≠ {b} (reporter)
- `r_bool` — {value} (reporter)
- `r_and` — {a} and {b} (reporter)
- `r_or` — {a} or {b} (reporter)
- `r_not` — not {a} (reporter)
- `r_newline` — new line (reporter)
- `r_tab` — tab character (reporter)
- `r_join` — join {a} {b} (reporter)
- `r_index` — index of {a} in {b} (reporter)
- `r_lastindex` — last index of {a} in {b} (reporter)
- `r_letter` — letter {a} of {b} (reporter)
- `r_letters` — letters from {a} to {b} of {text} (reporter)
- `r_length` — length of {text} (reporter)
- `r_contains` — {a} contains {b} ? (reporter)
- `r_startswith` — {a} starts with {b} ? (reporter)
- `r_endswith` — {a} ends with {b} ? (reporter)
- `r_replaceall` — in {text} replace all {a} with {b} (reporter)
- `r_replace` — in {text} replace first {a} with {b} (reporter)
- `r_regex` — match {text} with regex {pattern} flags {flags} (reporter)
- `r_casechange` — {text} to {style} (reporter)
- `r_mod` — {a} mod {b} (reporter)
- `r_round` — round {value} (reporter)
- `r_math` — {method} of {value} (reporter)
- `r_literal` — {value} (reporter)
- `r_ternary` — if {condition} then {a} else {b} (reporter)
- `r_mathchain` — {v0} {operator} {v1} (reporter)
- `r_comparechain` — {v0} {operator} {v1} (reporter)
- `r_logicchain` — {v0} {operator} {v1} (reporter)
- `r_joinchain` — join {v0} {v1} (reporter)

## Lists

- `listadd` — add {value} to {name}
- `listdelete` — delete {index} of {name}
- `listclear` — delete all of {name}
- `listinsert` — insert {value} at {index} of {name}
- `listreplace` — replace item {index} of {name} with {value}
- `r_listitem` — item {index} of {name} (reporter)
- `r_listindex` — item # of {value} in {name} (reporter)
- `r_listlength` — length of {name} (reporter)
- `r_listcontains` — {name} contains {value}? (reporter)
- `r_list` — {name} (reporter)
- `showlist` — show list {name}
- `hidelist` — hide list {name}
