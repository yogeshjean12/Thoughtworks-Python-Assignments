
class Planet:
    ''' Planet details '''

    one_year_in_days = 365.25

    def __init__(self, name, diameter, no_of_moons, length_of_year):
        length_of_year = length_of_year
        self.name = name
        self.no_of_moons = no_of_moons
        self.length_of_year = length_of_year
        self.diameter = int((diameter.split())[0])

    def get_no_of_days(self):
        l = self.length_of_year.split()
        if 'days' in self.length_of_year:
            no_of_days = l[0]
            return 'Number of days in {} is {}'.format(self.name,no_of_days)
        else:
            years=l[0]
            no_of_days = float(years) * self.one_year_in_days
            return 'Number of days in {} is {}'.format(self.name,no_of_days)

    def radius(self):
        return "The radius of planet {} is {}km".format(self.name,self.diameter/2)

def largest_planet(*planets):
    big_size=0
    big_planet=None
    for i in planets:
        if i.diameter > big_size:
            big_size=i.diameter
            big_planet=i.name
    return 'The largest planet in terms of size is {} with {}km'.format(big_planet,big_size)

mercury = Planet('Mercury','4879 km',0,'88 days')
venus   = Planet('Venus','12100 km',0,'225 days')
earth   = Planet('Earth','12755 km',1,'365 days')
mars    = Planet('Mars','6786 km',2,'687 days')
jupiter = Planet('Jupiter','142800 km',79,'12 earth years')
saturn  = Planet('Saturn','120537 km',82,'29.5 earth years')
uranus  = Planet('Uranus','51619 km',27,'84 earth years')
neptune = Planet('Neptune','49529 km',14,'165 earth years')

print(neptune.radius())
print(jupiter.get_no_of_days())
print(largest_planet(mercury, venus, earth, mars, jupiter, saturn, uranus, neptune))
