#include <cmath>

#include "plane.hpp"

Plane::Plane(const Point &point, const Vector &normal, const Vector &color)
    : point(point), normal(normal.normalize()), color(color) {}

bool Plane::intersect(const Point &rayOrigin, const Vector &rayDirection, double &t) const
{
    // Calcula o numerador da fórmula da interseção do raio com o plano
    double numerator = point.difference(rayOrigin).dot(normal);

    // Calcula o denominador da fórmula da interseção do raio com o plano
    double denominator = rayDirection.dot(normal);

    // Verifica se o raio é paralelo ou quase paralelo ao plano
    if (std::abs(denominator) > 1e-6)
    {
        // Calcula o parâmetro 't' de interseção
        t = numerator / denominator;

        // Verifica se a interseção está na frente do observador
        if (t > 0.0)
        {
            return true;
        }
    }

    return false; // Não houve interseção
}
