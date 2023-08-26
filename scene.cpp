#include "scene.hpp"

Scene::Scene(const Vector &ambientColor, const std::vector<Light> &lights)
    : ambientColor(ambientColor), lights(lights) {}

Vector Scene::getAmbientColor() const
{
    return ambientColor;
}

const std::vector<Light> &Scene::getLights() const
{
    return lights;
}