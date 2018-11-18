export const Location = {
  'label': 'Location',
  'fields': [
    {
      'label': 'Universe',
      'name': 'universe',
      'type': 'select',
      'options': ['Incoming']
    },
    {
      'label': 'Type of location',
      'name': 'type',
      'type': 'select',
      'options': [
        // Space locations
        'universe',
        'galaxy',
        'star system',
        'space sector',
        'planet',
        // Land locations
        'continent',
        'country',
        'region',
        'state',
        'city',
        'town',
        'village',
        'landmark',
        'building',
        // Water locations
        'ocean',
        'sea',
        'lake',
        'bay',
        'river',
        'pond',
        'stream'
      ]
    },
    {
      'label': 'Name',
      'name': 'name',
      'type': 'text'
    },
    {
      'label': 'Description',
      'name': 'description',
      'type': 'textarea'
    }
  ]
};
