#!/usr/bin/env python3

from pandas import DataFrame
import core.config as CFG

# Attributes ( Input )
a = []
#        [ 'adventure', 'active', 'family', 'outdoor', 'wellness', 'couple', 'cultur', 'lowbudget' ]
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])
a.append([           0,        0,        0,         0,          0,        0,        0,          0  ])

attr_data = DataFrame( a, columns=CFG.ATTRIBUTES )

# Type ( Output )
t = []
#        [ 'BedAndBreakfast', 'Campground', 'Hotel', 'Event' ]
t.append([                .0,           .0,      .0,      .0 ])

type_data = DataFrame(t, columns=CFG.TYPES)
