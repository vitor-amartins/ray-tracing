#include "point.hpp"

class Camera
{
public:
    Camera(const Point &C, const Point &M, const Vector &Vup, double distanceToScreen, int screenHeight, int screenWidth);

private:
    Point C;                 // Posição da câmera
    Point M;                 // Ponto para onde a câmera está apontando
    Vector Vup;              // Vetor up
    double distanceToScreen; // Distância da câmera para a tela
    int screenHeight;        // Altura da tela
    int screenWidth;         // Largura da tela

    Vector w, v, u; // Vetores da base ortonormal

    // Calcula os vetores da base ortonormal
    void calculateBase();
};

Camera::Camera(const Point &C, const Point &M, const Vector &Vup, double distanceToScreen, int screenHeight, int screenWidth) : C(C), M(M), Vup(Vup), distanceToScreen(distanceToScreen), screenHeight(screenHeight), screenWidth(screenWidth)
{
    calculateBase();
}

void Camera::calculateBase()
{
    w = C.difference(M).normalize();
    u = Vup.cross(w).normalize();
    v = w.cross(u);
}
