#ifndef VECTOR_H
#define VECTOR_H

struct Vector
{
    double x, y, z;

    Vector();
    Vector(double x, double y, double z);

    double magnitude() const;
    Vector normalize() const;
    double dot(const Vector &other) const;
    Vector cross(const Vector &other) const;
    Vector scale(double s) const;
};

#endif
