class Aqua:

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        elif isinstance(other, Aqua):
            return Wave()
        else:
            return None


class Air:

    def __add__(self, other):
        if isinstance(other, Aqua):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Air):
            return Vortex()
        else:
            return None


class Fire:

    def __add__(self, other):
        if isinstance(other, Aqua):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None


class Earth:

    def __add__(self, other):
        if isinstance(other, Aqua):
            return Steam()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Storm:

    def __str__(self):
        return 'Storm'


class Steam:

    def __str__(self):
        return 'Steam'


class Mud:

    def __str__(self):
        return 'Mud'


class Lightning:

    def __str__(self):
        return 'Lightning'


class Dust:

    def __str__(self):
        return 'Dust'


class Lava:

    def __str__(self):
        return 'Lava'


class Wave:

    def __str__(self):
        return 'Wave'


class Vortex:

    def __str__(self):
        return 'Vortex'
