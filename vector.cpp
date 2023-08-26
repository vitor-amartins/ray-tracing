#include <cmath>

struct Vector
{
    double x, y, z;

    Vector() : x(0.0), y(0.0), z(0.0) {}
    Vector(double x, double y, double z) : x(x), y(y), z(z) {}

    double magnitude() const
    {
        return std::sqrt(x * x + y * y + z * z);
    }

    // Normalizar
    Vector normalize() const
    {
        double m = magnitude();
        if (m > 0.0)
        {
            return Vector(x / m, y / m, z / m);
        }
        return *this;
    }

    // Produto escalar
    double dot(const Vector &other) const
    {
        return x * other.x + y * other.y + z * other.z;
    }

    // Produto vetorial
    Vector cross(const Vector &other) const
    {
        return Vector(y * other.z - z * other.y,
                      z * other.x - x * other.z,
                      x * other.y - y * other.x);
    }

    // Multiplicação por escalar
    Vector scale(double s) const
    {
        return Vector(x * s, y * s, z * s);
    }
};
