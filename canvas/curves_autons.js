// in inches from lower left corner
// note the robot with bumbers is ~39x34
var control_points =
[
  // center switch - left
  [
    { x: 20,  y: 156  },
    { x: 48,  y: 156  },
    { x: 95,  y: 222 },
    { x: 120, y: 222 }
  ],
  // center switch - left - second cube lineup
  [
    { x: 120,  y: 222  },
    { x: 95,  y: 222  },
    { x: 70,  y: 162 },
    { x: 50, y: 162 }
  ],
  // center switch - left - second cube pickup
  [
    {x: 50, y: 162},
    {x: 80, y: 162}
  ],
  // center switch - left -  second cube position for score
  [
    {x: 80, y: 162},
    {x: 55, y: 162},
    {x: 50, y: 150}
  ],
  // center switch - left - second cube drop off
  [
    {x: 50, y: 150},
    {x: 90, y: 222},
    {x: 120, y: 222}
  ],
  // center switch - right
  [
    { x: 20,  y: 156  },
    { x: 48,  y: 156  },
    { x: 95,  y: 102 },
    { x: 120, y: 102 }
  ],
  // center switch - right - second cube lineup
  [
    { x: 120,  y: 102  },
    { x: 90,  y: 102  },
    { x: 65,  y: 162 },
    { x: 50, y: 162 }
  ],
  // center switch - right - second cube pickup
  [
    {x: 50, y: 162},
    {x: 80, y: 162}
  ],
  // center switch - right - second cube position for score
  [
    {x: 80, y: 162},
    {x: 55, y: 162},
    {x: 50, y: 176}
  ],
  // center switch - right - second cube drop off
  [
    {x: 50, y: 176},
    {x: 85, y: 102},
    {x: 120, y: 102}
  ],
  //center switch - right - drive to scale on right side from switch
  [
    {x: 120, y: 102},
    {x: 45, y: 102},
    {x: 60, y: 30},
    {x: 230, y: 70},
    {x: 245, y: 60}
  ],
  //center switch - right - drive to scale on left side from switch
  [
    {x: 120, y: 102},
    {x: 45, y: 102},
    {x: 60, y: 260},
    {x: 230, y: 260},
    {x: 245, y: 280}
  ],
  // center switch - second cube to right scale
  [
    {x: 80, y: 162},
    {x: 30, y: 162},
    {x: 40, y: 40},
    {x: 323, y: 70},
    {x: 323, y: 25}
  ],
  // center switch - second cube place on right scale
  [
    {x: 323, y: 25},
    {x: 323, y: 75}
  ],
  // center switch - second cube to left scale
  [
    {x: 80, y: 162},
    {x: 30, y: 162},
    {x: 40, y: 284},
    {x: 323, y: 254},
    {x: 323, y: 299},
  ],
  // center switch - second cube place on right scale
  [
    {x: 323, y: 299},
    {x: 323, y: 273}
  ],
  // center far scale - left
  [
    { x: 20,  y: 156  },
    { x: 48,  y: 156  },
    { x: 120,  y: 46 },
    { x: 242, y: 46 },
    { x: 232, y: 226 },
    { x: 250, y: 258 },
    { x: 275, y: 252 }
  ],
  // center far scale - right
  [
    { x: 20,  y: 156  },
    { x: 48,  y: 156  },
    { x: 120,  y: 278 },
    { x: 242, y: 278 },
    { x: 232, y: 98 },
    { x: 250, y: 66 },
    { x: 275, y: 72 }
  ]
];
