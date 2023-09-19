class NationalPark:

    def __init__(self, name):
        self.name = name
        self.trip_list = []
        self.visitor_list = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if (not hasattr(self, 'name')) and isinstance(name_parameter, str) and len(name_parameter) >= 3:
            self._name = name_parameter
        
    def trips(self):
        return self.trip_list
    
    def visitors(self):
        return self.visitor_list
    
    def total_visits(self):
        return len(self.trip_list)
    
    def best_visitor(self):
        return max(self.visitor_list, key=lambda v: len([trip for trip in v.trip_list if trip.national_park is self]))


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        self.visitor.trip_list.append(self)

        if not (national_park in self.visitor.park_list):
            self.visitor.park_list.append(national_park)

        self.national_park.trip_list.append(self)

        if not (visitor in self.national_park.visitor_list):
            self.national_park.visitor_list.append(visitor)

        Trip.all.append(self)


    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, new_date):
        if type(new_date) == str and len(new_date) >= 7:
            self._start_date = new_date

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, date):
        if isinstance(date, str) and len(date) >= 7:
            self._end_date = date

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if type(visitor) == Visitor:
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, park):
        if type(park) == NationalPark:
            self._national_park = park



class Visitor:

    def __init__(self, name):
        self.name = name
        self.trip_list = []
        self.park_list = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if type(name_parameter) == str and 1 <= len(name_parameter) <= 15:
            self._name = name_parameter
        
    def trips(self):
        return self.trip_list
    
    def national_parks(self):
        return self.park_list
    
    def total_visits_at_park(self, park):
        if not park.visitors():
            return 0
        return len([trip for trip in self.trip_list if trip.national_park == park])