#!/usr/bin/env python3

from pandas import DataFrame
import core.config as CFG

# Attributes ( Input )
a = []
#        [ 'adventure', 'active', 'family', 'outdoor', 'wellness', 'couple', 'cultur', 'lowbudget' ]
a.append([           1,        1,        0,         0,          0,        1,        0,          0  ])
a.append([           0,        0,        1,         1,          0,        0,        0,          0  ])
a.append([           1,        0,        0,         1,          0,        0,        0,          1  ])
a.append([           0,        0,        0,         0,          1,        1,        1,          0  ])

attr_data = DataFrame( a, columns=CFG.ATTRIBUTES )

# Type ( Output )
t = []
#        [ 'BedAndBreakfast', 'Campground', 'Hotel', 'Event' ]
t.append([                .4,           .8,      .0,      .6 ])
t.append([                .8,           .3,      .3,      .2 ])
t.append([                .0,           .7,      .0,      .6 ])
t.append([                .0,           .0,      .7,      .4 ])

type_data = DataFrame(t, columns=CFG.TYPES)
