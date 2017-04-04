import langine

yoga = langine.controller()

full_noun_group = langine.phrase(
  'fng',
  yoga,
  [("$article $ng", 1)],
)

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
    ("inside", 1),
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
    ("$verb $fng $dir $fng", 10),
    ("breathe through $article $noun", 2),
    ("and relax", 1),
    ("let $fng go", 1),
    ("be present in $article $noun ", 1),
    ("$ph and as you $verb $ph", 1),
    ("be fully present for the $ng now", 1),
    ("feel your in-breath through $fng", 1),
    ("bend your $fng and $verb through it", 1),
    ("$phrase and $phrase", 1),
    ("$verb $dir $fng", 2),
    ("$phrase with $fng above $fng", 1),
    ("keeping $fng $dir $fng", 1),
    ("straighten $fng", 1)

  ]
)
