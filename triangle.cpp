#include "triangle.hpp"

Triangle::Triangle(const Point &p0, const Point &p1, const Point &p2, const Vector &color)
    : p0(p0), p1(p1), p2(p2), color(color)
{
    calculateNormal();
}

bool Triangle::intersect(const Point &rayOrigin, const Vector &rayDirection, double &t) const
{
    // Verifica a interseção com o plano que contém o triângulo
    Plane containingPlane = getContainingPlane();
    if (!containingPlane.intersect(rayOrigin, rayDirection, t))
    {
        return false; // Não há interseção com o plano
    }

    // Calcula o ponto de interseção no plano
    Point intersectionPoint = rayOrigin.translate(rayDirection.scale(t));

    // Calcula as coordenadas baricêntricas
    Vector edge0 = p1.difference(p0);
    Vector edge1 = p2.difference(p0);
    Vector intersectionVec = intersectionPoint.difference(p0);

    double dot00 = edge0.dot(edge0);
    double dot01 = edge0.dot(edge1);
    double dot11 = edge1.dot(edge1);
    double dotP0 = intersectionVec.dot(edge0);
    double dotP1 = intersectionVec.dot(edge1);

    double invDenom = 1.0 / (dot00 * dot11 - dot01 * dot01);

    // Calcula os valores de alpha, beta e gamma
    double alpha = (dot11 * dotP0 - dot01 * dotP1) * invDenom;
    double beta = (dot00 * dotP1 - dot01 * dotP0) * invDenom;
    double gamma = 1.0 - alpha - beta;

    // Verifica se os valores estão dentro dos limites adequados
    return (alpha >= 0.0 && beta >= 0.0 && gamma >= 0.0 && alpha <= 1.0 && beta <= 1.0 && gamma <= 1.0);
}

void Triangle::calculateNormal()
{
    Vector edge1 = p1.difference(p0);
    Vector edge2 = p2.difference(p0);
    normal = edge1.cross(edge2).normalize();
}

Plane Triangle::getContainingPlane() const
{
    return Plane(p0, normal, color);
}
