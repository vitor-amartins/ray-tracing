#ifndef LIGHT_H
#define LIGHT_H

#include "point.hpp"

class Light
{
public:
    Light(const Point &position, const Vector &intensity);

private:
    Point position;
    Vector intensity;
};

#endif
