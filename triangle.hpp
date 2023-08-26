#ifndef TRIANGLE_H
#define TRIANGLE_H

#include "plane.hpp"

class Triangle
{
public:
    Triangle(const Point &p0, const Point &p1, const Point &p2, const Vector &color);

    // Função para verificar a interseção entre um raio e o triângulo
    bool intersect(const Point &rayOrigin, const Vector &rayDirection, double &t) const;

private:
    Point p0, p1, p2;
    Vector color;
    Vector normal;

    // Função privada para calcular a normal do triângulo
    void calculateNormal();
    // Função para obter o plano que contém o triângulo
    Plane getContainingPlane() const;
};

#endif
