# Langine
Author: Will Berard (https://github.com/WBgrok/)

A small and simple language engine for context free grammars.

## Overview

Uses weighted random string expansion to generate entertaining gobbledygook.

Let's say for instance we define the following objects:

adjective -> [("blue", 1), ("small", 1), ("ridiculous", 1)]

noun -> [("flower", 10), ("cat", 10), ("saucepan", 7), ("$adjective $noun", 5)]

where the above reads:

object -> [(value1, weight), (value2, weight)]

with values being any string, where if a word is preceded by $ we attempt to expand the entity. This, as in the example above, can be recursive.

This has defined a small (context-free grammar)[https://en.wikipedia.org/wiki/Context-free_grammar] - we can then ask for an object to be generated - this will be done expanding $-prefixed tags into their own strings, following the weightings, so for instance askng for a noun might return "cat" or "saucepan", with a smaller chance of somethign like "blue saucepan" or an even smaller one of "ridiculous small cat".


### Worked example - yoga instructions generator

Start simpple - import the package, and create a controller. Each phrase object must belong to one and only one controller, so that if a $phrase is encountered we can turn to it to ask it to look for such a prhase and render it.

```lang=py
import langine

yoga = langine.controller()

```

We then define phrases - in our case they're mostly individual words, but they can be full phrases, made of human language words, $-prefixed references to other phrases, or any combination of the two.

```lang=py
noun_group = langine.phrase(
  'ng',
  yoga,
  [
    ("$noun", 1),
    ("$adj $noun", 1)
  ],
)

noun = langine.phrase(
  'noun',
  yoga,
  [
    ("arm", 1),
    ("leg", 1),
    ("torso", 1),
    ("fingertip", 1),
    ("toes", 1),
    ("toe", 1),
    ("pelvis", 1),
    ("hip", 1),
    ("knee", 1),
    ("thigh", 1),
    ("back", 1),
    ("nostril", 1),
    ("collarbone", 1),
    ("wrist", 1),
    ("forearm", 1),
    ("eyeball", 1),
  ],
)

adj = langine.phrase(
  'adj',
  yoga,
  [
    ("left", 3),
    ("right", 3),
    ("upper right", 1),
    ("lower right", 1),
    ("upper left", 1),
    ("lower left", 1),
  ]
)

article = langine.phrase(
  'article',
  yoga,
  [
    ("the", 1),
    ("your", 1),
  ],
)

direction = langine.phrase(
  'dir',
  yoga,
  [
    ("towards", 2),
    ("away from", 2),
    ("in line with", 1),
    ("over", 1),
    ("across", 1),
  ],
)

verb = langine.phrase(
  'verb',
  yoga,
  [
    ("push", 3),
    ("pull", 3),
    ("breathe", 1),
    ("expand", 1),
    ("exhale", 1),
    ("inhale", 1),
    ("align", 2),
    ("release", 2),
    ("stretch", 1),
  ],
)

ph = langine.phrase(
  'phrase',
  yoga,
  [
    ("$verb $article $ng $dir $article $ng", 10),
    ("breathe through $article $noun", 2),
    ("and relax", 1),
    ("let $article $ng go", 1),
    ("be present for $article $noun ", 1),
    ("and as you $verb", 1),
    ("fully present for the $ng now", 1),
    ("feel your in-breath through $article $ng", 1),
    ("bend your $article $ng and $verb trhough it", 1),
  ]
)
```

Giving it a spin:

```
>>> execfile('yoga.py')
>>> ph.generate()
'pull your nostril over the left toes'
>>> ph.generate()
'push the right hip away from your collarbone'
>>> ph.generate()
'and relax'
>>> ph.generate()
'breathe through the pelvis'
```
