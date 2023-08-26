#ifndef PLANE_H
#define PLANE_H

#include "point.hpp"

class Plane
{
public:
    Plane(const Point &point, const Vector &normal, const Vector &color);

    // Função para verificar a interseção entre um raio e o plano
    bool intersect(const Point &rayOrigin, const Vector &rayDirection, double &t) const;

private:
    Point point;
    Vector normal;
    Vector color;
};

#endif