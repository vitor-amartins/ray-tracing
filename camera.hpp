#ifndef CAMERA_H
#define CAMERA_H

#include "point.hpp"

class Camera
{
public:
    Camera(const Point &C, const Point &M, const Vector &Vup, double distanceToScreen, int screenHeight, int screenWidth);

private:
    Point C;
    Point M;
    Vector Vup;
    double distanceToScreen;
    int screenHeight;
    int screenWidth;

    Vector w, v, u;

    void calculateBase();
};

#endif
