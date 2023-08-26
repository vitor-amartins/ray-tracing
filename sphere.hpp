#ifndef SPHERE_H
#define SPHERE_H

#include "point.hpp"

class Sphere
{
public:
    Sphere(const Point &center, double radius, const Vector &color);

    // Função para verificar a interseção entre um raio e a esfera
    bool intersect(const Point &rayOrigin, const Vector &rayDirection, double &t) const;

private:
    Point center;
    double radius;
    Vector color;
};

#endif
