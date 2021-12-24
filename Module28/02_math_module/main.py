class MyMath:
    PI = 3.141592653589793238462643

    @classmethod
    def circle_len(cls, radius) -> float:
        return 2 * cls.PI * radius

    @classmethod
    def circle_sq(cls, radius) -> float:
        return cls.PI * (radius ** 2)

    @classmethod
    def vol_cube(cls, length) -> float:
        return length ** 3

    @classmethod
    def sph_sur_area(cls, radius) -> float:
        return 4 * cls.PI * (radius ** 2)

    @classmethod
    def vol_shp(cls, radius) -> float:
        return 4 / 3 * cls.PI * (radius ** 3)


res_1 = MyMath.circle_len(5)
res_2 = MyMath.circle_sq(6)
print(res_1)
print(res_2)
