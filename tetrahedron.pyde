from __future__ import division
    
def setup():
    size(800,800,P3D)
    #noStroke()
    stroke(50)
    
def draw():
    background(0)#black
    #translate to center
    translate(400,400)
    #rotations by mouse or auto
    rotx = frameCount/80.0# map(mouseY,0,600,0,TWO_PI)
    rotateX(-rotx)
    roty = frameCount/80.0#map(mouseX,0,600,0,TWO_PI)
    rotateY(-roty)
    rotateZ(-frameCount/160.0)
    gasket(300,6)
    
def tetrahedron(sz):
    '''How to make one tetrahedron
    drawn from its center'''
    #handy variables
    d1,d2 = 0.5*sz, 0.866*sz

    #front
    fill(255,0,0)
    beginShape(TRIANGLES);
    vertex(0, -sz,0);
    vertex(d2, d1,d1)
    vertex(-d2, d1,d1)
    endShape();
    
    #sides
    #fill(0,255,0)
    beginShape(TRIANGLES);
    vertex(0, -sz,0);
    vertex(d2, d1,d1)
    vertex(0, d1,-sz)
    endShape();
    
    #fill(0,0,255)
    beginShape(TRIANGLES);
    vertex(0, -sz,0);
    vertex(-d2, d1,d1)
    vertex(0, d1,-sz)
    endShape();
    
    #bottom
    #fill(0,255,255)
    beginShape(TRIANGLES)
    vertex(-d2, d1,d1)
    vertex(d2, d1,d1)
    vertex(0, d1,-sz)
    
    endShape()
    
def gasket(sz, level):
    '''Fractal of tetrahedrons: a 
    3D Sierpinski triangle'''
    d1, d2 = 0.5*sz, 0.866*sz
    if level == 1:
        #translate(0,-sz,0)
        tetrahedron(sz)
    else:
        pushMatrix()
        #top tetra
        translate(0,-sz/2,0)
        gasket(sz/2.0,level-1)
        popMatrix()
        #3 bottom tetras:
        pushMatrix()
        translate(-d2/2, d1/2,d1/2)
        gasket(sz/2.0,level-1)
       
        popMatrix()
        pushMatrix()
        translate(d2/2, d1/2,d1/2)
        gasket(sz/2.0,level-1)
        popMatrix()

        pushMatrix()
        translate(0, d1/2,-sz/2)
        gasket(sz/2.0,level-1)
        popMatrix()
        
    