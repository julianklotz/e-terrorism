#TYPES = [ 'BedAndBreakfast', 'Campground', 'Hotel', 'LodgingBusiness', 'Event', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'VisualArtsEvent' ]


GROUP_EVENTS = 'GROUP_EVENTS'
GROUP_LODGINGS = 'GROUP_LODGINGS'
GROUP_EAT_AND_DRINK = 'GROUP_EAT_AND_DRINK'
GROUP_SHOPPING = 'GROUP_SHOPPING'
GROUP_POIS = 'GROUP_POIS'
GROUP_ACTIVITIES = 'GROUP_ACTIVITIES'

TYPE_MAP = {
    GROUP_LODGINGS: ['Hotel', 'BedAndBreakfast', 'Campground', 'Hostel', 'Motel', 'Resort', 'LodgingBusiness'],
    GROUP_EVENTS: ['Event', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'VisualArtsEvent']
}

ATTRIBUTES = [ 'adventure', 'active', 'family', 'outdoor', 'wellness', 'couple',
        'culture', 'lowbudget' ]

