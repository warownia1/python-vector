Introduction
============

Copy ``vector.py`` module file directly into your project folder.

Then, import Vector from vector module
(note lowercase 'v' in module name and uppercase 'V' in class name)

	from vector import Vector

From now, you can use vectors in your program!


Creating a new Vector
=====================

To create a new vector you enter ``Vector(<components>)`` with arbitrary
number of components separated with commas.
examples:

	vec = Vector(2, 3, 4)
	vec = Vector(2.4, 2.64, 0, 2.5)
	vec = Vector(0.001)
	vec = Vector(3.4E16)  # engineering notation meaning 3.4 * 10^16

You can also create a vector from a list:

	l = [2, 5, 9]
	vec = Vector(*l)  # Vector(2, 5, 9)


Vector components
=================

You can access first three vector components as ``x``, ``y`` and ``z`` attributes:

	vec.x  # x-component
	vec.y  # y-component
	vec.z  # z-component

Any component can be accessed in the same way as list elements:

	vec[0]  # first component (x)
	vec[1]  # second component (y)
	vec[99]  # 100th component

Similarly to reading elements you can also set new values to the existing 
components:

	vec = Vector(3, 4, 9)
	vec[0] = 10
	vec.y = -3
	vec  # Vector(10, -3, 9)
	

Also, you can iterate over vector components, convert them to a list or just 
treat as a list:

	vec = Vector(3, 6, 8)
	list(vec)  # converts to a list [3, 6, 8]
	np.array(vec)  # creates one dimensional numpy array array([3, 6, 8])
	
	for comp in vec:
		print(comp)
	# prints:
	# 3
	# 6
	# 8

	[comp**2 for comp in vec]  # [9, 36, 81]

Note that after converting into a list or a numpy array your object is no
longer a vector and loses it's vector properties.


Operations
==========

Addition and subtraction
------------------------
Vectors support addition and subtraction of other vectors.
examples:

	v = Vector(0, 1, 2)
	u = Vector(4, 3, 7)
	v + u  # Vector(4, 4, 9)
	v - u  # Vector(-4, -2, -5)

alternatively, you can execute:

	v.add(u)  # Vector(4, 4, 9)
	Vector.add(v, u)  # Vector(4, 4, 9)
	v.sub(u)  # Vector(-4, -2, -5)
	Vector.sub(u, v)  # Vector(4, 2, 5)

Negative vector
---------------
Get the vector with the opposite direction.

	vec = Vector(1,2,3)
	-vec  # Vector(-1, -2, -3)

Dot product
-----------
You can take a dot product of two vectors in a following way:

	v.dot(u)  # 17
	Vector.dot(v, u)  # 17

Norm and unit vector
--------------------
Norm (magnitude) is obtained with ``norm()`` function or as the absolute value of 
the vector:

	v.norm()  # 2.23606797749979
	abs(v)  # 2.23606797749979

Unit vector:

	v.unit()  # Vector(0.0, 0.4472135954999579, 0.8944271909999159)

Transformation
--------------
You can multiply the vector by a transformation matrix using ``transform(<matrix>)`` method.
The matrix should be a list of lists.
Each inner list represents the row of the matrix and its length must be equal to the vector's length.

example:

	matrix = [[1, 3, 5],
	          [2, 0, 0]]
	vec = Vector(3, 1, -1)
	vec.transform(matrix)  # Vector(1, 4)

Additional functions
====================

You can convert the vector into a nice looking string of components using ``str(vec)``.
The components are rounded to three significant figures and they are enclosed in round brackets.

example:

	vec = Vector(42345362, 0.00000345, 3.8572038475, 467.23652E-20)
	str(vec)  # '(4.23E+07, 3.45E-06, 3.86, 4.67E-18)'

You can change the number of significant figures using:

	Vector.set_sig_fig(<figures>)
	
and brackets used with:

	Vector.set_brackets(<type>)
	
allowed types are: ``'('``, ``'['``, ``'{'``, ``' '``, ``'<'``

example:

	vec = Vector(42345362, 0.00000345, 3.8572038475, 467.23652E-20)
	str(vec)  # '(4.23E+07, 3.45E-06, 3.86, 4.67E-18)'
	Vector.set_sig_fig(1)
	Vector.set_brackets('<')
	str(vec)  # '<4E+07, 3E-06, 4, 5E-18>'
