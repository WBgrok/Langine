import langine

yoga = langine.controller()

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
