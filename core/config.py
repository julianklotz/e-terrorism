
#TYPES = [ 'BedAndBreakfast', 'Campground', 'Hotel', 'LodgingBusiness', 'Event', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'VisualArtsEvent' ]

TYPE_MAP = {
    'LodgingBusiness': ['BedAndBreakfast', 'Campground', 'Hostel', 'Hotel', 'Motel', 'Resort', 'LodgingBusiness'],
    'Event': ['Event', 'BusinessEvent', 'ChildrensEvent', 'ComedyEvent', 'CourseInstance', 'DanceEvent', 'DeliveryEvent', 'EducationEvent', 'ExhibitionEvent', 'Festival', 'FoodEvent', 'LiteraryEvent', 'MusicEvent', 'PublicationEvent', 'SaleEvent', 'ScreeningEvent', 'SocialEvent', 'SportsEvent', 'TheaterEvent', 'VisualArtsEvent']
}

ATTRIBUTES = [ 'adventure', 'active', 'family', 'outdoor', 'wellness', 'couple',
        'culture', 'lowbudget' ]
