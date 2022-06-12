import numpy as np
from vpython import sphere,color,rate,canvas,vector,curve,label,box,cross,mag,random,arrow,cylinder

canvas() #Create a new canvas
#The following 2 lines of code are from the script for the final assignment:
scene = canvas(width=640, height=480, center=vector(8,5,0),range=8, background=color.cyan) #Make a scene such that the origin is on the bottom left(like a positive x,y,z axis)
ground = curve(pos=[(0,0,0),(16,0,0)],color=color.green) #Make the ground the x axis and limit it to 16 units (16 metres)

target_pos = 5 + (random()*10) #This is the x position such that it is a random number between 5 and 15
target = box(pos=vector(target_pos,1,0), color=color.gray(.6), height=2, width=0.5, length=0.5)
target_mass = 100#kg
#Next, we will make a platform so that an object can be thrown from it:
platform = cylinder(pos=vector(0,0,0), color=vector(0.72,0.42,0), height=random(), radius=0.5, axis=vector(0,1,0))

#We will now code the projectile:
bird_mass = 0.1
bird = sphere(pos=vector(0,platform.height + 0.3,0), radius=0.3, color=color.red)
#I added the radius to the height because we want the bottom of the sphere to touch the platform, not the middle

#The user inputs:
initial_v = float(input("Choose an inital velocity of the bird in metres/second:  "))
theta0 = float(input("Choose an angle at which to launch the bird in degrees:  "))
theta = np.radians(theta0)
#The motion equations:
g=9.81
t=0 #Set initial time as 0
dt=0.0001 #Set a timestep
x0=0 #The bird starts at x=0
y0=platform.height + bird.radius #The inital height(height of platform + radius of bird)

rx=x0 #Define rx as equal to x0 INITIALLY then it will change in the while loop
ry=y0 #Define ry as equal to y0 INITIALLY then it will change in the while loop

#Coding the arrow:
pointer = arrow(pos=bird.pos, axis=vector(0,0,0), shaftwidth=0.1, color=color.red)
px=0 #Initially, horizontal momentum will be 0
py=0 #Initially, vertical momentum will be 0


while ry >= bird.radius:
    rate(3000) #I put the rate high so the bird moves close to real time
    t=t+dt #Small changes in the time
    rx = x0 + initial_v*t*np.cos(theta) #The x component of the position of the bird (Equation 1)
    ry = y0 + initial_v*t*np.sin(theta) - (g*(t**2))/2 #The y component of the position of the bird (Equation 2)
    bird.pos=vector(rx,ry,0) #This is to make the position vector of the bird change in the loop
    
    #Now we use this while loop to change the position of the arrow at each step of the animation:
    px = bird_mass*initial_v*np.cos(theta) #Horizontal momentum equation (Equation 4)
    py = bird_mass*initial_v*np.sin(theta) - bird_mass*g*t #Vertical momentum equation (Equation 5)
    pointer.pos=bird.pos #Change the position of the arrow with the position of the bird
    pointer.axis=vector(px,py,0) #Make the azis change as momentum changes so the arrow represents momentum
    

    #TOPPLING THE TARGET:
    F_grav = vector(0,target_mass*g,0) #This is the weight of the target as a vector
    d_r = vector(target.width/2,0,0) #This is the horizontal distance between the point of rotation (i.e. the bottom right corner) and the centre of mass
    restoring_torque = cross(F_grav, d_r) #Equation for restoring torque (cross product) Equation 6
    restoring_torque_mag = mag(restoring_torque) #We will need to use the magnitude and not the vector because python does not allow us to use a vector in equation 11

    momentum_of_ball = vector(px,py,0) #The momentum of the ball as a vector, this is used in equation 10
    applied_force = momentum_of_ball/0.01 #Equation 10

    h= vector(target_pos-(target.width/2)-bird.radius, ry,0) #This is the height that the ball makes contact with the target 
    point_of_rotation = vector(target_pos+(target.width/2),0,0) #Point of rotation as a vector which is the bottom right hand corner of the target
    d_a = point_of_rotation-h #The vector from the point of rotation (bottom right-hand corner of target) to the point of impact, on the left-hand side of the target at height h
    applied_torque = cross(applied_force, d_a) #Equation for applied torque (cross product) Equation 9
    applied_torque_mag = mag(applied_torque)#We will need to use the magnitude and not the vector because python does not allow us to use a vector in equation 11
    
    
    if ry<=2 and target_pos-(target.width/2)-bird.radius <= rx <= target_pos: #These are the possible points of contact between the bird and the target
        ry_new=ry #Define the new vertical motion as (INITIALLY) the previous vertical motion
        t=0 #Set time to zero as there is now a new motion
        
        print("The height of the impact point is {0:0.3f} m".format(ry))
        print("The bird's momentum at the point of impact is", pointer.axis, "kg m/s") 
        print("The applied torque from the ball is", applied_torque, "Nm")
        print("The magnitude of the restoring torque is {0:0.3f} Nm".format(restoring_torque_mag))
    
        while ry_new >= bird.radius: #This will decide what happens to the BALL when it makes contact with the target
            rate(3000)
            t=t+dt #Small changes in the time
            ry_new = ry - 0.5*g*(t**2) #Use the ry equation again but with initial velocity as 0 scince the bird comes to rest
            bird.pos=vector(target_pos-(target.width/2)-bird.radius,ry_new,0) #This will make the ball go in free fall after it comes to rest
    
        #WILL THE TARGET TOPPLE?
        if applied_torque_mag > restoring_torque_mag: #This is the NECCESARY condition to topple the target as shown in Equation 11
            target.rotate(angle=-np.pi/2, axis=vector(0,0,1),origin=vector(target_pos,target.width/2,0)) #This will rotate the target 90 degrees clockwise and put it on the floor
            #Add a label to tell the user that their target has been toppled or not:
            label(pos=vector(8,6,0), text="YOU WIN!!!", background=color.black, height=48)
        
        break #To stop the previous animation from continuing 
    

    
label(pos=vector(8,3,0), text="Unlucky, you did not topple the target. :( Try Again!", background=color.black)
print("The ball landed {0:0.3f} m from the origin".format(rx))

