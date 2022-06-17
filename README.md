# Angry-Birds-Game

Using, physics equations and concepts you can code the trajectory of a projectile and the subsequent motion when it hits a target. These equations and concepts include, momentum, torque, equations of motion and newtons laws. These equations and concepts will be used to code the trajectory of a 'bird' and also what happens if it hits a tall, rectangular target. The user will be able to input their own initial conditions of velocity and angle of trajectory with the aim of toppling the target. 

## The motion of the 'bird' and the momentum arrow:

### Equations of motion
$$ r_x = x_0 + v_0 t \cos \theta   
\quad\quad \text{(Equation 1)} $$

$$ r_y = y_0 + v_0 t  \sin \theta -\frac{1}{2}g t^2
\quad\quad \text{(Equation 2)} $$

### Equations of momentum:
Since momentum is defined as

$$ \mathbf{p} = m  \frac{d \mathbf{r}}{dt} 
\quad\quad \text{(Equation 3)} $$

we can express the momentum of the projectile as

$$ p_x = m v_0 \cos \theta
\quad\quad \text{(Equation 4)} $$

$$ p_y = m v_0 \sin \theta - m g t 
\quad\quad \text{(Equation 5)} $$

## Will the bird topple the target? and Toppling the target


### Equations used:
Restoring Torque:  

$$\mathbf{T}_{restoring} = \mathbf{F}_{grav} \times \mathbf{d}_r \quad\quad \text{(Equation 6)} $$

$$where  \mathbf{F}_{grav} = m\mathbf{g}\quad\quad \text{(Equation 7)}\quad and\quad  \mathbf{d}_r = width/2 \quad\quad \text{(Equation 8)} $$

Applied Torque: 

$$\mathbf{T}_{applied} = \mathbf{F}_{applied} \times \mathbf{d}_a \quad\quad \text{(Equation 9)} $$

$$where \quad \mathbf{T}_{applied} = \text{momentum of ball/contact  time} \quad\quad \text{(Equation 10)}\quad and\quad \mathbf{d}_r = \text{the vector from the rotation point and contact point} $$

$$ \mathbf{T}_{applied} > \mathbf{T}_{restoring} \quad\quad \text{(Equation 11)} $$


##### Conclusion:

I would make improvements to the physics of this game by adding resistive forces. For example, adding air resistance by including a constant opposing force in the motion equations. This force would increase as the speed of the bird increases. Also, I would include friction between the bird and the target. This would mean, that some momentum would be lost, therefore I would code a momentum transfer to the target that is less than the momentum of the bird. Furthermore, I would not assume that all of the momentum is transferred. Instead, I would use the concept of coefficient of restitution in the equations of momentum. This would tell us the respective momentums of the bird and the target, after the collision.
