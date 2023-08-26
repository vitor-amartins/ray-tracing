#ifndef POINT_H
#define POINT_H

#include "vector.hpp"

struct Point
{
    double x, y, z;

    Point() : x(0.0), y(0.0), z(0.0) {}
    Point(double x, double y, double z) : x(x), y(y), z(z) {}

    double distanceTo(const Point &other) const;
    Vector difference(const Point &other) const;
    Point translate(const Vector &v) const;
};

#endif