#! /usr/bin/python

import langine

yoga = langine.controller()

full_noun_group = langine.phrase(
  'fng',
  yoga,
  [("$article $ng", 10)],
)

noun_group = langine.phrase(
  'ng',
  yoga,
  [
    ("$noun", 10),
    ("$adj $noun", 10)
  ],
)

noun = langine.phrase(
  'noun',
  yoga,
  [
    ("arm", 10),
    ("leg", 10),
    ("torso", 10),
    ("fingertip", 10),
    ("toes", 10),
    ("toe", 10),
    ("pelvis", 10),
    ("hip", 10),
    ("knee", 10),
    ("thigh", 10),
    ("back", 10),
    ("nostril", 10),
    ("collarbone", 10),
    ("wrist", 10),
    ("forearm", 10),
    ("eyeball", 10),
    ("coccyx", 5),
    ("spleen", 5),
    ("knuckle", 5),
    ("hamstring", 5),
    ("heel", 5),
    ("shoulder", 5),
  ],
)

adj = langine.phrase(
  'adj',
  yoga,
  [
    ("left", 30),
    ("right", 30),
    ("upper right", 10),
    ("lower right", 10),
    ("upper left", 10),
    ("lower left", 10),
  ]
)

article = langine.phrase(
  'article',
  yoga,
  [
    ("the", 10),
    ("your", 10),
  ],
)

direction = langine.phrase(
  'dir',
  yoga,
  [
    ("towards", 2),
    ("away from", 2),
    ("in line with", 10),
    ("over", 10),
    ("across", 10),
    ("inside", 10),
  ],
)

verb = langine.phrase(
  'verb',
  yoga,
  [
    ("push", 30),
    ("pull", 30),
    ("breathe", 10),
    ("expand", 10),
    ("exhale", 10),
    ("inhale", 10),
    ("align", 5),
    ("release", 5),
    ("stretch", 10),
    ("relax", 10),
    ("straighten", 10)
  ],
)

ph = langine.phrase(
  'phrase',
  yoga,
  [
    ("$verb $fng $dir $fng", 10),
    ("breathe through $article $noun", 2),
    ("and relax", 10),
    ("$verb $fng", 10),
    ("let $fng go", 10),
    ("be present in $article $noun ", 10),
    ("$phrase and as you $verb $phrase", 10),
    ("be fully present for the $ng now", 10),
    ("feel your in-breath through $fng", 10),
    ("bend your $fng and $verb through it", 10),
    ("$phrase and $phrase", 10),
    ("$verb $dir $fng", 2),
    ("$phrase with $fng above $fng", 10),
    ("keeping $fng $dir $fng", 10),
  ]
)

print(ph.generate())
