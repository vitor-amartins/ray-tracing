#include <cmath>

#include "sphere.hpp"

Sphere::Sphere(const Point &center, double radius, const Vector &color)
    : center(center), radius(radius), color(color) {}

bool Sphere::intersect(const Point &rayOrigin, const Vector &rayDirection, double &t) const
{
    // Calcula o vetor entre o centro da esfera e a origem do raio
    Vector rayToCenter = center.difference(rayOrigin);

    // Calcula o coeficiente 'a' da equação quadrática
    double a = rayDirection.dot(rayDirection);

    // Calcula o coeficiente 'b' da equação quadrática
    double b = 2.0 * rayToCenter.dot(rayDirection);

    // Calcula o coeficiente 'c' da equação quadrática
    double c = rayToCenter.dot(rayToCenter) - radius * radius;

    // Calcula o discriminante da equação quadrática
    double discriminant = b * b - 4 * a * c;

    // Verifica se há interseção
    if (discriminant > 0)
    {
        // Calcula as soluções da equação quadrática
        double t1 = (-b - std::sqrt(discriminant)) / (2.0 * a);
        double t2 = (-b + std::sqrt(discriminant)) / (2.0 * a);

        // Verifica se as soluções estão na frente do observador e escolhe a menor
        if (t1 > 0.0 || t2 > 0.0)
        {
            t = (t1 < t2) ? t1 : t2;
            return true;
        }
    }

    return false; // Não houve interseção
}
