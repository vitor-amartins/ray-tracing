#include <cmath>

#include "vector.hpp"

struct Point
{
    double x, y, z;

    Point() : x(0.0), y(0.0), z(0.0) {}
    Point(double x, double y, double z) : x(x), y(y), z(z) {}

    // Distância entre dois pontos
    double distanceTo(const Point &other) const
    {
        double dx = x - other.x;
        double dy = y - other.y;
        double dz = z - other.z;
        return std::sqrt(dx * dx + dy * dy + dz * dz);
    }

    Vector difference(const Point &other) const
    {
        return Vector(x - other.x, y - other.y, z - other.z);
    }

    Point translate(const Vector &v) const
    {
        return Point(x + v.x, y + v.y, z + v.z);
    }
};
