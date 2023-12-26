# If using Web VPython, append "Web VPython 3.2" at top without quotes
# If using local Python environment, append "from vpython import *" without quotes

scene.caption = '''To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.'''

# Values for radius for sun and earth below are for modeling, not exact

# Change these values if you'd like to model other systems 

sun_radius=15e9
earth_radius = 0.4*sun_radius

# Earth's approximate distance from sun and velocity at Jan 1
dist_sun_earth=1.47e11
earth_initial_velocity = 29780

sun_mass=2e30
earth_mass=6e24
G=6.67e-11

'''
A Celestial Body is a sphere (VPython) with the following attributes:

position : vector (from VPython)
    represents the position of the celestial body in three dimensional space
color : color (from VPython)
    represents the color of the celestial body in simulation
trail: boolean (from VPython)
    represents the trail in the path of the celestial body in simulation
radius : float
    represents the radius (in m) of a Celestial Body
mass : float
    represents the mass (in kg) of a Celestial Body
p : float
    represents the momentum (in kg * m / s) of a Celestial Body
'''

# The central Celestial Body (that the orbital object revolves around)
central_object=sphere(pos=vector(0,0,0), radius=sun_radius, color=color.orange, make_trail=True)
central_object.mass=sun_mass
#sun.p=vector(0,0,0)*sun.m

# pos vector represents distance between the central object and orbital object 
# with respect to the central object
orbital_object=sphere(pos=vector(dist_sun_earth,0,0), radius=earth_radius, color=color.green, make_trail=True)
orbital_object.mass=earth_mass
orbital_object.p=vector(0,earth_initial_velocity,0)*orbital_object.mass

# Total momentum of system is 0
central_object.p=-(orbital_object.p)

# time step
dt=50

while True:
    rate(1e6)
    # Radius = magnitude of difference of position vectors of two celestial bodies
    
    dist_sun_earth=orbital_object.pos-central_object.pos

    # Newton's law of gravitation
    # Force = -G * m1 * m2 * r hat / r^2

    force_c_on_o=-G*central_object.mass*orbital_object.mass*dist_sun_earth.hat/mag(dist_sun_earth)**2

    # By Newton's third law... 
    force_o_on_c=-force_c_on_o

    # New momentum = original momentum + Impulse ->  original momentum + F * dt

    orbital_object.p=orbital_object.p+(force_c_on_o)*dt
    central_object.p=central_object.p+(force_o_on_c)*dt

    # New position = 
    # change the position of the orbital mass with respect to time
    # x = v * t or x = dx/dt * dt
    central_object.pos=central_object.pos+central_object.p*dt/central_object.mass
    orbital_object.pos=orbital_object.pos+orbital_object.p*dt/orbital_object.mass
