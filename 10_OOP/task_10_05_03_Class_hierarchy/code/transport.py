import datetime
import time

class TransportError(Exception):
    pass

class Transport:
    ''' Абстрактный класс для всех транспортных средств.
    '''
    
    def __init__(self, color, max_speed, acceleration, seats, passengers = 0, driver_inside = False):
        ''' self._color - (str) 
            self.__max_speed - (float) m/s
            self.__acceleration - (float) m^2/s
            self._seats - (int)
            self._passengers - (int)
            self._driver_inside - (false)
            
            self._target_speed - (float)
            self._start_time - (datetime.datetime)
        '''
        assert 0 < max_speed < (3 * 10**8) and acceleration > 0 and 0 <= passengers < seats
        self._color = color
        self.__max_speed = max_speed
        self.__acceleration = acceleration
        self._seats = seats
        self._passengers = passengers
        self._driver_inside = driver_inside
        
        self._target_speed = 0
        self._start_time = None     
        
    def __str__(self):
        return 'Transport object:\n'\
               '    Color: {}\n'\
               '    Max Speed: {} m/s\n'\
               '    Acceleration: {} m/s^2\n'\
               '    Seats: {}'.format(self._color,
                                    self.__max_speed,
                                    self.__acceleration,
                                    self._seats)
         
        
    def go(self, target_speed = None):
        ''' target_speed - (int)
        '''
        if target_speed is None:
            target_speed = self.__max_speed
        if not self._driver_inside or self._is_going() or target_speed > self.__max_speed:
            raise TransportError('Driver must be inside. Transport mustn\'t go.')
        self._start_time = datetime.datetime.now()
        self._target_speed = target_speed
    
    def stop(self):
        self._target_speed = 0
        self._start_time = None
        
    def _time(self):
        ''' Return (float) seconds from start of ride.
        '''
        
        return (datetime.datetime.now() - self._start_time).total_seconds()
                
    def _check_distance(self):
        ''' Return (float) distance from start of ride.
        '''
        seconds = self._time()
        acceleration_time = self._target_speed/self.__acceleration
        if seconds > acceleration_time:
            seconds = seconds - acceleration_time
        else:
            acceleration_time = seconds
            seconds = 0
        distance = acceleration_time**2 * self.__acceleration / 2 + seconds * self._target_speed
        
        return distance
        
       
    def _is_going(self):
        ''' Return True, if Transport is going.
            Otherwise False.
        '''
        if self._start_time:
            return True
        else:
            return False
    
    def check_condition(self):
        ''' Return (tuple). 
            (True, self._check_distance()), if self._is_going() is True.
            Otherwise (False, None).
        '''
        res = self._is_going()
        return res, (self._check_distance() if res else None) 

    def get_in(self):
        if self._driver_inside:
            raise TransportError('Driver is inside.')
        self._driver_inside = True 
        
    def get_out(self):
        if not self._driver_inside:
            raise TransportError('There isn\'t driver.')
        self._driver_inside = False
        
    def add_passenger(self):
        if self._passengers + 1 >= self._seats:
            raise TransportError('Seats are fulled.')
        self._passengers += 1
        
    def remove_passenger(self):
        if self._passengers == 0:
            raise TransportError('There are no passengers.')
        self._passengers -= 1
        
    @property
    def color(self):
        return self._color
        
    @property
    def max_speed(self):
        return self.__max_speed  
        
    @property
    def acceleration(self):
        return self.__acceleration   

    @property
    def driver_inside(self):
        return self._driver_inside   
        
    @property
    def seats(self):
        return self._seats   
        
    @property
    def passengers(self):
        return self._passengers   
        
    @property
    def start_time(self):
        return self._start_time   
        
    @property
    def target_speed(self):
        return self._target_speed    
    
class WaterTransport(Transport):
    
    def __init__(self, color, max_speed, acceleration, seats, max_weight, cargo_weight = 0, passengers = 0, driver_inside = False):
        ''' Fields from SuperClass: 
            self._color - (str) 
            self.__max_speed - (float) m/s
            self.__acceleration - (float) m^2/s
            self._seats - (int)
            self._passengers - (int)
            self._driver_inside - (false)
            
            self._target_speed - (float)
            self._start_time - (datetime.datetime)
            
            Specific Fields: 
            self.__max_weight - (float) kg
            self._flow - (float) flow in the opposite direction
        '''
        assert max_weight > seats * 80 + cargo_weight
        
        self.__max_weight = max_weight
        self._cargo_weight = cargo_weight
        self._flow = None
        super().__init__(color, max_speed, acceleration, seats, passengers, driver_inside)
        
    def __str__(self):
                return 'WaterTransport object:\n'\
               '    Color: {}\n'\
               '    Max Speed: {} m/s\n'\
               '    Acceleration: {} m/s^2\n'\
               '    Seats: {}\n'\
               '    Max Weight: {} kg'.format(self._color,
                                    self.max_speed,
                                    self.acceleration,
                                    self._seats,
                                    self.__max_weight)
    
    def go(self, target_speed = None, flow = 0):
        if flow >= (target_speed if target_speed else self.max_speed):
            raise TransportError('flow is higher than target_speed.')
        self._flow = flow
        super().go(target_speed)
    
    def _check_distance(self):
        ''' Return (int) distance from start of ride.
        '''
        distance = super()._check_distance() - self._flow*self._time()
        return distance
    
    def stop(self):
        self._flow = None
        super().stop()
        
    def add_cargo(self, weight):
        if weight > self.__max_weight - self._cargo_weight - self._seats * 80:
            raise TransportError('Too much weight.')
        self._cargo_weight += weight
    
    def remove_cargo(self, weight):
        if weight > self._cargo_weight:
            raise TransportError('Too much weight.')
            
    @property
    def max_weight(self):
        return self.__max_weight
    
    @property
    def cargo_weight(self):
        return self._cargo_weight
    
    @property
    def flow(self):
        return self._flow
    
class Vehicle(Transport):
    
    def __init__(self, wheels, color, max_speed, acceleration, seats, passengers = 0, driver_inside = False, opened = False):
        ''' Fields from SuperClass: 
            self._color - (str) 
            self.__max_speed - (float) m/s
            self.__acceleration - (float) m^2/s
            self._seats - (int)
            self._passengers - (int)
            self._driver_inside - (false)
            
            self._target_speed - (float)
            self._start_time - (datetime.datetime)
            
            Specific Fields: 
            self._wheels - (int)
            self.__opened - (bool)
        '''
        
        assert wheels >=1
        self._wheels = wheels
        self.__opened = opened
        super().__init__(color, max_speed, acceleration, seats, passengers, driver_inside)
    
    def __str__(self):
        return 'Vehicle object:\n'\
               '    Color: {}\n'\
               '    Max Speed: {} m/s\n'\
               '    Acceleration: {} m/s^2\n'\
               '    Seats: {}\n'\
               '    Wheels: {}'.format(self._color,
                                    self.max_speed,
                                    self.acceleration,
                                    self._seats,
                                    self._wheels)
        
    def open(self):
        self.__opened = True
        
    def close(self):
        self.__opened = False
        
    def get_in(self):
        if not self.__opened:
            raise TransportError('Vehicle must be opened.')
        super().get_in()
    
    def get_out(self):
        if not self.__opened:
            raise TransportError('Vehicle must be opened.')
        super().get_out()
        
    def add_passenger(self):
        if not self.__opened:
            raise TransportError('Vehicle must be opened.')
        super().add_passenger()
        
    def remove_passenger(self):
        if not self.__opened:
            raise TransportError('Vehicle must be opened.')
        super().remove_passenger()

    @property
    def wheels(self):
        return self._wheels
    
    @property
    def opened(self):
        return self.__opened
                
class Car(Vehicle):
    def __init__(self, tank, fuel_consumption, wheels, color, max_speed, acceleration, seats, fuel = 0, passengers = 0, driver_inside = False, opened = False):
        ''' Fields from SuperClass (Transport): 
            self._color - (str) 
            self.__max_speed - (float) m/s
            self.__acceleration - (float) m^2/s
            self._seats - (int)
            self._passengers - (int)
            self._driver_inside - (false)
            
            self._target_speed - (float)
            self._start_time - (datetime.datetime)
            
            Fields from SuperClass (Vehicle):
            self._wheels - (int)
            self.__opened - (bool)
            
            Specific Fields: 
            self._fuel - (float)
            self.__tank - (float)
            self.__fuel_consumption - (float)
        '''
        assert 0 <= fuel < tank and fuel_consumption > 0
        self._fuel = fuel
        self.__tank = tank
        self.__fuel_consumption = fuel_consumption
        super().__init__(wheels, color, max_speed, acceleration, seats, passengers, driver_inside, opened)
    
    def __str__(self):
        return 'Car object:\n'\
               '    Color: {}\n'\
               '    Max Speed: {} m/s\n'\
               '    Acceleration: {} m/s^2\n'\
               '    Seats: {}\n'\
               '    Wheels: {}\n'\
               '    Tank: {} l\n'\
               '    Fuel Consumtion: {} l/100km '.format(self._color,
                                    self.max_speed,
                                    self.acceleration,
                                    self._seats,
                                    self._wheels,
                                    self.__tank,
                                    self.__fuel_consumption)
    
    def go(self, target_speed = None):
        if self._fuel == 0:
            raise TransportError('There isn\'t fuel.')
        super().go(target_speed)
        
    def stop(self):
        super().stop()
        self._fuel = self._fuel - (self.__fuel_consumption/1000)*self.check_condition()[1]
    
    def check_condition(self):
        condition = list(super().check_condition())
        if condition[0]:
            if condition[-1] > self._fuel/(self.__fuel_consumption/1000):
                condition[0] = False
                condition[-1] = self._fuel/(self.__fuel_consumption/1000)
                super().stop()
            self._fuel = self._fuel - (self.__fuel_consumption/1000)*condition[-1]
        condition.append(self._fuel)

        return tuple(condition)
        
    def tank_up(self, volume):
        if volume > self.__tank - self._fuel:
            raise TransportError('Too much fuel.')
        self._fuel += volume
        
    @property
    def tank(self):
        return self.__tank
    
    @property
    def fuel(self):
        return self._fuel
        
    @property
    def fuel_consumption(self):
        return self.__fuel_consamption

