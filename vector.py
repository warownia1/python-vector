import math


class Vector(object):
    
    SIG_FIG = 3
    BRACKETS = ('(', ')')
    
    _bracket_types = {
        '(': ('(', ')'),
        '[': ('[', ']'),
        '{': ('{', '}'),
        ' ': ('', ''),
        '<': ('<', '>')
    }
    
    def __init__(self, *args):
        if len(args) == 0:
            raise TypeError("Cannot create an empty vector")
        for comp in args:
            if not isinstance(comp, (int, float)):
                raise TypeError("Vector component must be a number")
        self.components = list(args)

    def __getattr__(self, name):
        if name == "size":
            return len(self)
        if name == 'x':
            return self.components[0]
        if name == 'y' and len(self) >= 2:
            return self.components[1]
        if name == 'z' and len(self) >= 3:
            return self.components[2]
        raise AttributeError(
            "'Vector' object has no attribute '{}'".format(name)
        )
        
    def __setattr__(self, name, value):
        if name == 'x':
            self.components[0] = value
        elif name == 'y':
            self.components[1] = value
        elif name == 'z':
            self.components[2] = value
        else:
            super().__setattr__(name, value)
        
    def __getitem__(self, index):
        return self.components[index]
        
    def __setitem__(self, index, value):
        self.components[index] = value
        
    def __add__(self, vec):
        if not isinstance(vec, Vector):
            raise TypeError("Can't add non-vector")
        if len(self) != len(vec):
            raise TypeError("Can't add vectors with different dimensions")
        components = [s + t for (s, t) in zip(self.components, vec.components)]
        return Vector(*components)
        
    def __sub__(self, vec):
        if not isinstance(vec, Vector):
            raise TypeError("Can't subtract non-vector")
        if len(self) != len(vec):
            raise TypeError("Can't subtract vectors with different dimensions")
        components = [s - t for (s, t) in zip(self.components, vec.components)]
        return Vector(*components)
        
    def __neg__(self):
        return Vector(*[-c for c in self.components])
        
    def __pos__(self):
        return self
        
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply by scalars")
        components = [x * scalar for x in self.components]
        return Vector(*components)
        
    def __rmul__(self, scalar):
        return self * scalar
        
    def __div__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply by scalars")
        components = [x / scalar for x in self.components]
        return Vector(*components)
        
    def __len__(self):
        return len(self.components)
        
    def __abs__(self):
        return self.norm()
        
    def __repr__(self):
        return "Vector(" + ", ".join(map(str, self.components)) + ")"
        
    def __str__(self):
        return Vector.BRACKETS[0] + ", ".join(
            "{{:.{}G}}".format(Vector.SIG_FIG).format(c)
            for c in self.components
        ) + Vector.BRACKETS[1]
        
    def __iter__(self):
        return self.components.__iter__()
        
    def dot(self, vec):
        if len(self) != len(vec):
            raise TypeError("Can't take the dot product of vectors "\
                            "with different sizes")
        if not isinstance(vec, Vector):
            raise TypeError("Can't take the dot product of non-vector")
        return sum(s * t for (s, t) in zip(self.components, vec.components))
        
    def transform(self, matrix):
        if any(len(row)-len(self.components) for row in matrix):
            raise TypeError("Incorrect number of columns in the matrix")
        components = (
            sum(a*b for (a,b) in zip(row, self.components)) 
            for row in matrix
        )
        return Vector(*components)

    def norm(self):
        return math.sqrt(sum(c*c for c in self.components))      
        
    def unit(self):
        length = self.norm()
        components = [c / length for c in self.components]
        return Vector(*components)
        
    def add(vec1, vec2):
        return vec1 + vec2
        
    def sub(vec1, vec2):
        return vec1 - vec2
        
    @staticmethod
    def set_sig_fig(figures):
        if type(figures) is not int:
            raise TypeError("The number must be an integer")
        if figures <= 0:
            raise ValueError("The number must be positive")
        Vector.SIG_FIG = figures
        
    @staticmethod
    def set_brackets(bracket_type):
        Vector.BRACKETS = Vector._bracket_types[bracket_type]
